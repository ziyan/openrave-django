
from django.contrib import admin
from user.models import Key

class KeyAdmin(admin.ModelAdmin):
    list_display = ['key', 'user', 'created', 'modified']

admin.site.register(Key, KeyAdmin)
