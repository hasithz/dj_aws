from django.db import models
from dataclasses import dataclass

@dataclass
class StoreTypes:
    COMPUTER = "Com"
    MOBILE = "Mob"
    GROCESSORY = "Grs"
    TEXTILE = "Tex"
    FOOD = "Fod"
    OTHER = "Oth"
    NONE = "Non"

    store_types = [
        (COMPUTER, 'Computer'),
        (MOBILE, 'Mobile'),
        (GROCESSORY, 'Grocessory'),
        (TEXTILE, 'Textile'),
        (FOOD, 'Food'),
        (OTHER, 'Other'),
    ]

# Create your models here.
class Store(models.Model):
    id   = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    lat  = models.FloatField()
    lon  = models.FloatField()
    

class StoreItems(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE,)
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    discription = models.TextField()
    discount = models.FloatField()
    price = models.FloatField()
    No_of_items = models.IntegerField()
    
    uploadpath = 'storeItems/'
    item_image = models.ImageField(blank=True, upload_to=uploadpath)
    
    def __str__(self):
        return self.name