from django.urls import path
from graphene_django.views import GraphQLView
from .schema import schema
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView
from django.conf.urls import url



urlpatterns = [
    # path("graphql",  csrf_exempt(GraphQLView.as_view(graphiql= True, schema= schema)))
    path('graphql', csrf_exempt(FileUploadGraphQLView.as_view(graphiql=True, schema= schema))),
]