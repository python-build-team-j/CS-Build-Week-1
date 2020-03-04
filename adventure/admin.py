from django.contrib import admin

from .models import Room, Player

# From tutorial - can ignore for now
# class NoteAdmin(admin.ModelAdmin):
#     # read only fields from models.py
#     readonly_fields = ("created_at", "last_modified")


# Register your models here.
admin.site.register(Room)
admin.site.register(Player)
