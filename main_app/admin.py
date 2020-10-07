from django.contrib import admin
# import your models here
from .models import Puffin, Feeding

# Register your models here
admin.site.register(Puffin)
admin.site.register(Feeding)