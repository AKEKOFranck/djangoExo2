from django.contrib import admin
from.models import User

# Register your models here.
class CustomUser(admin.ModelAdmin):
    list_display = ['username', 'last_name', 'age']
    

admin.site.register(User, CustomUser)
