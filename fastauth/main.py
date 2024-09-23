from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastauth.common.exception import FastAuthError

app = FastAPI()


@app.exception_handler(FastAuthError)
def fastauth_exception_handler(request: Request, exc: FastAuthError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/")
async def root():
    return {"message": "Hello World"}
