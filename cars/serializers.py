from rest_framework import serializers
from cars.models import Car, CarMaker, CarModel

class CarMakerSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarMaker
        fields = ('id', 'name', 'country')

class CarModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarModel
        fields = ('id', 'name', 'carmaker')

class CarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'carmodel', 'year', 'owners', 'pub_date')