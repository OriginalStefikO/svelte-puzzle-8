from fastapi import APIRouter
from fastapi.responses import JSONResponse


dummy_router = APIRouter(prefix="/v1/dummy")


@dummy_router.get("/hello")
async def hello():
    return JSONResponse(content={"message": "Hello, World!"})