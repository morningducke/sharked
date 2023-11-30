from random import random
from uuid import uuid4
from core.controllers.games import get_user_games_chesscom, get_user_games_lichess
from core.schemas.report_schemas import ChessWebsites, ExtendedReport
from core.models.database import db_reports
from core.schemas.user_schemas import UsernameAnnotated


def is_user_cheating(games) -> bool:
    return random() > 0.5

def generate_report(username: str, website: ChessWebsites, made_by: str):
    """generate an extended report on a user"""
    games = None
    if website == ChessWebsites.LICHESS:
        games = get_user_games_lichess(username)
    elif website == ChessWebsites.CHESSCOM:
        games = get_user_games_chesscom(username)
        
    verdict = is_user_cheating(games)
    report = ExtendedReport(website=website, suspect_username=username, verdict=verdict, made_by=made_by)
    db_reports[uuid4()] = report
    return report

def get_users_reports(username: UsernameAnnotated) -> list:
    """get reports made by a user"""
    return [(id, report) for id, report in db_reports.items() if report.made_by == username]
    