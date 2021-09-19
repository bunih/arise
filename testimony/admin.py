from django.contrib import admin
from .models import (Testimony,Believer,Location)
# Register your models here.
@admin.register(Testimony)
class TestimonyAdmin(admin.ModelAdmin):
    list_display = [
        'title',
    ]
    prepopulated_fields = {'slug': ('title',)}



@admin.register(Believer)
class BelieverAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]


@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display = [
        'name'
    ]
