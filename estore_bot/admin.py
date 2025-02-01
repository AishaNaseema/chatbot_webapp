from django.contrib import admin

# Register your models here.
from .models import Order  # Import the model

admin.site.register(Order)  # Register the model
