from django.db import models

class AdminInquiry(models.Model):
    name = models.CharField(max_length=100,default="Anonymous")
    contact = models.CharField(max_length=100,default="Null")
    msg = models.TextField()
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name