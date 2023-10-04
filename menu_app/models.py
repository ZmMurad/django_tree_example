from django.db import models

# Create your models here.
class MenuItem(models.Model):
    '''I wanna use MTPP but in your task said, we should use only django'''
    title = models.CharField(max_length=100)
    url = models.CharField(max_length=100)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='children')

    def __str__(self):
        return self.title