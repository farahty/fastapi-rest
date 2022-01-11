import strawberry as gql


@gql.type
class AuthQuery:
    @gql.field
    def login() -> bool:
        return True
