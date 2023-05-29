from django.contrib import admin

from .forms import ClientsForm, SalonForm, MasterForm
from .models import Clients, Salon, Master


@admin.register(Clients)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'master', 'service', 'price', 'visit_time')
    form = ClientsForm


@admin.register(Salon)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'adress')
    form = SalonForm


@admin.register(Master)
class ClientsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'working_hours')
    form = MasterForm
