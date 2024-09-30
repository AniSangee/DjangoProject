from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/user/{user_id}/")
async def user_data(user_id):
    return {user_id: f"This is the data for user {user_id}"}