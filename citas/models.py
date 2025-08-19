from django.db import models

class Paciente(models.Model):
    class AseguradoraSalud(models.TextChoices):
        PRIVADO = "PRIVADO", "Privado"
        ARS_CMD = "ARS_CMD", "ARS CMD"
        ARS_CONSTITUCION = "ARS_CONSTITUCION", "ARS Constitución"
        ARS_FUTURO = "ARS_FUTURO", "ARS Futuro"
        ARS_HUMANO = "ARS_HUMANO", "ARS Humano"
        ARS_INDEPENDIENTE = "ARS_INDEPENDIENTE", "ARS Independiente"
        ARS_MAPFRE = "ARS_MAPFRE", "ARS MAPFRE Salud"
        ARS_MAEP = "ARS_MAEP", "ARS MAEP"
        ARS_META_SALUD = "ARS_META_SALUD", "ARS Meta Salud"
        ARS_MUNICIPAL = "ARS_MUNICIPAL", "ARS SEMMA / Municipal"
        ARS_PALIC = "ARS_PALIC", "ARS Palic"
        ARS_PEPSICO = "ARS_PEPSICO", "ARS PepsiCo"
        ARS_PRESIDENCIAL = "ARS_PRESIDENCIAL", "ARS Primera ARS de Humano"
        ARS_RESERVAS = "ARS_RESERVAS", "ARS Reservas"
        ARS_SIMAG = "ARS_SIMAG", "ARS SIMAG"
        ARS_UNIVERSAL = "ARS_UNIVERSAL", "ARS Universal"
        ARS_YUNEN = "ARS_YUNEN", "ARS Yunen"
        PARTICULAR = "PARTICULAR", "Particular (sin ARS)"
        OTRA = "OTRA", "Otra"

    nombre = models.CharField(max_length=100)
    aseguradora = models.CharField(max_length=255, choices=AseguradoraSalud, default=AseguradoraSalud.PRIVADO)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    fecha_nacimiento = models.DateField()
    direccion = models.CharField(max_length=255, blank=True, null=True)
    sexo = models.CharField(max_length=10, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino')], default='femenino')

    def __str__(self):
        return f"{self.nombre} ({self.aseguradora}) - {self.correo} - {self.telefono}"

class Doctor(models.Model):
    class SeleccionEspecialidad(models.TextChoices):
        ALERGOLOGIA = "ALERGOLOGIA", "Alergología"
        CARDIOLOGIA = "CARDIOLOGIA", "Cardiología"
        DERMATOLOGIA = "DERMATOLOGIA", "Dermatología"
        ENDOCRINOLOGIA = "ENDOCRINOLOGIA", "Endocrinología"
        GASTROENTEROLOGIA = "GASTROENTEROLOGIA", "Gastroenterología"
        GERIATRIA = "GERIATRIA", "Geriatría"
        GINECOLOGIA = "GINECOLOGIA", "Ginecología"
        HEMATOLOGIA = "HEMATOLOGIA", "Hematología"
        INFECTOLOGIA = "INFECTOLOGIA", "Infectología"
        MEDICINA_GENERAL = "MEDICINA_GENERAL", "Medicina General"
        MEDICINA_INTERNA = "MEDICINA_INTERNA", "Medicina Interna"
        NEUMOLOGIA = "NEUMOLOGIA", "Neumología"
        NEFROLOGIA = "NEFROLOGIA", "Nefrología"
        NEUROLOGIA = "NEUROLOGIA", "Neurología"
        NUTRIOLOGIA = "NUTRIOLOGIA", "Nutriología"
        OFTALMOLOGIA = "OFTALMOLOGIA", "Oftalmología"
        ONCOLOGIA = "ONCOLOGIA", "Oncología"
        ORTOPEDIA = "ORTOPEDIA", "Ortopedia"
        OTORRINOLARINGOLOGIA = "OTORRINOLARINGOLOGIA", "Otorrinolaringología"
        PEDIATRIA = "PEDIATRIA", "Pediatría"
        PSIQUIATRIA = "PSIQUIATRIA", "Psiquiatría"
        RADIOLOGIA = "RADIOLOGIA", "Radiología"
        REUMATOLOGIA = "REUMATOLOGIA", "Reumatología"
        TRAUMATOLOGIA = "TRAUMATOLOGIA", "Traumatología"
        UROLOGIA = "UROLOGIA", "Urología"

    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=21, choices=SeleccionEspecialidad, default=SeleccionEspecialidad.ALERGOLOGIA)
    exequatur = models.CharField(max_length=100, unique=True)
    correo = models.EmailField(unique=True)
    telefono = models.CharField(max_length=10, blank=True, null=True)

class Agenda(models.Model):
    SeleccionDia = [
        ('lunes', 'Lunes'),
        ('martes', 'Martes'),
        ('miercoles', 'Miércoles'),
        ('jueves', 'Jueves'),
        ('viernes', 'Viernes'),
        ('sabado', 'Sábado'),
        ('domingo', 'Domingo'),
    ]
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    dia_semana = models.CharField(max_length=10, choices=SeleccionDia)
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()

    class Meta:
        unique_together = ('doctor', 'dia_semana')

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    costo = models.DecimalField(max_digits=10, decimal_places=2, blank=True,  null=True)
    descripcion = models.TextField(blank=True, null=True)

class Cita (models.Model):
    class EstadoCita(models.TextChoices):
        AGENDADA = "AGENDADA", "Agendada"
        COMPLETADA = "COMPLETADA", "Completada"
        CANCELADA = "CANCELADA", "Cancelada"
        AUSENTE = "AUSENTE", "Ausente"

    servicio = models.ForeignKey(Servicio, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    fecha =  models.DateField()
    hora_inicio = models.TimeField()
    estado = models.CharField(max_length=50, choices=EstadoCita, default=EstadoCita.AGENDADA)
    creada_en = models.DateTimeField(auto_now_add=True)