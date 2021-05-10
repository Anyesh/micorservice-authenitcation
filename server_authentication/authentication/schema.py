import graphene
import graphql_jwt
import main.schema

import authentication.core.schema


class Query(
    authentication.core.schema.Query, main.schema.Query, graphene.ObjectType
):
    pass


class Mutation(
    authentication.core.schema.Mutation,
    main.schema.Mutation,
    graphene.ObjectType,
):
    token_auth = graphql_jwt.ObtainJSONWebToken.Field()
    verify_token = graphql_jwt.Verify.Field()
    refresh_token = graphql_jwt.Refresh.Field()


schema = graphene.Schema(query=Query, mutation=Mutation)
