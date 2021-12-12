from django.db import models
from rest_framework import serializers
from .models import Car
from django.db.models import fields


class CarSerialzer(serializers.ModelSerializer):
    class Meta:
        fields = ['model', 'description', 'manufacturer', 'author', 'added_on', 'published']
        model = Car