from django.urls import path
from . import views

# app_name = 'library'

urlpatterns = [
    path('', views.index, name='index'),

    path('books/', views.listBooks, name='books'),
    path('book/<int:pk>', views.bookDetails, name='book-detail'),
    path('book/add', views.BookCreate.as_view(), name='book-add'),
    path('book/update/<int:pk>', views.BookUpdate.as_view(), name='book-update'),
    path('book/delete/<int:pk>', views.BookDelete.as_view(), name='book-delete'),

    path('authors/', views.listAuthors, name='authors'),
    path('author/add', views.AuthorCreate.as_view(), name='author-add'),
    path('author/update/<int:pk>', views.AuthorUpdate.as_view(), name='author-update'),
    path('author/delete/<int:pk>', views.AuthorDelete.as_view(), name='author-delete'),

]
