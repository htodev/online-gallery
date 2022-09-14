
from django.urls import path

# from titles import views
from titles.views import detail_title, photo_detail

urlpatterns = [
    path('title/<str:pk>/', detail_title, name='title-photos'),
    path('title/photo/<str:pk>/', photo_detail, name='photo'),
]