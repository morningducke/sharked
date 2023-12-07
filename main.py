from fastapi import FastAPI, Depends
from core.routers import reports, users
from typing import Annotated

app = FastAPI()
app.include_router(users.router)
app.include_router(reports.router)

# @app.get("/")
# async def root():
#     return {"placeholder"}
