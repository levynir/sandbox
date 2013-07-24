from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from cars import views

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'cars', views.CarViewSet)
router.register(r'carmodels', views.CarModelViewSet)
router.register(r'carmakers', views.CarMakerViewSet)

urlpatterns = patterns('snippets.views',
    url(r'^', include(router.urls)),
)