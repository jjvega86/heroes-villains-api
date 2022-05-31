from rest_framework import serializers
from .models import Super, Power


class PowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Power
        fields = ['id', 'name']


class SuperSerializer(serializers.ModelSerializer):
    powers = PowerSerializer(many=True)

    class Meta:
        model = Super
        fields = ['id', 'name', 'alter_ego', 'powers',
                  'catchphrase', 'super_type']
        depth = 1
