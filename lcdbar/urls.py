"""
API Routing
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static

from rest_framework import routers
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

from graphene_django.views import GraphQLView

from lcdbar.api import views
from lcdbar.api import schema

ROUTER = routers.DefaultRouter()

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^graphql', GraphQLView.as_view(graphiql=True)),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
