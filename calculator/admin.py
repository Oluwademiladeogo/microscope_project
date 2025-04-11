from django.contrib import admin
from .models import Specimen

@admin.register(Specimen)
class SpecimenAdmin(admin.ModelAdmin):
    list_display = ('username', 'specimen_name', 'microscope_size', 'magnification', 'actual_size', 'created_at')
    search_fields = ('username', 'specimen_name')
    list_filter = ('created_at',)