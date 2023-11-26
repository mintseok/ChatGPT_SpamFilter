# fileupload/forms.py
from django.forms import ModelForm
from .models import FileUpload

class FileUploadForm(ModelForm):
    class Meta:
        model = FileUpload
        #fields = ['title', 'csvfile', 'content']
        fields = ['csvfile']
    def __init__(self, *args, **kwargs):
        super(ModelForm, self).__init__(*args, **kwargs)
        self.fields['csvfile'].required = True