
from django.db import models

# Create your models here.

DISTANCIA_CHOICE=(
    ('1milla', '1milla'),
    ('5km', '5km'),
    ('10km', '10km'),
    ('15km', '15km'),
    ('21.096km', '21.096km'),
    ('42.192km', '42.192km')
)
SUPERFICIE_CHOICE=(
    ('Asfalto', 'Asfalto'),
    ('Trail', 'Trail')
)

REGION_CHOICE=(
    ('Cantabria', 'Cantabria'),
    ('Asturias', 'Asturias'),
    ('País Vasco', 'País Vasco')
)


class calendario(models.Model):
    nombre=models.CharField(max_length=100)
    fecha= models.DateField()
    superficie=models.CharField(choices=SUPERFICIE_CHOICE, default='none',max_length=100)
    region=models.CharField(choices=REGION_CHOICE, max_length=100, default='none')
    distancia=models.CharField(choices=DISTANCIA_CHOICE,default='none', max_length=100)
    distancia_real=models.CharField(default='none', max_length=100)
    web=models.URLField(default='none', max_length= 100)
    def __str__(self):
        return self.nombre

        