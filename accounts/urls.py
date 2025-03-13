from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserView

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('register', RegisterUserView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
]