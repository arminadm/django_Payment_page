from django.db import models

# Create your models here.
class Customers(models.Model):
    name = models.CharField(null=False, blank=False, max_length=50)
    lastname = models.CharField(null=False, blank=False, max_length=50)
    address = models.TextField(null=False, blank=False,)
    phone = models.IntegerField(null=False, blank=False, unique=True)
    email = models.EmailField(null=False, blank=False, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    payment = models.BooleanField(default=False)
    class Meta:
        verbose_name = ("Customer")
        verbose_name_plural = ("Customers")
        ordering = ['-created_date']
    def __str__(self):
        return self.email