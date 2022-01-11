from typing import List
import strawberry as gql


@gql.type
class User:
    name: str
    age: int


@gql.type
class Query:
    @gql.field
    def user(self) -> List[User]:
        return [User(name="Nimer", age=20), User(name="Kareem", age=6)]


schema = gql.Schema(query=Query)
