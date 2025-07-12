
from .models import *
from rest_framework import serializers

class Blogserializer(serializers.ModelSerializer):
    class Meta():
        model=Blog
        exclude=['created_at', 'updated_at']
