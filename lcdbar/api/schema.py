import graphene

from django.contrib.auth import get_user_model

from graphene_django.types import DjangoObjectType

from lcdbar.api import models

class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        quantity = graphene.Int()

    ok = graphene.Boolean()
    product = graphene.Field(lambda: ProductType)

    def mutate(self, info, name, quantity, avatar):
        product = models.Product.objects.create(name=name, quantity=quantity)
        ok = True
        return CreateProduct(product=product, ok=ok)

class Mutations(graphene.ObjectType):
    create_product = CreateProduct.Field()
