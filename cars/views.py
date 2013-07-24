# Create your views here.
from rest_framework import viewsets
from cars.models import CarMaker, CarModel, Car
from cars.serializers import CarSerializer, CarModelSerializer, CarMakerSerializer

class CarViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = Car.objects.all()
    serializer_class = CarSerializer

class CarModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer

class CarMakerViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = CarMaker.objects.all()
    serializer_class = CarMakerSerializer