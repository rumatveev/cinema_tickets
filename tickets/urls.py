from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from tickets import endpoints


router = routers.DefaultRouter()
router.register(r'movies', endpoints.MovieViewSet)

urlpatterns = [
    path('', TemplateView.as_view(template_name='tickets/home.html'), name='home'),
    path('api/', include(router.urls)),



]