from typing import List
import strawberry as gql

from schema.base import Base


@gql.type
class User(Base):
    name: str
    age: int


@gql.type
class UserQuery:
    @gql.field
    def user(self) -> List[User]:
        return [User(name="Nimer", age=20), User(name="Kareem", age=6)]
