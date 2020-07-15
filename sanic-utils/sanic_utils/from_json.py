import functools
from typing import TypeVar, Optional

from sanic.request import Request
from sanic.response import HTTPResponse

T = TypeVar('T')


def from_json(func=None, *, message_type: T):
    def from_json_decorator(func):
        """Extract the json from sanic request to specified type"""

        @functools.wraps(func)
        async def _from_json(*args, **kwargs):
            try:
                request: Request = args[0]
                message: Optional[T] = None
                json = request.json

                if not message_type or not json:
                    message = None
                else:
                    message = message_type.from_dict(request.json)
            except BaseException:
                pass
            response: HTTPResponse = await func(*args, **kwargs, message=message)
            return response

        return _from_json

    if func is None:
        return from_json_decorator
    else:
        return from_json_decorator(func)
