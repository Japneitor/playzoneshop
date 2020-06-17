from django.db import models

# Create your models here.
categoria = (
    ('Juegos de accion', 'Juegos de accion'),
    ('Juegos de simulacion', 'Juegos de simulacion'),
    ('Juegos de deportes', 'Juegos de deportes'),
    ('Juegos de aventura', 'Juegos de aventura'),
    ('Juegos de plataformas', 'Juegos de plataformas'),
    ('Juegos de puzzle', 'Juegos de puzzle'),
)
class Juego(models.Model):
    nombre = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='home/', null=True)
    descripcion = models.TextField()
    precio = models.PositiveIntegerField()
    categoria = models.CharField(choices=categoria, max_length=80, null=True)

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'
