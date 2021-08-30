from uuid import UUID
from models.base import AbstractModel


class BookMark(AbstractModel):
    user_id: str  # TODO add validation for UUID
    movie_id: str