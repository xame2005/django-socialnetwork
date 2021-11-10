from graphene_django.views import GraphQLView
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('socialnet/', include('posts.urls')),
    path('admin/', admin.site.urls),
    path(r'graphql/', csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
