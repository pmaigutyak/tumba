from django.shortcuts import render
from .forms import TumbForm
from .models import Tumb

def home(request):
    form = TumbForm()
    tumbs = Tumb.objects.all()

    if request.method == 'POST':
        form = TumbForm(request.POST)
        if form.is_valid():
            form.save()

    return render(request, 'main/home.html', {
        'form': form,
        'tumbs': tumbs
    })


def  about(request):
    return render(request, 'main/about.html')
from django.shortcuts import redirect

def delete_tumb(request, id):
    tumb = Tumb.objects.get(id=id)
    tumb.delete()
    return redirect('/')