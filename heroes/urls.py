from django.urls import path, include
from rest_framework import routers
from heroes import views




router = routers.DefaultRouter()
router.register(r'heroes', views.HeroViewSet)


urlpatterns = [
    path('', include(router.urls))
]
