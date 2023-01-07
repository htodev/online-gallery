from categories.models import Category

from django.shortcuts import render
from django.core.paginator import Paginator

def list_categories(request):
    categories = Category.objects.all()
    context = {
        'categories': categories,
    }
    return render(request, 'categories/category_list.html', context)


def detail_category(request, pk):
    category = Category.objects.get(id=pk)
    titles = category.title_set.all()
    paginator = Paginator(titles, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    contex = {'page_obj': page_obj}
    return render(request, 'categories/category_detail.html', contex)
