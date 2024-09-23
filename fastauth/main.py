from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from fastauth.common.exception import FastAuthError
from fastauth.database.engine import create_db_and_tables, get_engine

app = FastAPI()


create_db_and_tables(engine=get_engine())


@app.exception_handler(FastAuthError)
def fastauth_exception_handler(request: Request, exc: FastAuthError):
    return JSONResponse(status_code=exc.status_code, content={"detail": exc.message})


@app.get("/")
async def root():
    return {"message": "Hello World"}
