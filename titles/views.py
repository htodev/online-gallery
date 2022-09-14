from django.shortcuts import render

from photos.models import Photo
from titles.models import Title


def detail_title(request, pk):
    title = Title.objects.get(id=pk)
    photos = title.photo_set.all()
    contex = {'photos': photos}
    return render(request, 'titles/title_detail.html', contex)


def photo_detail(request, pk):
    photo = Photo.objects.get(id=pk)

    contex = {'photo': photo}
    return render(request, 'titles/photo_detail.html', contex)