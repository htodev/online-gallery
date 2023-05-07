from django.db import models
from titles.models import Title


def get_upload_path(instance, filename):
    return f'{instance.title.title_name}/{filename}'


class Photo(models.Model):
    picture = models.ImageField(upload_to='gallery', blank=True)
    title = models.ForeignKey(Title, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        # Update the upload path before saving the model instance
        if self.title:
            self.picture.name = get_upload_path(self, self.picture.name)
        super(Photo, self).save(*args, **kwargs)
