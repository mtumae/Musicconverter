from django.shortcuts import render, HttpResponse, redirect
from django_htmx.http import HttpResponseLocation
from django.http import Http404
from .models import Mxl_files, video_files
from .forms import mxl_files, Tester
import os
from .VideoRender import VideoRenders


# Create your views here.

def home(request):
    file_count = Mxl_files.objects.count()
    form = mxl_files(request.POST, request.FILES)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            filename = str(form.cleaned_data.get('mxl_file'))
            filename_mp4 = filename.removesuffix('.mxl')+".mp4"
            filename_mxl = os.path.join("media", filename)
            context = {
                "filename":filename,
                'filename_mp4':filename_mp4,
                'filename_mxl':filename_mxl
            }
            VideoRenders(filename, filename_mp4).render(request)
            return render(request, 'home.html', {"filename_mp4": filename_mp4})
        else:
            errors = form.errors
            context = {
                'form':form,
                'error':errors
            }
            return render(request, "home.html", context)
    context = {
        'file_count':file_count,
        'form':form,
    }
    
    return render(request, 'home.html', context)


#
# REMEMBER TO ADD ICONS 🫵🏿🫵🏿
#


def upload(request):
    file_count = Mxl_files.objects.count()
    print(file_count)
    return render(request, 'home.html', {'file_count':file_count})


def loading(request):
    return render(request, "main/loading.html")

def download(request):
    video = video_files.objects.all()
    return render(request, "main/download.html", {'video':video})

