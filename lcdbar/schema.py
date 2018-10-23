import graphene

from graphene.relay import Node

from graphene_django.filter import DjangoFilterConnectionField

from django.contrib.auth import get_user_model

import lcdbar.api.schema

from lcdbar.api import models

class Query(graphene.ObjectType):
    #all_products = graphene.List(lcdbar.api.schema.ProductType)
    all_users = graphene.List(lcdbar.api.schema.UserType)
    all_products = graphene.List(lcdbar.api.schema.ProductType)

    #product = Node.Field(lcdbar.api.schema.ProductType)
    product = graphene.Field(lcdbar.api.schema.ProductType, id=graphene.Int())

    #all_products = DjangoFilterConnectionField(lcdbar.api.schema.ProductType)

  #   query {
  # allProducts(name: "Agua") {
  #     edges {
  #         node {
  #             name
  #         }
  #     }
  # }
  #   }

    # def resolve_all_products(self, info, **kwargs):
    #     print('not using this shit anymore')
    #     return models.Product.objects.all()

    # def resolve_product(self, info, **kwargs):
    #     print('fucking resolving')

    def resolve_all_products(self, info, **kwargs):
        return models.Product.objects.all()

    def resolve_product(self, info, **kwargs):
        id = kwargs.get('id')

        if id is not None:
            return models.Product.objects.get(pk=id)

        return None

    def resolve_all_users(self, info, **kwargs):
        return get_user_model().objects.all()


schema = graphene.Schema(query=Query, mutation=lcdbar.api.schema.Mutations)
