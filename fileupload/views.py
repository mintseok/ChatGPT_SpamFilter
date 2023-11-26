# fileupload/views.py
from django.shortcuts import render, redirect
from .forms import FileUploadForm
from .models import FileUpload
import time

def fileUpload(request):
    if request.method == 'POST':
        # time.sleep(2)
        print("\nCalled fileUpload from views.py as POST\n")
        #title = request.POST['title']
        #content = request.POST['content']
        csv = request.FILES["csvfile"]
        fileupload = FileUpload(
            #title=title,
            #content=content,
            csvfile=csv,
        )
        fileupload.save()
        return redirect('/getresult')
    else:
        print("\nCalled fileUpload from views.py as GET\n")
        fileuploadForm = FileUploadForm
        context = {
            'fileuploadForm': fileuploadForm,
        }
        return render(request, 'fileupload.html', context)