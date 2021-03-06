from django.urls import path, include
from django.views.generic import TemplateView
from rest_framework import routers
from tickets import endpoints

router = routers.DefaultRouter()
router.register(r'movies', endpoints.MovieViewSet, basename='movies')
router.register(r'rooms', endpoints.ShowingRoomViewSet, basename='rooms')
router.register(r'showings', endpoints.ShowingViewSet, basename='showings')
router.register(r'order', endpoints.OrderViewSet, basename='order')

urlpatterns = [
    path('', TemplateView.as_view(template_name='tickets/home.html'), name='home'),
    path('api/', include(router.urls)),

]