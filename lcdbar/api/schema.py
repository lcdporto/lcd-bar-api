import graphene

from graphene.relay import Node

from graphene_django.filter import DjangoFilterConnectionField

from django.contrib.auth import get_user_model

from graphene_django.types import DjangoObjectType

from graphene_file_upload.scalars import Upload

from lcdbar.api import models

class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product
        #filter_fields = ['name']
        # filter_fields = {
        #     'name': ['exact', 'icontains', 'istartswith'],
        #     'quantity': ['exact']
        # }
        # interfaces = (Node, )

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()


# mutations

class CreateProduct(graphene.Mutation):
    class Arguments:
        name = graphene.String()
        quantity = graphene.Int()
        avatar = Upload(required=True)

    # output fields, after resolving
    ok = graphene.Boolean()
    product = graphene.Field(lambda: ProductType)

    def mutate(self, info, name, quantity, avatar):
        print('params', name, quantity)
        product = models.Product.objects.create(name=name, quantity=quantity)
        print('the create product', product)
        ok = True
        return CreateProduct(product=product, ok=ok)
        #return CreateProduct(ok=ok)

class Mutations(graphene.ObjectType):
    create_product = CreateProduct.Field()


# optei por não usar a mixin para já, para simplificar o código

# class Query(object):
#     all_products = graphene.List(ProductType)

#     def resolve_all_products(self, info, **kwargs):
#         return models.Product.objects.all()
