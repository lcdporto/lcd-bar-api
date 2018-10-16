import graphene

from graphene_django.types import DjangoObjectType

from lcdbar.api import models

class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product

class Query(object):
    all_products = graphene.List(ProductType)

    def resolve_all_products(self, info, **kwargs):
        return models.Product.objects.all()
