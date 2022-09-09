
from django.urls import path

# from titles import views
from titles.views import detail_title

urlpatterns = [
    path('title/<str:pk>/', detail_title, name='title-photos'),
]