from django.contrib import admin
from .models import Paciente, Doctor, Cita, Agenda, Servicio

admin.site.register(Paciente)
admin.site.register(Doctor)
admin.site.register(Cita)
admin.site.register(Agenda)
admin.site.register(Servicio)
