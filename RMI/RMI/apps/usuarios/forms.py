#-*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User 
from RMI.apps.usuarios.models import *
#from django.forms.widgets import PasswordInput

SUPERVISOR=(
	('Julio Prado','Julio Prado '),
	('Maria del Carmen','Maria del Carmen'),
	('Janeth Patricia','Janeth Patricia'),
	('No tiene','No tiene'),
	)

AREA=(
	('Electricidad','Electricidad'),
	('Electrónica','Electrónica'),
	('Mantenimiento y Redes de Computadores','Mantenimiento y Redes de Computadores'),
	('Transversales','Transversales'),
	('Telecomunicaciones','Telecomunicaciones'),
	('Confecciones','Confecciones'),
	('Actividad Física','Actividad Física'),
	('Ebanistería','Ebanistería'),
	('Marroquinería','Marroquinería'),
	('Joyería','Joyería'),
	('Inglés','Inglés'),
	('Construcción','Construcción'),
	('Desarrollo de Software','Desarrollo de Software'),
	('Industrias Creativas','Industrias Creativas'),
	('Gestión Empresarial','Gestión Empresarial'),
	('Mecánica','Mecánica'),
	('Minería','Minería'),
	('Ambiental','Ambiental'),
	('Soldadura ','Soldadura '),
	('Virtualismo','Virtualismo'),
	('Tecnico en sistemas','Tecnico en sistemas'),	
	('Electricidad Tecnico','Electricidad Tecnico'),
	('Aula Movil','Aula Movil'),
	('Apoyo Pedagodico','Apoyo Pedagodico'),
	('Santander','Santander'),
	('CNC','CNC'),
	('Artesanias', 'Artesanias'),
	('No tiene','No tiene'),
	)

class Login_form(forms.Form):

	usuario = forms.CharField(label="Cedula",widget = forms.TextInput())	
	clave = forms.CharField(widget = forms.PasswordInput(render_value = False))	

class Reporte(forms.ModelForm):	

	#nombre_adjunto = forms.CharField(label='Nombre del adjunto',max_length = 50,widget = forms.TextInput())
	#adjunto_exel = forms.FileField(label='Adjunto')
	

	class Meta:
		model = Reporte_Mensual
		fields = '__all__'
		exclude = ['mes','usuario']

class UserForm(forms.ModelForm):	

	first_name = forms.CharField(label="Nombres",widget=forms.TextInput())
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())
	#telefono = forms.CharField(label="Telefono",widget=forms.TextInput())	
	#password = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))

	class Meta:
		model = User
		fields = ['first_name','last_name','email']
			

class AdminUserForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['first_name','last_name','username','email']

	first_name = forms.CharField(label="Nombres",widget=forms.TextInput())
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())
	username = forms.CharField(label="Cedula",widget=forms.TextInput())
	email    = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput())
	#password = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))

class User_profile_Form(forms.ModelForm):
	class Meta:
		model = User_profile
		fields = ['telefono','supervisor','area']	

	telefono = forms.CharField(label="Teléfono",widget=forms.TextInput())	

class RegisterForm(forms.Form):
	
	first_name = forms.CharField(label="Nombres",widget=forms.TextInput())
	last_name = forms.CharField(label="Apellidos",widget=forms.TextInput())
	username = forms.CharField(label="Cedula",widget=forms.TextInput())
	email    = forms.EmailField(label="Correo Electrónico",widget=forms.TextInput())
	telefono = forms.CharField(label="Teléfono",widget=forms.TextInput())
	supervisor = forms.CharField(label='Supervisor',max_length = 50,widget=forms.Select(choices=SUPERVISOR))
	area = forms.CharField(label='Area',max_length = 50,widget=forms.Select(choices=AREA))
	password_one = forms.CharField(label="Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))	
	
	def clean_username(self):
		username = self.cleaned_data['username']
		try:
			u = User.objects.get(username=username)
		except User.DoesNotExist:
			return username 
		raise forms.ValidationError('Cedula ya registrada')	

	def clean_email(self):
		email = self.cleaned_data['email']
		try:		
			u = User.objects.get(email=email)
		except User.DoesNotExist:
			return email 
		raise forms.ValidationError('Email ya registrado')
	
	def clean_password_two(self):
		password_one = self.cleaned_data['password_one']			
		password_two = self.cleaned_data['password_two']

		if password_one == password_two:	
			pass 
		else:
			raise forms.ValidationError('Password no coinciden')

class PasswordForm(forms.ModelForm):

	class Meta:
		model = User
		fields = ['password']

	password = forms.CharField(label="Nuevo Password",widget=forms.PasswordInput(render_value=False))
	password_two = forms.CharField(label="Confirmar password",widget=forms.PasswordInput(render_value=False))	
		
	
	def clean_password_two(self):
		password = self.cleaned_data['password']			
		password_two = self.cleaned_data['password_two']

		if password == password_two:	
			pass 
		else:
			raise forms.ValidationError('Password no coinciden')									