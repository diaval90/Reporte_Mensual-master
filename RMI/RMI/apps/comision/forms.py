from django import forms
from .models import *
class Regional_form(forms.ModelForm):
	class Meta:
		model = Regional
		fields = '__all__'	

class Comision_form(forms.ModelForm):
	class Meta:
		model = Comision
		fields = '__all__'
		widgets= {
			'fecha_de_nacimiento': forms.DateInput(attrs={'class':'datepicker'}),
			'ida_fecha_salida': forms.DateInput(attrs={'class':'datepicker'}),
			'regreso_fecha_partida': forms.DateInput(attrs={'class':'datepicker'}),
			'vencimiento_contrato': forms.DateInput(attrs={'class':'datepicker'}),
        	'objeto_contractual': forms.Textarea(attrs={'class':"materialize-textarea" ,'cols': 80, 'rows': 20  }),
			#'firma': forms.FileInput(attrs={'class':"file-field input-field"}),
			'ida_hora_salida': forms.TextInput(attrs={'placeholder':'18:50'}),
			'regreso_hora_partida': forms.TextInput(attrs={'placeholder':'18:50'}),


		}
