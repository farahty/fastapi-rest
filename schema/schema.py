from fastapi.params import Query
import strawberry as gql
from strawberry.tools import merge_types

from schema.user import UserQuery
from schema.auth import AuthQuery

Query = merge_types("Query", (UserQuery, AuthQuery))

schema = gql.Schema(query=Query)
