from django.db import models

class Emp(models.Model):
    name = models.CharField( max_length=50)
    sal = models.CharField(max_length=50)
    address = models.TextField()
    def __str__(self) -> str:
        return self.name