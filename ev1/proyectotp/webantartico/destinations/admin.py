from django.contrib import admin
from .models import Flip_card

# Register your models here.
class Flip_cardAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')

admin.site.register(Flip_card, Flip_cardAdmin)