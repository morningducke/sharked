from typing import Annotated
from fastapi import APIRouter, Depends
from core.models.database import get_db
from config import API_PREFIX
from core.controllers.reports_controller import generate_report, get_users_reports
from core.controllers.users_controller import get_current_active_user
from core.schemas.report_schemas import BaseReport, ChessWebsites, ExtendedReport, SuspectUsername
from core.schemas.user_schemas import BaseUser
from motor.motor_asyncio import AsyncIOMotorDatabase

router = APIRouter(
    prefix="".join([API_PREFIX, "/reports"]),
    tags=["reports"]
)

@router.post("/lichess")
async def generate_report_lichess(username: SuspectUsername, 
                                  current_user: Annotated[BaseUser, Depends(get_current_active_user)],
                                  db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> ExtendedReport:
    return await generate_report(username=username, website=ChessWebsites.LICHESS, made_by=current_user.username, db=db)

@router.post("/chesscom")
async def generate_report_chesscom(username: SuspectUsername, 
                                   current_user: Annotated[BaseUser, Depends(get_current_active_user)],
                                   db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> ExtendedReport:
    return await generate_report(username=username, website=ChessWebsites.CHESSCOM, made_by=current_user.username, db=db)

@router.get("/me", description="Get reports made by the current user")
async def get_current_user_reports(current_user: Annotated[BaseUser, Depends(get_current_active_user)],
                                   db: Annotated[AsyncIOMotorDatabase, Depends(get_db)]) -> list[ExtendedReport]:
    return await get_users_reports(current_user.username, db=db)





