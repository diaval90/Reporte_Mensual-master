from django.shortcuts import render
from .forms import *
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
# Create your views here.
def comision_view (request):

	if request.method == "POST":
		form_Com= Comision_form(request.POST, request.FILES)
		
		if form_Com.is_valid():
			firma = request.FILES['firma']
			try:
				i = form_Com.save(commit = False)
				i.save()
				info = "Informacion Guardada con Exito!" 
			except:
				info = "Debe completar todos los campos"
			
			texto = i.nombres_comisionado+" "+ i.identificacion+" "+i.email 
			mail = EmailMessage('Registro de comision '+i.nombres_comisionado, texto, 'serviciosdocumentosctpi@gmail.com',['dfprado4@misena.edu.co', 'fkenneth228@gmail.com'] )
			#mail.attach(firma.name, firma.read(), firma.content_type)
			file_path = settings.MEDIA_ROOT + str(i.firma)
			print(file_path)
			fd = open("%s"%(file_path),"rb")
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			print (firma.name, firma.read(), firma.content_type)
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			#mail.attach_file(i.firma)
			mail.attach(firma.name, fd.read(), firma.content_type)
			x= mail.send()
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			print x
			print "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"
			fd.close()
			form_Com = Comision_form()
		else:		
			info = "Debe completar todos los campos" 
	if request.method == "GET":
		form_Com = Comision_form()

	return render (request,'comision/comision.html',locals())

def listado_comision_view (request):
	lista = Comision.objects.all().order_by('-id')
	return render (request,'comision/listado_comision.html',locals())

def ver_comision_view (request, id_com):
	comisionado = Comision.objects.get(pk=id_com)
	return render (request,'comision/ver_comision.html',locals())

