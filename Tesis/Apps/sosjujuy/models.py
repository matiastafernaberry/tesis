from django.db import models
from django.contrib.auth.models import User


NA, LUNES, MARTES, MIERCOLES, JUEVES, VIERNES, SABADO, DOMINGO = range(-1, 7)
Dias = (
    (NA, '-'),
    (LUNES, 'Lunes'),
    (MARTES, 'Martes'),
    (MIERCOLES, 'Miércoles'),
    (JUEVES, 'Jueves'),
    (VIERNES, 'Viernes'),
    (SABADO, 'Sábado'),
    (DOMINGO, 'Domingo'),
)


NA, ODONTOLOGIA, INGLES, PSICOLOGIA = range(-1, 3)
Rubros = (
    (NA, '-'),
    (ODONTOLOGIA, 'Odontología'),
    (INGLES, 'Clases de Inglés'),
    (PSICOLOGIA, 'Psicología'),
)

DNI, LE, LC = range(-1, 2)
Tipo_Documento = (
    (DNI, 'Documento Único'),
    (LE, 'Libreta de Enrolamiento'),
    (LC, 'Libreta Cívica'),
)


class Pais(models.Model):
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Provincia(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=30)

    def __str__(self):
        return self.nombre


class Persona(models.Model):
    nombre = models.CharField(max_length=60)
    apellido = models.CharField(max_length=60)
    tipo_documento = models.IntegerField(choices=Tipo_Documento, default=DNI)
    documento = models.IntegerField()
    sexo = models.CharField(max_length=1)
    fecha_de_nacimiento = models.DateField()
    telefono = models.CharField(max_length=16, null=True)

    class Meta:
        abstract = True

    def nombre_completo(self):
        cadena = "{0}, {1}"
        return cadena.format(self.apellido, self.nombre)

    def __str__(self):
        return self.nombre_completo()


class Domicilio(models.Model):
    pais = models.ForeignKey(Pais, on_delete=models.SET_NULL, null=True)
    provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
    ciudad = models.CharField(max_length=60)
    barrio = models.CharField(max_length=60, null=True)
    calle = models.CharField(max_length=60)
    numero = models.CharField(max_length=60)
    piso = models.CharField(max_length=60, null=True, blank=True)
    departamento = models.CharField(max_length=60, null=True, blank=True)
    observaciones = models.CharField(max_length=100, null=True, blank=True)

    def domicilio_completo(self):
        cadena = "{0}, {1} - {2} {3}"
        return cadena.format(self.provincia, self.ciudad, self.calle, self.numero)

    def __str__(self):
        return self.domicilio_completo()


class Antecedente(models.Model):
    enfermedad = models.CharField(max_length=60)
    fecha_aparicion = models.DateField()
    medicamento = models.CharField(max_length=60)


class Beneficiario(Persona):
    domicilio_legal = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, blank=True, null=True,
                                        related_name='domicilio_legal')
    domicilio_real = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, blank=True, null=True,
                                       related_name='domicilio_real')
    antecedente = models.ForeignKey(Antecedente, on_delete=models.SET_NULL, blank=True, null=True)
    familiar = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, default=None)
    email = models.EmailField(max_length=70, default='')


class Prestador(Persona):
    matricula = models.IntegerField()
    especialidad = models.CharField(max_length=300)


class Disponibilidad_horaria(models.Model):
    dia_de_la_semana = models.IntegerField(choices=Dias, default=NA)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()


class Prestacion(models.Model):
    rubro = models.CharField(max_length=300)
    dias_disponibles = models.ForeignKey(Disponibilidad_horaria, on_delete=models.SET_NULL, blank=True, null=True)
    domicilio = models.ForeignKey(Domicilio, on_delete=models.SET_NULL, blank=True, null=True)
    porcentaje_de_cobertura = models.PositiveIntegerField()
    prestador = models.ForeignKey(Prestador, on_delete=models.SET_NULL, blank=True, null=True)
    descripcion = models.CharField(max_length=300)
    condiciones_de_prestacion = models.CharField(max_length=300)
    aclaraciones = models.CharField(max_length=300)

    def prestacion_completo(self):
        cadena = "{0}: {1}"
        return cadena.format(self.rubro, self.prestador)

    def __str__(self):
        return self.prestacion_completo()


class Notificacion(models.Model):
    escala = models.CharField(max_length=300)
    escalaDos = models.CharField(max_length=300)
    asunto = models.CharField(max_length=300)
    fecha = models.DateTimeField(auto_now_add=True)
    prestador = models.ForeignKey(Prestador, on_delete=models.SET_NULL, blank=True, null=True)
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        cadena = "{0}, {1}"
        return cadena.format(self.asunto, self.escala)


class NotificacionEstado(models.Model):
    notificacion = models.ForeignKey(Notificacion, on_delete=models.SET_NULL, blank=True, null=True)
    estado = models.CharField(max_length=300)
    observacion = models.CharField(max_length=500)
    archivo = models.FileField(max_length=254, null=True, blank=True)
    user = models.ForeignKey(User, models.SET_NULL, blank=True,null=True)

    def __str__(self):
        cadena = "{0}, {1}"
        return cadena.format(self.estado, self.observacion)


class ActividadExtension(models.Model):
    titulo = models.CharField(max_length=60)
    descripcion = models.CharField(max_length=300)
    fecha = models.DateTimeField()
    presupuesto = models.PositiveIntegerField()
    disertante = models.ForeignKey(Prestador, on_delete=models.SET_NULL, blank=True, null=True)
    capacidad = models.PositiveIntegerField()


class Derivacion(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.CASCADE)
    fecha_hora = models.DateTimeField(null=True)
    motivo = models.CharField(max_length=300)
    prestacion = models.ForeignKey(Prestacion, on_delete=models.CASCADE)
    observacion = models.CharField(max_length=300)

    def derivacion_completo(self):
        cadena = "{0} el día {1}/{2} a las {3} hs"
        if self.fecha_hora:
            return cadena.format(self.prestacion, self.fecha_hora.date.day, self.fecha_hora.date.month, self.fecha_hora.time)
        else:
            return "{0}".format(self.prestacion)

    def __str__(self):
        return self.derivacion_completo()


class EncuestaAtencionBeneficiario(models.Model):
    beneficiario = models.ForeignKey(Beneficiario, on_delete=models.SET_NULL, blank=True, null=True)
    derivacion = models.ForeignKey(Derivacion, on_delete=models.SET_NULL, blank=True, null=True)
    atendido = models.BooleanField()
    nivel_de_atencion = models.IntegerField(choices=[(x, x) for x in range(1, 6)], default=0)
    nivel_de_puntualidad = models.IntegerField(choices=[(x, x) for x in range(1, 6)], default=0)
    observacion = models.CharField(max_length=300)
