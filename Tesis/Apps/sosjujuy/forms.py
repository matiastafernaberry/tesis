from datetimewidget import widgets
from django import forms

from .models import Domicilio, Beneficiario, Derivacion, Prestador, Prestacion, ActividadExtension, \
    EncuestaAtencionBeneficiario


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ('pais',
                  'provincia',
                  'ciudad',
                  'barrio',
                  'calle',
                  'numero',
                  'observaciones')

        labels = {'pais': 'Pais ',
                  'provincia': 'Provincia ',
                  'ciudad': 'Ciudad ',
                  'barrio': 'Barrio ',
                  'calle': 'Calle ',
                  'numero': 'Nº ',
                  'observaciones': 'Observaciones '
                  }

        widgets = {'pais': forms.Select(attrs={'class': 'form-control'}),
                   'provincia': forms.Select(attrs={'class': 'form-control'}),
                   'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
                   'barrio': forms.TextInput(attrs={'class': 'form-control'}),
                   'calle': forms.TextInput(attrs={'class': 'form-control'}),
                   'numero': forms.TextInput(attrs={'class': 'form-control'}),
                   'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows':2})
                   }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)


class BeneficiarioForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True
        }
        model = Beneficiario
        fields = ('numero_beneficiario',
                  'nombre',
                  'apellido',
                  'tipo_documento',
                  'documento',
                  'sexo',
                  'fecha_de_nacimiento',
                  'email',
                  'telefono')

        labels = {'numero_beneficiario': 'Nº Beneficiario ',
                  'nombre': 'Nombre ',
                  'apellido': 'Apellido ',
                  'tipo_documento': 'Tipo de Documento ',
                  'documento': 'Nº de Documento ',
                  'sexo': 'Sexo ',
                  'fecha_de_nacimiento': 'Fecha de Nacimiento ',
                  'email': 'E-mail',
                  'telefono': 'Teléfono '}

        widgets = {'numero_beneficiario': forms.TextInput(attrs={'class': 'form-control'}),
                   'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                   'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
                   'documento': forms.TextInput(attrs={'class': 'form-control'}),
                   'sexo': forms.TextInput(attrs={'class': 'form-control'}),
                   'fecha_de_nacimiento': widgets.DateWidget(attrs={'id': 'id_fecha', 'class': 'form-control'}, bootstrap_version=3, options=dateTimeOptions),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PrestadorForm(forms.ModelForm):
    class Meta:
        model = Prestador
        fields = ('matricula',
                  'especialidad',
                  'nombre',
                  'apellido',
                  'tipo_documento',
                  'documento',
                  'sexo',
                  'fecha_de_nacimiento',
                  'telefono')

        labels = {'matricula': 'Nº Matricula ',
                  'especialidad': 'Especialidad ',
                  'nombre': 'Nombre ',
                  'apellido': 'Apellido ',
                  'tipo_documento': 'Tipo de Documento ',
                  'documento': 'Nº de Documento ',
                  'sexo': 'Sexo ',
                  'fecha_de_nacimiento': 'Fecha de Nacimiento ',
                  'telefono': 'Telefono '}

        widgets = {'matricula': forms.TextInput(attrs={'class': 'form-control'}),
                   'especialidad': forms.TextInput(attrs={'class': 'form-control'}),
                   'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                   'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
                   'documento': forms.TextInput(attrs={'class': 'form-control'}),
                   'sexo': forms.TextInput(attrs={'class': 'form-control'}),
                   'fecha_de_nacimiento': forms.DateInput(attrs={'class': 'form-control'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class PrestacionForm(forms.ModelForm):
    class Meta:
        model = Prestacion
        fields = ('rubro',
                  'prestador',
                  'porcentaje_de_cobertura',
                  'descripcion',
                  'condiciones_de_prestacion',
                  'aclaraciones')

        labels = {'rubro': 'Especialidad',
                  'prestador': 'Prestador',
                  'porcentaje_de_cobertura': 'Cobertura %',
                  'descripcion': 'Descripcion',
                  'condiciones_de_prestacion': 'Condiciones',
                  'aclaraciones': 'Observaciones'}

        widgets = {'rubro': forms.TextInput(attrs={'class': 'form-control'}),
                   'prestador': forms.Select(attrs={'class': 'form-control'}),
                   'porcentaje_de_cobertura': forms.TextInput(attrs={'class': 'form-control'}),
                   'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
                   'condiciones_de_prestacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
                   'aclaraciones': forms.Textarea(attrs={'class': 'form-control', 'rows':3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class DerivacionForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii',
            'autoclose': True
        }
        model = Derivacion
        fields = ('beneficiario', 'prestacion', 'fecha_hora', 'motivo', 'observacion')

        labels = {'beneficiario': 'Beneficiario',
                  'prestacion': 'Prestacion',
                  'fecha_hora': 'Fecha y hora',
                  'motivo': 'Motivo',
                  'observacion': 'Observaciones'}

        widgets = {'beneficiario': forms.Select(attrs={'class': 'form-control'}),
                   'prestacion': forms.Select(attrs={'class': 'form-control'}),
                   'fecha_hora': widgets.DateTimeWidget(attrs={'id': 'id_fecha', 'class': 'form-control'},
                                                   bootstrap_version=3, options=dateTimeOptions),
                   'motivo': forms.TextInput(attrs={'class': 'form-control'}),
                   'observacion': forms.Textarea(attrs={'class': 'form-control'})
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class ActividadExtensionForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy HH:ii',
            'autoclose': True
        }
        model = ActividadExtension
        fields = ('titulo', 'descripcion', 'fecha', 'presupuesto', 'disertante', 'capacidad')

        labels = {'titulo': 'Título',
                  'descripcion': 'Descripción',
                  'fecha': 'Fecha',
                  'presupuesto': 'Presupuesto',
                  'disertante': 'Disertante',
                  'capacidad': 'Capacidad'}

        widgets = {'titulo': forms.TextInput(attrs={'class': 'form-control'}),
                   'descripcion': forms.Textarea(attrs={'class': 'form-control'}),
                   'fecha': widgets.DateTimeWidget(attrs={'id': 'id_fecha', 'class': 'form-control'}, bootstrap_version=3, options=dateTimeOptions),
                   'presupuesto': forms.TextInput(attrs={'class': 'form-control'}),
                   'disertante': forms.Select(attrs={'class': 'form-control'}),
                   'capacidad': forms.TextInput(attrs={'class': 'form-control'})
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class EncuestaAtencionBeneficiarioForm(forms.ModelForm):
    class Meta:
        model = EncuestaAtencionBeneficiario
        fields = ('atendido', 'nivel_de_atencion', 'nivel_de_puntualidad', 'observacion')

        labels = {'atendido': '¿Fuiste atendido?',
                  'nivel_de_atencion': '¿Cómo calificás la atención?',
                  'nivel_de_puntualidad': '¿Cómo calificás la puntualidad?',
                  'observacion': '¿Algo que quieras agregar?'}

        widgets = {'atendido': forms.CheckboxInput(attrs={'class': 'form-control'}),
                   'nivel_de_atencion': forms.Select(attrs={'class': 'form-control'}),
                   'nivel_de_puntualidad': forms.Select(attrs={'class': 'form-control'}),
                   'observacion': forms.Textarea(attrs={'class': 'form-control'})
                   }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
