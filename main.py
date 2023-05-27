import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from fastapi import Request


app = FastAPI()

origins = [
    "http://127.0.0.1:3000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


class Keywords(BaseModel):
    keywords: list


@app.get("/")
def read_message():
    return {"message": "hello quickdraw"}


@app.post("/api/keyword-image", tags=["keyword-image"])
async def get_images(keywords: Keywords):
    print(keywords)
    return


# run a Uvicorn server on port 8000 and reload on every file change
if __name__ == "__main__":
    uvicorn.run("main:app", port=8080, reload=True)
