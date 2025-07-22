from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"

class Race(models.Model):
    title = models.CharField(max_length=250)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    longitude = models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True)
    latitude = models.DecimalField(max_digits=6, decimal_places=2,blank=True,null=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}-{self.category}"