from django.shortcuts import render, get_object_or_404
from django.template.context_processors import request

from .models import Tumb

def home(request):
    tumbs = Tumb.objects.all()
    return render(request, 'main/home.html', {'tumbs': tumbs})


def tumb_detail(request, id):
    tumb = get_object_or_404(Tumb, id=id)
    return render(request, 'main/tumb_detail.html', {'tumb': tumb})
def blog(request):
    return render(request, 'main/blog.html')
def about(request):
    return render(request, 'main/about.html')
