from django.db import models

# Create your models here.


class Album(models.Model):

	album_name = models.CharField(max_length=40)
	artist 	= models.CharField(max_length=40)

	def create(self, validated_data):
		tracks_data = validated_data.pop('tracks')
		album = Album.objects.create(**validated_data)

		for track_data in tracks_data:
			Track.objects.create(album=album, **track_data)

		return album

class Track(models.Model):

	album = models.ForeignKey(Album, on_delete=models.CASCADE)
	order = models.CharField(max_length=40)
	title = models.CharField(max_length=40)
	duration = models.IntegerField()

