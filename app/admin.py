from django.contrib import admin
from .models import Employee
# Register your models here.

class EmpAdmin(admin.ModelAdmin):
    list_display=["id","name","city","dept","age","salary"]
admin.site.register(Employee,EmpAdmin)    
