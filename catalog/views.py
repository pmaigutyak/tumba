from django.shortcuts import render, get_object_or_404

from catalog.models import Tumb, Category

from django.shortcuts import redirect

def home(request):
    query = request.GET.get('q')
    tumbs = Tumb.objects.all()

    if query:
        tumbs = tumbs.filter(title__icontains=query)

    return render(request, 'main/home.html', {'tumbs': tumbs})

def add_favorite(request, id):
    favorites = request.session.get('favorites', [])

    if id not in favorites:
        favorites.append(id)

    request.session['favorites'] = favorites

    return redirect('home')

def tumb_detail(request, id):
    tumb = get_object_or_404(Tumb, id=id)
    return render(request, 'main/tumb_detail.html', {'tumb': tumb})


def get_categories(request):
    categories = Category.objects.all()
    return render(request, 'main/categories.html', {'categories': categories})


def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    tumbs = Tumb.objects.filter(category=category)
    return render(request, 'main/category.html', {
        'category': category,
        'tumbs': tumbs
    })


def about(request):
    return render(request, 'main/about.html')
