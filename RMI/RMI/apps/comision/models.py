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

class Regional (models.Model):
	regional 			= models.CharField(max_length=500)

	def __unicode__(self):
		return self.regional

class Comision (models.Model):
	
	nombres_comisionado	= models.CharField(max_length=500)
	identificacion 		= models.CharField(max_length=500)
	celular		 		= models.CharField(max_length=500)
	email		 		= models.EmailField()
	fecha_de_nacimiento = models.DateField()
	firma 				= models.FileField(upload_to='firmas')

	tipo_cuenta			= models.CharField(max_length=500, choices=TIPO_CUENTA)
	numero_cuenta		= models.CharField(max_length=500)
	banco				= models.CharField(max_length=500)
	tipo_vinculacion	= models.CharField(max_length=20, choices=TIPO_CONTRATO)

	numero_contrato		= models.CharField(max_length=500)
	objeto_contractual  = models.CharField(max_length=5000)
	vencimiento_contrato= models.DateField()
	asignacion_mensual	= models.CharField(max_length=500)
	
	grado				= models.CharField(max_length=500, blank= True, null=True)
	
	supervisor 			= models.CharField(max_length=500)
	cargo 				= models.CharField(max_length=500)
	regional 			= models.ForeignKey(Regional)
	centro  			= models.CharField(max_length=500)

	ciudad_origen 			= models.CharField(max_length=500)
	ida_fecha_salida 		= models.DateField()
	ida_hora_salida 		= models.TimeField()
	regreso_fecha_partida 	= models.DateField()
	regreso_hora_partida 	= models.TimeField()

	fecha_de_registro 	= models.DateTimeField(auto_now_add=True, null=True, blank=True)


	def clean(self):
		if self.regreso_fecha_partida:
			if self.ida_fecha_salida > self.ida_fecha_salida and self.ida_fecha_salida > self.fecha_de_nacimiento:
				raise ValidationError('La fecha de inicio no puede ser mayor a la fecha de fin')

	def __unicode__(self):
		return self.nombres_comisionado


