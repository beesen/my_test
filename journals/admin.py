from django.contrib import admin
from journals.models import Journal


# Register your models here.
class JournalAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register(Journal, JournalAdmin)
