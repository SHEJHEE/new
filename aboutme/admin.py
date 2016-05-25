from django.contrib import admin
from .models import Content
from .models import TemplateImage

# Register your models here.
admin.site.register(Content)
admin.site.register(TemplateImage)