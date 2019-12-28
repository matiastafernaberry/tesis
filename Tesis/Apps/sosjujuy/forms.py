from datetimewidget import widgets
from django import forms

from .models import Domicilio, Beneficiario, Derivacion, Prestador, Prestacion, ActividadExtension, \
    EncuestaAtencionBeneficiario, Notificacion, NotificacionEstado


class DomicilioForm(forms.ModelForm):
    class Meta:
        model = Domicilio
        fields = ('pais',
                  'provincia',
                  'ciudad',
                  'barrio',
                  'calle',
                  'numero',
                  'piso',
                  'departamento',
                  'observaciones')

        labels = {'pais': 'Pais ',
                  'provincia': 'Provincia ',
                  'ciudad': 'Ciudad ',
                  'barrio': 'Barrio ',
                  'calle': 'Calle ',
                  'numero': 'Nº ',
                  'piso': 'Piso',
                  'departamento': 'Departamento',
                  'observaciones': 'Observaciones'
                  }

        widgets = {'pais': forms.Select(attrs={'class': 'form-control'}),
                   'provincia': forms.Select(attrs={'class': 'form-control'}),
                   'ciudad': forms.TextInput(attrs={'class': 'form-control'}),
                   'barrio': forms.TextInput(attrs={'class': 'form-control'}),
                   'calle': forms.TextInput(attrs={'class': 'form-control'}),
                   'numero': forms.TextInput(attrs={'class': 'form-control'}),
                   'piso': forms.TextInput(attrs={'class': 'form-control'}),
                   'departamento': forms.TextInput(attrs={'class': 'form-control'}),
                   'observaciones': forms.Textarea(attrs={'class': 'form-control', 'rows':2})
                   }

        def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)

SEXO=[
  ('h','Hombre'),
  ('m','Mujer'),
  ('o','Otro')]

class BeneficiarioForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True
        }
        model = Beneficiario
        fields = (
                  'nombre',
                  'apellido',
                  'tipo_documento',
                  'documento',
                  'sexo',
                  'fecha_de_nacimiento',
                  'email',
                  'telefono')

        labels = {
                  'nombre': 'Nombre ',
                  'apellido': 'Apellido ',
                  'tipo_documento': 'Tipo de Documento ',
                  'documento': 'Nº de Documento ',
                  'sexo': 'Sexo ',
                  'fecha_de_nacimiento': 'Fecha de Nacimiento ',
                  'email': 'E-mail',
                  'telefono': 'Teléfono '}

        widgets = {
                   'nombre': forms.TextInput(attrs={'class': 'form-control'}),
                   'apellido': forms.TextInput(attrs={'class': 'form-control'}),
                   'tipo_documento': forms.Select(attrs={'class': 'form-control'}),
                   'documento': forms.TextInput(attrs={'class': 'form-control'}),
                   'sexo': forms.RadioSelect(choices=SEXO),
                   'fecha_de_nacimiento': widgets.DateWidget(attrs={'id': 'id_fecha', 'class': 'form-control'}, bootstrap_version=3, options=dateTimeOptions),
                   'email': forms.EmailInput(attrs={'class': 'form-control'}),
                   'telefono': forms.TextInput(attrs={'class': 'form-control'})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


ESCALA=[
  ('','----------'),
  #('Auditoria','Auditoria'),
  ('Actividades de Extension','Actividades de Extension'),
  ('Beneficiarios', 'Beneficiarios'),
  ('Atencion y Derivacion', 'Atencion y Derivacion')
  ]

ESCALADOS=[
  ('','----------'),
  ('Reporte','Reporte'),
  ('Solicitud', 'Solicitud'),
  ('Solicitud de Audiencia', 'Solicitud de Audiencia'),
  ('Pedido Extraordinario', 'Pedido Extraordinario')
  ]

ESTADO=[
  #('Iniciado','Iniciado'),
  #('Enviado','Enviado'),
  ('','----------'),
  ('Pendiente','Pendiente'),
  ('Anulado','Anulado'),
  ('Aprobado','Aprobado'),
  ('Rechazado','Rechazado'),
  ('Finalizado','Finalizado')
  ]

class NotificacionForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True
        }
        model = Notificacion
        fields = (
                  'escala',
                  'escalaDos',
                  'asunto',
                  'prestador',
                  'beneficiario')

        labels = {
                  'escala': 'Escala1 ',
                  'escalaDos': 'Escala2 ',
                  'asunto': 'Asunto ',
                  'prestador': 'Prestador',
                  'beneficiario': 'Beneficiario'
                  }

        widgets = {
                   'escala': forms.Select(choices=ESCALA),
                   'escalaDos': forms.Select(choices=ESCALADOS),
                   'asunto': forms.TextInput(attrs={'class': 'form-control'}),
                   #'estado': forms.Select(choices=ESTADO),
                   #'archivos': forms.ClearableFileInput(attrs={'multiple': True}),
                   #'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NotificacionEstadoForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True
        }
        model = NotificacionEstado
        fields = (
                  #'estado',
                  'observacion',
                  'archivo')

        labels = {
                  #'estado': 'Estado ',
                  'observacion': 'Observaciones',
                  'archivo': 'Adjuntar',
                  }

        widgets = {
                   #'estado': forms.Select(choices=ESTADO),
                   'archivos': forms.ClearableFileInput(attrs={'multiple': True}),
                   'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
                  }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


class NotificacionEstadoUpdateForm(forms.ModelForm):
    class Meta:
        dateTimeOptions = {
            'format': 'dd/mm/yyyy',
            'autoclose': True
        }
        model = NotificacionEstado
        fields = (
                  'estado',
                  'observacion',
                  'archivo')

        labels = {
                  'estado': 'Estado ',
                  'observacion': 'Observaciones',
                  'archivo': 'Adjuntar',
                  }

        widgets = {
                   'estado': forms.Select(choices=ESTADO),
                   'archivos': forms.ClearableFileInput(attrs={'multiple': True}),
                   'observacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
                  }

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

        widgets = {
          'rubro': forms.TextInput(attrs={'class': 'form-control'}),
          'prestador': forms.Select(attrs={'class': 'form-control'}),
          'porcentaje_de_cobertura': forms.TextInput(attrs={'class': 'form-control'}),
          'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
          'condiciones_de_prestacion': forms.Textarea(attrs={'class': 'form-control', 'rows':3}),
          'aclaraciones': forms.Textarea(attrs={'class': 'form-control', 'rows':3})}

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

MOTIVOS=[
  ('Primera Consulta','Primera Consulta'),
  ('Paciente del Profesional','Paciente del Profesional')
  ]

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
                   'motivo': forms.Select(choices=MOTIVOS),
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
