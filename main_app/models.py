from django.db import models

# Create your models here.
class Currency(models.Model):

    name = models.CharField(max_length=100)
    image = models.CharField(max_length=500)
    country = models.TextField(max_length=50)
    
    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Money(models.Model):

    type = models.CharField(max_length=150)
    currency = models.ForeignKey(Currency, on_delete=models.CASCADE, related_name="money")

    def __str__(self):
        return self.type