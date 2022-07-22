from django.shortcuts import render
import logging # to record some event in the system , logging is imported


# Create your views here.
from rest_framework import status, filters
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from library.models import Book, Publisher, Profile, User, Author
from library.serializers import BookSerializer, PublisherSerializer, ProfileSerializer, UserSerializer, AuthorSerializer


logger = logging.getLogger(__name__)

# modelViewSet --> link DB and views Automatically
class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.all()
    serializer_class = PublisherSerializer


class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'books__title']


class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    # Overwrite the queryset method

    def get_queryset(self):
        search_term = self.request.query_params.get('search_terms')
        if search_term:
            queryset = Book.objects.filter(title__contains=search_term)
        else:
            queryset = Book.objects.all()

        return queryset

class ProfileViewSet(ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# It is an HTTP API --> requires post and get methods to be defined
# when Django calls route with POST method, post method in APIView is executed
class BookApiView(APIView):

    def post(self, request: Request):
        #logger.info(request.data)

        # create a serializer
        serializer = BookSerializer(data=request.data) # set data to that we are receiving
        if serializer.is_valid():
            return Response(data=request.data)
        else:
            return Response(data=serializer.errors, status=status.HTTP_422_UNPROCESSABLE_ENTITY)

    def get(self, request: Request):
        #logger.info('Get Received...')

        return Response({'message':'Hi from books2'}, status=status.HTTP_200_OK)
