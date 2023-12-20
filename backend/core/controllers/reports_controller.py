from random import random, randint
from config import REPORTS_COLLECTION
from core.controllers.games_controller import get_user_games_chesscom, get_user_games_lichess
from core.schemas.report_schemas import ChessWebsites, ExtendedReport
from core.schemas.user_schemas import UsernameAnnotated
from motor.motor_asyncio import AsyncIOMotorDatabase


async def is_user_cheating(games) -> bool:
    return random() > 0.5

async def generate_report(username: str, website: ChessWebsites, made_by: str, db: AsyncIOMotorDatabase):
    """generate an extended report on a user"""
    games = None
    if website == ChessWebsites.LICHESS:
        games = await get_user_games_lichess(username)
    elif website == ChessWebsites.CHESSCOM:
        games = await get_user_games_chesscom(username)
        
    verdict = await is_user_cheating(games)
    report = ExtendedReport(website=website, suspect_username=username, verdict=verdict, made_by=made_by, total_games=randint(1, 100), winrate=random() * 100)
    await db[REPORTS_COLLECTION].insert_one(dict(report))
    return report

async def get_users_reports(username: UsernameAnnotated, db: AsyncIOMotorDatabase, limit: int = 10) -> list[ExtendedReport]:
    """get reports made by a user"""
    reports_cursor = db[REPORTS_COLLECTION].find({"made_by": username})
    return [report for report in await reports_cursor.to_list(limit)]
    