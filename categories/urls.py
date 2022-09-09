
from django.urls import path


from categories.views import list_categories, detail_category

urlpatterns = [
    path('', list_categories, name='all-categories'),
    path('category/<str:pk>/', detail_category, name='category')
]