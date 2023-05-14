from django.shortcuts import render, get_object_or_404


from photos.models import Photo
from titles.models import Title


def detail_title(request, pk):
    title = Title.objects.get(id=pk)
    category_id = title.category.id if title.category else None
    photos = title.photo_set.all()
    context = {'photos': photos, 'title_id': category_id}
    return render(request, 'titles/title_detail.html', context)






def photo_detail(request, pk):
   photo = get_object_or_404(Photo, pk=pk)
   title = photo.title
   photos = title.photo_set.all()
   photo_index = list(photos).index(photo)
   previous_photo = photos[photo_index - 1] if photo_index > 0 else None
   next_photo = photos[photo_index + 1] if photo_index < len(photos) - 1 else None
   context = {
       'photo': photo,
       'previous_photo': previous_photo,
       'next_photo': next_photo,
       'pk': title.id,
   }
   return render(request, 'titles/photo_detail.html', context)
