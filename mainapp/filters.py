from django.forms import widgets
from .models import calendario
import django_filters
from .models import *
from django_filters import CharFilter

class FiltroPrueba(django_filters.FilterSet):
    nombre = CharFilter(field_name='nombre', lookup_expr='contains', label='Nombre')
    fecha_inicio = django_filters.DateFilter(field_name='fecha', lookup_expr='gte', label='inicio', 
        widget= widgets.DateInput( 
            attrs={'class': 'datepicker'}))
        
    fecha_fin = django_filters.DateFilter(field_name='fecha', lookup_expr='lte', label='fin',
    widget= widgets.DateInput( 
            attrs={'class': 'datepicker'}
        ))
        
    class Meta():
        model = calendario
        fields = '__all__' 
        exclude = ['fecha', 'web','distancia_real']
                
    
        
