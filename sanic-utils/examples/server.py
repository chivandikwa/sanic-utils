from dataclasses import dataclass

from dataclasses_json import dataclass_json
from sanic import Sanic, response
from sanic.request import Request

from sanic_utils.from_json import from_json


def create_app():
    app = Sanic("App Name")

    @dataclass_json
    @dataclass
    class ExampleInput:
        name: str
        identifier: str

    @app.post("/test")
    @from_json(message_type=ExampleInput)
    async def test(request: Request, message: ExampleInput):
        return response.json(message.__dict__ if message else None)

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=8112)

    return app


create_app()
