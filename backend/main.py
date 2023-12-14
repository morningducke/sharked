from fastapi import FastAPI
from core.routers import reports, users

app = FastAPI()
app.include_router(users.router)
app.include_router(reports.router)
