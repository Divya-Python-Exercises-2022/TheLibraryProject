"""the_library_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from library.views import BookViewSet, PublisherViewSet, ProfileViewSet, UserViewSet, AuthorViewSet, BookApiView

router = DefaultRouter()
router.register(r'books', BookViewSet)
router.register(r'publisher', PublisherViewSet)
router.register(r'user', UserViewSet)
router.register(r'profile', ProfileViewSet)
router.register(r'author', AuthorViewSet)

urlpatterns = [
    path('books2', BookApiView.as_view()), # View is added directly in the URL patterns without registering in the router
    path('', include(router.urls)),
    path('admin/', admin.site.urls),
]
