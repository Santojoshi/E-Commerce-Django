from django.db import models


class cont(models.Model):
    name = models.CharField(max_length=50, blank=False )
    email = models.EmailField()
    phone = models.IntegerField(max_length=10)
    comment = models.TextField(max_length=500, blank=False)

def __str__(self):
    return self.name

