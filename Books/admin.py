from ctypes.wintypes import BOOL
from django.contrib import admin

# Register your models here.
from .models import Department,Book
admin.site.register((Department,Book,))