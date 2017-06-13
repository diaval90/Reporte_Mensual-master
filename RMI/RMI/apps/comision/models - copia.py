from __future__ import unicode_literals

from django.db import models

# Create your models here.
TIPO_CUENTA =(
	('Corriente','Corriente'),
	('Ahorros','Ahorros'),
)
TIPO_CONTRATO =(
	('Planta','Planta'),
	('Contrato','Contrato'),
)


class Ciudad (models.Model):
	nombre 			= models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre

class Regional (models.Model):
	nombre 			= models.CharField(max_length=500)

	def __unicode__(self):
		return self.nombre

class Centro (models.Model):
	nombres 			= models.CharField(max_length=500)
	regional 			= models.ForeignKey(Regional)
	
	def __unicode__(self):
		return self.nombres

class Supervisor (models.Model):
	nombres 			= models.CharField(max_length=500)
	cargo 				= models.CharField(max_length=500)
	centro 				= models.ForeignKey(Centro)

	def __unicode__(self):
		return self.nombres

class Instructor (models.Model):
	nombres 			= models.CharField(max_length=500)
	identificacion 		= models.CharField(max_length=500)
	celular		 		= models.CharField(max_length=500)
	email		 		= models.EmailField()
	fecha_de_nacimiento = models.DateField()
	tipo_cuenta			= models.CharField(max_length=500, choices=TIPO_CUENTA)
	numero_cuenta		= models.CharField(max_length=500)
	firma 				= models.ImageField(upload_to='firmas')
	def __unicode__(self):
		return self.nombres

class Contrato (models.Model):
	tipo_vinculacion	= models.CharField(max_length=20, choices=TIPO_CONTRATO)
	numero 				= models.CharField(max_length=500)
	vencimiento_contrato= models.DateField()
	asignacion_mensual	= models.CharField(max_length=500)
	grado				= models.CharField(max_length=500, blank= True, null=True)
	objeto_contractual  = models.CharField(max_length=5000)
	instructor 			= models.ForeignKey(Instructor)
	supervisor			= models.ForeignKey(Supervisor)

	def __unicode__(self):
		return self.numero

class Tiquete (models.Model):
	ciudad_origen 			= models.ForeignKey(Ciudad)
	ida_fecha_salida 		= models.DateField()
	ida_hora_salida 		= models.TimeField()
	regreso_fecha_partida 	= models.DateField()
	regreso_hora_partida 	= models.TimeField()
	instructor 				= models.ForeignKey(Instructor)

	def __unicode__(self):
		return str(self.ciudad_origen.nombre)+ self.instructor.nombres 



