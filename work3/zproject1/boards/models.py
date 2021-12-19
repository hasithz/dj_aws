from django.db import models
from dataclasses import dataclass

@dataclass
class AdvTypes:
    COMPUTER = "Com"
    MOBILE = "Mob"
    GROCESSORY = "Grs"
    TEXTILE = "Tex"
    FOOD = "Fod"
    OTHER = "Oth"
    NONE = "Non"

    adv_types = [
        (COMPUTER, 'Computer'),
        (MOBILE, 'Mobile'),
        (GROCESSORY, 'Grocessory'),
        (TEXTILE, 'Textile'),
        (FOOD, 'Food'),
        (OTHER, 'Other'),
    ]
# Create your models here.
class Boards(models.Model):
    lon = models.FloatField()
    lat = models.FloatField()
    
class Advetiesments(models.Model):
    name = models.CharField(max_length=255)
    adv_type = models.CharField(max_length=3,
                        choices=AdvTypes.adv_types, 
                        default=AdvTypes.NONE)
    
    uploadpath = 'advertiesments/'
    image = models.ImageField(blank=True, upload_to=uploadpath)
    
    # def __str__(self):
    #     opt_name = self.name+" " +str(self.id)
    #     return opt_name