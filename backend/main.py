from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from core.routers import users_router
from core.routers import reports_router

app = FastAPI()
app.include_router(users_router.router)
app.include_router(reports_router.router)

# TODO: Move it somewhere appropriately
origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
