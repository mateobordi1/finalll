from django.contrib import admin
from .models import User , Categoria, Asistencia , Partido

admin.site.register(User),
admin.site.register(Categoria),
admin.site.register(Asistencia),
admin.site.register(Partido),

# Register your models here.
