import os
from model import Account, AccountGetAll
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from database import (
    fetch_one_account,
    fetch_all_account,
    create_account,
    update_account,
    remove_account,
)

app = FastAPI()

origins = [
    "http://localhost:3000",
    "http://localhost:8000",
    os.environ.get("CORS_HOST", None),
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root():
    return {"Go": "FoodMe"}


@app.get("/api/account")
async def get_account():
    response = await fetch_all_account()
    return response


@app.get("/api/account/{id}", response_model=Account)
async def get_account_byid(id: str):
    response = await fetch_one_account(id)
    if response:
        return response
    raise HTTPException(404, f"There is no account with this id.{id}")


@app.post("/api/account", response_model=AccountGetAll)
async def post_account(account: Account):
    response = await create_account(account.dict())
    newdict = {
        "id": str(response["_id"]),
        "name": response["name"],
        "password": response["password"],
        "email": response["email"]
    }
    if response:
        return newdict
    raise HTTPException(400, "Something went wrong / Bad Request")


@app.put("/api/account/{id}", response_model=Account)
async def put_account(
    id: str,
    name: str | None = None,
    password: str | None = None,
    email: str | None = None,
):
    response = await update_account(
        id=id,
        name=name,
        password=password,
        email=email
    )
    if response:
        return response
    raise HTTPException(404, f"There is no account with this id.{id}")


@app.delete("/api/account/{id}")
async def delete_account(id: str):
    response = await remove_account(id)
    if response:
        return "Sucessfully deleted account"
    raise HTTPException(404, f"There is no account with this id.{id}")