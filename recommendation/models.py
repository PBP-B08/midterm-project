from django.db import models

# Create your models here.


class Recommendation(models.Model):
    """Model representing a recommendation."""
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='recommendation_images', blank=True)
    description = models.TextField(
        max_length=1000, help_text='Enter a brief description of the recommendation')
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief summary of the recommendation')


class Province(models.Model):
    """Model representing a province."""
    name = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief summary of the province')

    def __str__(self):
        """String for representing the Model object."""
        return self.name


class Area(models.Model):
    """Model representing an area."""
    name = models.CharField(max_length=100)
    province = models.ForeignKey(
        'Province', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the area')
    description = models.TextField(
        max_length=1000, help_text='Enter a brief description of the area')

    def __str__(self):
        """String for representing the Model object."""
        return self.name
