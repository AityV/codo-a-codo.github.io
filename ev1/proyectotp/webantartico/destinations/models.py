from django.db import models

# Create your models here.
class Flip_card(models.Model):
    image_front = models.ImageField(verbose_name='Imagen frente', upload_to='destinations_media')
    title_front = models.CharField(max_length=100, verbose_name='Título frente')
    
    title_back = models.CharField(max_length=100, verbose_name='Título posterior')
    description_back = models.TextField(verbose_name='Descripción posterior')
    link_back = models.URLField(verbose_name='Enlace')
    
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    updated = models.DateTimeField(auto_now=True, verbose_name='Fecha de modificación')
    
    
    def __str__(self) -> str:
        return self.title_front
    
        
    class Meta:
        verbose_name = 'Tarjeta giratoria'
        verbose_name_plural = 'Tarjetas giratorias'
        ordering = ['created']
        
    
    