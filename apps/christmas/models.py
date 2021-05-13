from django.db import models

class Letter(models.Model):
    '''Letter Model'''
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now=True)
    updated_at = models.DateField(auto_now_add=True)
    title = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return f'{ self.title } - { self.name }'