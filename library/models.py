from django.db import models


# Create your models here.
class Publisher(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=200)

class Book(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=300)
    number_of_pages = models.IntegerField()
    publisher = models.ForeignKey(Publisher, null=True, blank=True,
                                  related_name='books', on_delete=models.SET_NULL)  # one to many relations --> one publisher will publish many books


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=300)
    country = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name='authors')


class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    age = models.IntegerField()


class Profile(models.Model):
    id = models.AutoField(primary_key=True)
    address = models.CharField(max_length=200)
    avatarUrl = models.CharField(max_length=400)
    user = models.OneToOneField(User, on_delete=models.CASCADE,
                                   null=True, blank=True)

