import graphene

import lcdbar.api.schema

class Query(lcdbar.api.schema.Query, graphene.ObjectType):
    pass

schema = graphene.Schema(query=Query)
