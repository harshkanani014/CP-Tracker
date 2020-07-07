from rest_framework import serializers
from .models import postcard


class postcardSerializer(serializers.ModelSerializer):
    class Meta:
        model = postcard
        fields = ('id', 'heading', 'image', 'alt', 'text', 'created_at')
