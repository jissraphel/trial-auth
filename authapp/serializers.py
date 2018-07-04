from .models import Album, Track
from rest_framework import serializers
class TrackSerializer(serializers.ModelSerializer):
    class Meta:
        model = Track
        fields = ('order', 'title', 'duration')

class AlbumSerializer(serializers.ModelSerializer):
    track_set = TrackSerializer(many=True, read_only=False)

    class Meta:
        model = Album
        fields = ('album_name', 'artist', 'track_set')