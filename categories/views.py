from categories.models import Category

from django.shortcuts import render


def list_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/category_list.html', context)


def detail_category(request, pk):
    category = Category.objects.get(id=pk)
    titles = category.title_set.all()
    contex = {'titles': titles}
    return render(request, 'categories/category_detail.html', contex)
