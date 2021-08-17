"""
Auth integration
"""
import uuid

import aiohttp
import backoff
from aiohttp import ClientConnectionError

from core.config import AUTH_BACKOFF_TIME, AUTH_URL, BACKOFF_FACTOR
from models.user import User


class AuthServiceUnavailable(BaseException):
    ...


class UserNotFound(BaseException):
    ...


def giveup_handler(details):
    raise AuthServiceUnavailable


@backoff.on_exception(backoff.expo,
                      ClientConnectionError,
                      max_time=AUTH_BACKOFF_TIME,
                      factor=BACKOFF_FACTOR,
                      on_giveup=giveup_handler)
async def get_user_info(token: str) -> User:
    async with aiohttp.ClientSession() as session:

        headers = {
            "Authorization": token,
            "X-Request-Id": str(uuid.uuid4()),
        }

        async with session.get(AUTH_URL, headers=headers) as response:
            if response.status == 200:
                return User(**await response.json())
            elif response.status == 404:
                raise UserNotFound
            else:
                raise AuthServiceUnavailable
