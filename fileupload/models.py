# fileupload/models.py
from django.db import models

class FileUpload(models.Model):
    #title = models.TextField(max_length=40, null=True)
    csvfile = models.FileField(null=True, upload_to="", blank=True)
    #content = models.TextField()

    def __str__(self):
        return self.title