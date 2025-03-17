from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UserViewSet, RegisterUserView
from django.views.decorators.csrf import csrf_exempt

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('register', RegisterUserView, basename='register')

urlpatterns = [
    path('', include(router.urls)),
    path('get', UserViewSet.as_view({'get': 'me'}), name='me'),
    path('register/', csrf_exempt(RegisterUserView.as_view({'post': 'register'})))
]