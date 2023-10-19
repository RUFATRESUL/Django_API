from django.urls import path
from . import views

urlpatterns = [
    path('studios/',views.StudioListAV.as_view(),name='studio_list'),
    path('studios/<int:pk>/',views.StudioDetailAV.as_view(),name='studio_detail'),
    path('genres/',views.GenreListAV.as_view(),name='genre_list'),
    path('genres/<int:pk>/',views.GenreDetailAV.as_view(),name='genre_detail'),
    path('movies/',views.MovieListAV.as_view(),name='movie_list'),
    path('movies/<int:pk>/',views.MovieDetailAV.as_view(),name='movie_detail'),
    path('movies/<int:pk>/form-update/', views.MovieFormUpdateAV.as_view(), name='movie-form-update'),
    path('movies/movie_comment/<int:movie_pk>/',views.BlogCommentListCreateAV.as_view(),name='blog_comment'),
    
]
