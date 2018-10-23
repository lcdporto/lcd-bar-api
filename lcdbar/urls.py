"""
API Routing
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from graphene_django.views import GraphQLView

from graphene_file_upload.django import FileUploadGraphQLView


from lcdbar.api import views
from lcdbar.api import schema

ROUTER = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # https://github.com/graphql-python/graphene-django/issues/61
    # https://github.com/graphql-python/graphene-django/issues/170
    url(r'^graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True))),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
