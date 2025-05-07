from django.urls import path
from .views import BookListView, BookDetailView

app_name = 'books'

urlpatterns = [
    path('', BookListView.as_view(), name='main'), # This matches /books/
    path('list/<pk>', BookDetailView.as_view(), name='detail') # This matches /books/list/2

]

