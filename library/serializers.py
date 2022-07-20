from rest_framework import serializers
from rest_framework.serializers import HyperlinkedModelSerializer

from library.models import Book, Publisher, Profile, User, Author

class AuthorSerializer(HyperlinkedModelSerializer):

    books = serializers.HyperlinkedRelatedField(
        queryset=Book.objects.all(), many=True,
        view_name='book-detail')

    class Meta:
        model = Author
        fields = ['url', 'name', 'country', 'books']



class BookSerializer(HyperlinkedModelSerializer):
    authors = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(), many=True,
        view_name='author-detail')
    publisher = serializers.HyperlinkedRelatedField(
        queryset=Publisher.objects.all(),
        view_name='publisher-detail')

    class Meta:
        model = Book
        fields = ['url', 'id', 'title', 'number_of_pages', 'publisher', 'authors']


class PublisherSerializer(HyperlinkedModelSerializer):

    books = serializers.HyperlinkedRelatedField(
        queryset=Book.objects.all(),
        many=True,
        view_name='book-detail')

    class Meta:
        model = Publisher
        fields = ['url', 'id', 'name', 'country', 'books']

class ProfileSerializer(HyperlinkedModelSerializer):

    user = serializers.HyperlinkedRelatedField(
        queryset=User.objects.all(),
        many=False,
        view_name='user-detail')

    class Meta:
        model = Profile
        fields = ['url', 'address', 'avatarUrl', 'user']

class UserSerializer(HyperlinkedModelSerializer):

    profile = serializers.HyperlinkedRelatedField(
        queryset=Profile.objects.all(), required=False,
        many=False,
        view_name='profile-detail')

    class Meta:
        model = User
        fields = ['url', 'id', 'name', 'age', 'url', 'profile']