from django.db import models
from django.conf import settings

# Create your models here.
class Content(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    summary = models.CharField(max_length=200)
    work_exp = models.TextField()
    is_published = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    template_image = models.ForeignKey('TemplateImage', blank=True, null=True)

class TemplateImage(models.Model):
    image = models.ImageField(blank=True, null=True)