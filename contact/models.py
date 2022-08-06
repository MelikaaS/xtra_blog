from django.db import models

class Message(models.Model):
    name = models.CharField(max_length=20)
    email = models.CharField(max_length=30)
    subject = models.CharField(max_length=20)
    text = models.CharField(max_length=200)



    def __str__(self):
        return self.subject



# Create your models here.
