from django.db import models
import json

# Create your models here.

class Document(models.Model):
    file = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    chunks_json = models.TextField(blank=True) 
    index_path = models.CharField(max_length=255, blank=True) #file path

    def __str__(self):
        return self.file.name