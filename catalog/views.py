from django.shortcuts import render, get_object_or_404

from catalog.models import Tumb, Category


def home(request):
    tumbs = Tumb.objects.all()
    return render(request, 'main/home.html', {'tumbs': tumbs})


def tumb_detail(request, id):
    tumb = get_object_or_404(Tumb, id=id)
    return render(request, 'main/tumb_detail.html', {'tumb': tumb})


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'main/categories.html', {'categories': categories})


def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    return render(request, 'main/category.html', {'category': category})


def about(request):
    return render(request, 'main/about.html')
