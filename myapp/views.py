from django.shortcuts import render
from .models import File
from .forms import video
from django.http import HttpResponse
from .functions.functions import uploded_file_fn
# Create your views here.
def index(request):
    all_video=File.objects.all()
    if request.method == "POST":
        form=video(data=request.POST,files=request.FILES)
        if form.is_valid():
            uploded_file_fn(request.FILES['videofile'])
            form.save()
            return HttpResponse("<h1> Uploaded successfully </h1>")
    else:
        form=video()
        return render(request,'myapp/index.html',{"form":form,"all":all_video})