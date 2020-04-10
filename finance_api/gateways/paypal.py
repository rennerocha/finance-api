import requests
from fastapi import APIRouter, Request, Response

router = APIRouter()


@router.get("/gateway/paypal")
async def paypal(request: Request):
    return {"gateway": "paypal"}


@router.get("/chuck/norris")
async def chuck_norris(request: Request):
    response = requests.get("https://api.chucknorris.io/jokes/random")
    return response.json()