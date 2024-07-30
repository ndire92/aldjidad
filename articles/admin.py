from django.contrib import admin
from .models import Article, Media, Slider, Rapport, Even

# Enregistrement des modèles dans l'admin
admin.site.register(Article)
admin.site.register(Media)
admin.site.register(Slider)
admin.site.register(Rapport)  # Assurez-vous que ce nom est correct
admin.site.register(Even)
