from django.shortcuts import render
from rest_framework import permissions
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet

from lcdbar.api import models, serializers

# Create your views here.
