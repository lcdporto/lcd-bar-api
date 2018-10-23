import graphene

from django.contrib.auth import get_user_model

from lcdbar.api import schema, models


class Query(graphene.ObjectType):
    all_users = graphene.List(schema.UserType)
    all_products = graphene.List(schema.ProductType)
    product = graphene.Field(schema.ProductType, id=graphene.Int())

    def resolve_all_products(self, info, **kwargs):
        return models.Product.objects.all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.Product.objects.get(pk=id)

        return None

    def resolve_all_users(self, info, **kwargs):
        return get_user_model().objects.all()

schema = graphene.Schema(query=Query, mutation=schema.Mutations)
