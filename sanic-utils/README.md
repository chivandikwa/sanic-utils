# sanic-utils

A suite of useful Sanic utilities

## from_json

A decorator for Sanic endpoints to grab the json from the request and pass it in as a parameter. 
Default Sanic approach:


```python
from sanic import Sanic, response
from sanic.request import Request

app = Sanic("App Name")

class ExampleInput:
    name: str
    identifier: str

@app.post("/test")
async def test(request: Request):
    json = request.json
    message = None # convert json to object in whatever prefered way
    return response.text("done")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8112)
```

Usage of the decorator:

```python
from dataclasses import dataclass

from dataclasses_json import dataclass_json
from sanic import Sanic, response
from sanic.request import Request

from sanic_utils.from_json import from_json

app = Sanic("App Name")

@dataclass_json
@dataclass
class ExampleInput:
    name: str
    identifier: str

@app.post("/test")
@from_json(message_type=ExampleInput)
async def test(request: Request, message: ExampleInput):
    print(message)
    return response.text("done")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8112)
```

###  Usage

Mark endpoint method with @from_json decorator passing in a single param, the resulting message type.
The message type should be marked with @dataclass_json and @dataclass.

## Dependencies

sanic 20.6.3

dataclasses 0.6

dataclasses-json 0.5.1

# [CONTRIBUTING](CONTRIBUTING.md)

# [LICENSE](LICENSE)
