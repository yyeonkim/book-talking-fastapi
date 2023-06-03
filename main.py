import uvicorn
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from quickdraw import QuickDrawData

qd = QuickDrawData()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Keywords(BaseModel):
    keywords: list


@app.post("/api/keyword-image", tags=["keyword-image"])
async def get_images(req: Keywords):
    success = False  # 이미지를 가져오는데 성공하면 True

    for keyword in req.keywords:
        # 두 단어 이상으로 이루어진 문자는 나눠서 확인 (ex. white rabbit)
        keywordList = keyword.lower().split()
        for item in keywordList:
            try:
                result = qd.get_drawing(item)
                success = True
                break
            except:
                continue

    if not success:
        raise HTTPException(status_code=404, detail="Image not found")

    return result


# run a Uvicorn server on port 8000 and reload on every file change
if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
