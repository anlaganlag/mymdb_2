from django.urls import path
from . import views

app_name = 'core'
urlpatterns = [
    path('movies',
                views.MoiveList.as_view(),
                name='MovieList'),

    path('movies/<int:pk>',
                views.MoiveDetail.as_view(),
                name='MovieDetail'),
]