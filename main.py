from typing import Optional
from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema import schema


app = FastAPI()

graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)


@app.get("/")
def index():
    return {"message": "hello world, tigers team"}


@app.get("/option/")
def optional(option: Optional[str] = None):
    return {"option": option}


@app.get("/post/{post_id}")
def one(post_id: int):
    return {"post_id": post_id}
