from django.db import models

class Inquiry(models.Model):
    name = models.CharField(max_length=100,default="Anonymous")
    contact = models.CharField(max_length=100,default="Null")
    msg = models.TextField()

    def __str__(self):
        return self.name