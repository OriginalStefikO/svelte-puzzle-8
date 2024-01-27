import uvicorn
import logging
import sys

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.mount("/assets", StaticFiles(directory="public/assets"), name="static")

@app.get("/favicon.png", response_class=FileResponse)
async def favicon_png():
    return FileResponse("public/favicon.png")

@app.get("/favicon.ico", response_class=FileResponse)
async def favicon_ico():
    return FileResponse("public/favicon.png")


app.mount('/', StaticFiles(directory='public', html=True))

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    return FileResponse("public/200.html")

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ["dev", "--dev", "-d", "development"]:
            uvicorn.run("backend.main:app", port=8080, log_level="debug", reload=True)
    else:
        uvicorn.run("backend.main:app", host="0.0.0.0", port=8080, log_level="info", reload=False)