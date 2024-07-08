from django.contrib import admin
from .models import Form


# class ModelAdmin designed to modify admin interfaces
class FormAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email", "date", "occupation")
    search_fields = ("first_name", "last_name", "email", "date", "occupation")
    list_filter = ("date", "occupation")
    odering = ("first_name",)
    readonly_fields = ("occupation", )

admin.site.register(Form, FormAdmin)
