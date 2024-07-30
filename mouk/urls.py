from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),  # Assurez-vous que 'app.urls' est correct
    path('articles/', include('articles.urls')),  # Inclure les URLs de l'application articles
    path('ckeditor/', include('ckeditor_uploader.urls')),  # Inclure les URLs de CKEditor
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

