from django.shortcuts import render
from rest_framework import viewsets

# Create your views here.

from .serializer import PostsSerializer
from .models import PostsModel


class PostsViewSet(viewsets.ModelViewSet):
    queryset = PostsModel.objects.all()
    serializer_class = PostsSerializer
