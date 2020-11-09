from django.db import models

class cuenta(models.Model):
    nom_usuario = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=15)

class cliente(models.Model):
    nom_cliente = models.CharField(max_length=15)
    apellido_paterno = models.CharField(max_length=15)
    apellido_materno = models.CharField(max_length=15)
    correo = models.CharField(max_length=30)
    telefono = models.CharField(max_length=9)
    genero = models.CharField(max_length=10)
    rut = models.CharField(max_length=15)
    tipo_cuenta = models.IntegerField(max_length=1)
    id_cuenta = models.ForeignKey(cuenta, on_delete=models.CASCADE)

class juego(models.Model):
    id_juego = models.CharField( max_length=10)
    juegos = models.CharField(max_length=20)
    precio = models.CharField(max_length=15)
