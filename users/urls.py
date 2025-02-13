from django.urls import path, include
from rest_framework import routers
from users import views

router = routers.DefaultRouter()
router.register(r'users', views.UsersViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
