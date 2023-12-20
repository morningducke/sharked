from datetime import timedelta
from enum import StrEnum
from typing import Annotated
from fastapi import Query
from pydantic import BaseModel

class ChessWebsites(StrEnum):
    LICHESS = "lichess"
    CHESSCOM = "chesscom"

class BaseReport(BaseModel):
    suspect_username: str
    made_by: str
    verdict: bool

class ExtendedReport(BaseReport):
    website: ChessWebsites
    total_games: int | None = None
    winrate: float | None = None
    account_age: timedelta | None = None
    

# type aliases
SuspectUsername = Annotated[str, Query(title="Suspect's username")]