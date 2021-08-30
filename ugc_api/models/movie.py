from datetime import datetime
from typing import List
from uuid import UUID

from models.base import AbstractModel


class Movie(AbstractModel):
    rating: int
    scores: List[UUID]
    scores_quality: int
    reviews: List[UUID]