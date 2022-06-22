from django.urls import path, include
from .views import AuthorViewSet, BookViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('author', AuthorViewSet)
router.register('books', BookViewSet)

urlpatterns = [
    path('api/v1/', include(router.urls))
]
