from django.urls import path
from . import views


app_name = 'articles'
urlpatterns = [
    path('', views.article_list, name='article_list'),  # La liste des articles
    path('articles/<int:id>/', views.article_detail, name='article_detail'),
    path('articles/<int:id>/update/', views.article_update, name='article_update'),
    path('articles/<int:id>/delete/', views.article_delete, name='article_delete'),
    path('create/', views.article_create, name='article_create'),  # Création d'un nouvel article
    path('<int:id>/', views.article_detail, name='article_detail'),  # Détails d'un article
    path('medias/', views.media_list, name='media_list'),  # Liste des médias
    path('medias/create/', views.media_create, name='media_create'),  # Création de médias
    path('medias/update/<int:pk>/', views.media_update, name='media_update'),
    path('medias/delete/<int:pk>/', views.media_delete, name='media_delete'),
    path('sliders/', views.slider_list, name='slider_list'),  # Liste des sliders
    path('sliders/create/', views.slider_create, name='slider_create'),  # Création de sliders
    path('events/create/', views.even_create, name='even_create'),
    path('events/<int:pk>/update/', views.even_update, name='even_update'),
    path('events/<int:pk>/delete/', views.even_delete, name='even_delete'),
    path('events/', views.even_list, name='even_list'),  # Ajoutez une vue pour lister les événements

]



