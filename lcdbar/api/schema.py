import graphene

from django.contrib.auth import get_user_model

from graphene_django.types import DjangoObjectType

from lcdbar.api import models

class PaymentType(DjangoObjectType):
    class Meta:
        model = models.Payment

class ProductType(DjangoObjectType):
    class Meta:
        model = models.Product

class UserType(DjangoObjectType):
    class Meta:
        model = get_user_model()

class CreatePayment(graphene.Mutation):
    class Arguments:
        barcode = graphene.Int()
        pin = graphene.Int()

    # output fields
    payment = graphene.Field(lambda: PaymentType)

    def mutate(self, info, barcode, pin):
        payment = models.Payment.objects.create(barcode=barcode, pin=pin)
        return CreatePayment(payment=payment)

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
    create_payment = CreatePayment.Field()
