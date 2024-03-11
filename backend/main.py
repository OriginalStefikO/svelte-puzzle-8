import uvicorn
import logging
import sys

from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import FileResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

from backend.routers import dummy_api_router
from backend.utils.settings import DEVELOPMENT


app = FastAPI()

if DEVELOPMENT == "true":
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(dummy_api_router.dummy_router)

@app.exception_handler(404)
async def not_found_exception_handler(request: Request, exc: HTTPException):
    if request.url.path.startswith("/v1/"):
        error_message = {"error": "Not Found", "detail": "Endpoint not found"}
        logging.error(f"404 Not Found: {request.url}")
        return JSONResponse(content=error_message, status_code=404)
    else:
        return FileResponse("public/200.html")

app.mount('/', StaticFiles(directory='public', html=True))

if __name__ == '__main__':
    logging.basicConfig(format='%(asctime)s %(levelname)s %(message)s', level=logging.INFO)
    
    if len(sys.argv) > 1:
        if sys.argv[1] in ["dev", "--dev", "-d", "development"]:
            uvicorn.run("backend.main:app", port=8080, log_level="debug", reload=True)
    else:
        uvicorn.run("backend.main:app", host="0.0.0.0", port=8080, log_level="info", reload=False)