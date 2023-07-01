from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "You've done the first thing"}
