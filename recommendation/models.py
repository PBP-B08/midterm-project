from django.db import models

# Create your models here.


class Province(models.Model):
    """Model representing a province."""
    title = models.CharField(max_length=100)
    header = models.CharField(max_length=100)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief summary of the province')
    image = models.URLField(max_length=512, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title


class Area(models.Model):
    """Model representing an area."""
    title = models.CharField(max_length=100)
    province = models.ForeignKey(
        'Province', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(
        max_length=1000, help_text='Enter a brief description of the area')
    description = models.TextField(
        max_length=1000, help_text='Enter a brief description of the area')
    image = models.URLField(max_length=512, null=True, blank=True)

    def __str__(self):
        """String for representing the Model object."""
        return self.title
