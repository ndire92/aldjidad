from django import forms
from .models import Article, Media, Slider,Even

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['user', 'title', 'content', 'image']
        

class MediaForm(forms.ModelForm):
    class Meta:
        model = Media
        fields = ['user', 'title', 'video_url']

class SliderForm(forms.ModelForm):
    class Meta:
        model = Slider
        fields = ['title', 'image', 'sub_title']


class ArticleForm(forms.ModelForm):
    title = forms.CharField(
        label='Titre', 
        widget=forms.TextInput(attrs={
            'class': 'form-control',  # Correction de la faute de frappe "form-controle"
        })
    )
    content = forms.CharField(
        label='Content', 
        widget=forms.Textarea(attrs={
            'class': 'form-control',  # Classe CSS pour le textarea
            'cols': 100,              # Largeur en colonnes
            'rows': 20                # Hauteur en lignes
        })
    )
    image = forms.ImageField(required=False)  # Assurez-vous d'ajouter le champ image s'il est utilisé

    class Meta:
        model = Article
        fields = ['title', 'content', 'image']
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',  # Classe CSS pour le textarea
                'cols': 100,              # Largeur en colonnes
                'rows': 20                # Hauteur en lignes
            }),
        }

class EvenForm(forms.ModelForm):
    class Meta:
        model = Even
        fields = ['even']