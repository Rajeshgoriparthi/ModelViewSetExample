from django.db import models

# Create your models here.

class Product_catagiry(models.Model):
    pcid=models.IntegerField()
    pcname=models.CharField(max_length=20)

    def __str__(self):
        return self.pcname




class Products(models.Model):
    pcname=models.ForeignKey(Product_catagiry,on_delete=models.CASCADE)
    pid=models.IntegerField()
    pname=models.CharField(max_length=30)
    price=models.DecimalField(max_digits=8,decimal_places=2)
    date=models.DateField()

    def __str__(self):
        return self.pname