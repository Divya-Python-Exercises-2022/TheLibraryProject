from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Publisher, Profile, User, Author
from library.serializers import BookSerializer, PublisherSerializer, ProfileSerializer, UserSerializer, AuthorSerializer


class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer