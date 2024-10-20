from django.db import models

class AdminInquiry(models.Model):
    name = models.CharField(max_length=100,default="Anonymous")
    contact = models.CharField(max_length=100,default="Null")
    msg = models.TextField()
    dt = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return self.name

class IPInfo(models.Model):
    ip_address = models.CharField(max_length=45)  # Supports both IPv4 and IPv6
    city = models.CharField(max_length=100, null=True, blank=True)
    region = models.CharField(max_length=100, null=True, blank=True)
    country = models.CharField(max_length=50, null=True, blank=True)
    org = models.CharField(max_length=255, null=True, blank=True)
    page = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.ip_address

class Product(models.Model):
    pid = models.CharField(max_length=255,primary_key=True)
    amount = models.CharField(max_length=100,default="100")
    val_id = models.CharField(max_length=100,default="test")
    tran_id = models.CharField(max_length=100,default="test")
    sessionkey = models.CharField(max_length=100,default="test")
    paid_status = models.BooleanField(default=False)
    paid_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.pid

class Earning(models.Model):
    name = models.CharField(max_length=100,primary_key=True)
    total_amount = models.DecimalField(max_digits=12, decimal_places=2, default=0.00)

    def __str__(self):
        return f"{self.name} - {self.total_amount}"