from django.shortcuts import render

from titles.models import Title


def detail_title(request, pk):
    title = Title.objects.get(id=pk)
    photos = title.photo_set.all()
    contex = {'photos': photos}
    return render(request, 'titles/title_detail.html', contex)