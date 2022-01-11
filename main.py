from fastapi import FastAPI
from strawberry.asgi import GraphQL
from schema.schema import schema
from router import auth

app = FastAPI()

app.include_router(auth.router)

graphql_app = GraphQL(schema)
app.add_route("/graphql", graphql_app)
app.add_websocket_route("/graphql", graphql_app)
