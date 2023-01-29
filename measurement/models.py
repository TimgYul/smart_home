from django.db import models

class Sensor(models.Model):
    name = models.CharField(max_length=256, verbose_name='Датчик')
    description = models.CharField(max_length=256, verbose_name='Описание') 
    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Датчик'
        verbose_name_plural = 'Датчики'

class Measurement(models.Model):
    
    sensors = models.ForeignKey(Sensor, on_delete = models.CASCADE, related_name='measurements')
    temperature = models.FloatField()    
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
   
    
    
