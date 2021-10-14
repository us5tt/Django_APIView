from django.db import models


class Pars(models.Model):
    title = models.CharField(max_length=100)
    usd_price = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    description = models.CharField(max_length=100)
    #    public = models.DateTimeField

    def __str__(self):
        return self.title

