from typing import Annotated
from fastapi import APIRouter, Depends
from core.controllers.reports import generate_report, get_users_reports
from core.controllers.users import get_current_active_user
from core.schemas.report_schemas import BaseReport, ChessWebsites, SuspectUsername
from core.schemas.user_schemas import BaseUser

router = APIRouter(
    prefix="/reports",
    tags=["reports"]
)

@router.post("/lichess")
async def analyze_user_lichess(username: SuspectUsername, current_user: Annotated[BaseUser, Depends(get_current_active_user)]) -> BaseReport:
    return await generate_report(username=username, website=ChessWebsites.LICHESS, made_by=current_user.username)

@router.post("/chesscom")
async def analyze_user_chesscom(username: SuspectUsername, current_user: Annotated[BaseUser, Depends(get_current_active_user)]) -> BaseReport:
    return await generate_report(username=username, website=ChessWebsites.CHESSCOM, made_by=current_user.username)

@router.get("/me")
async def get_current_user_reports(current_user: Annotated[BaseUser, Depends(get_current_active_user)]):
    return await get_users_reports(current_user.username)





