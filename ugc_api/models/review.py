from datetime import datetime
from typing import List

from models.base import AbstractModel
from pydantic import Field


class Review(AbstractModel):
    user_id: str  # TODO add validation for UUID
    movie_id: str
    pub_date: datetime
    text: str = Field(max_length=1000)
    movie_score_id: str
    rating: int
    scores: List[str]
    scores_quality: int
