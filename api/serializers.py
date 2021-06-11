from rest_framework import serializers
from .models import *
class urlshorserializer(serializers.ModelSerializer):
    class Meta:
        model=urlshort
        fields=['url','slug']