from fastapi import FastAPI

app = FastAPI()


@app.get("/users/me")
async def read_users_me():
    return {"user-id": "the current user"}


@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}
