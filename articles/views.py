from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Article, Even, Media, Slider
from .forms import ArticleForm, EvenForm, MediaForm, SliderForm
from .forms import ArticleForm
from django.contrib import messages
from .forms import MediaForm

def article_list(request):
    articles = Article.objects.all().order_by('-published_date')  # Récupérer tous les articles
    events = Even.objects.all().order_by('-published_date')  # Récupérer tous les événements
    media_items = Media.objects.all()
    active_video = media_items.first()  # La première vidéo comme active
    paginator = Paginator(articles, 4)  # 4 articles par page

    page_number = request.GET.get('page')
    articles = paginator.get_page(page_number)
    return render(request, 'articles/index.html', {'articles': articles,'events': events,'articles': articles,'media_items': media_items, 'active_video': active_video})


def article_detail(request, id):
    article = get_object_or_404(Article, id=id)
    return render(request, 'articles/article_detail.html', {'article': article})

@login_required
def article_create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            article = form.save(commit=False)
            article.user = request.user  # Assigner l'utilisateur connecté
            article.save()
            return redirect('articles:article_list')
    else:
        form = ArticleForm()
    return render(request, 'articles/article_form.html', {'form': form})

def article_update(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list', id=article.id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'articles/article_form.html', {'form': form})



def article_delete(request, id):
    article = get_object_or_404(Article, id=id)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')  # Assurez-vous d'avoir une vue liste pour les articles
    return render(request, 'articles/article_confirm_delete.html', {'article': article})

def media_list(request):
 # Récupérer tous les articles
   
    return render(request, 'articles/index.html')

def media_create(request):
    if request.method == 'POST':
        form = MediaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:article_list')
    else:
        form = MediaForm()
    return render(request, 'articles/media_form.html', {'form': form})


def media_update(request, pk):
    media = get_object_or_404(Media, pk=pk)
    if request.method == 'POST':
        form = MediaForm(request.POST, request.FILES, instance=media)
        if form.is_valid():
            form.save()
            messages.success(request, 'Le média a été mis à jour avec succès.')
            return redirect('articles:article_list')
        else:
            messages.error(request, 'Il y a eu une erreur dans le formulaire. Veuillez réessayer.')
    else:
        form = MediaForm(instance=media)
    return render(request, 'articles/media_form.html', {'form': form})

def media_delete(request, pk):
    media = get_object_or_404(Media, pk=pk)
    if request.method == 'POST':
        media.delete()
        messages.success(request, 'Le média a été supprimé avec succès.')
        return redirect('media_list')
    return render(request, 'articles/media_confirm_delete.html', {'media': media})

# URL pattern:
# path('medias/delete/<int:pk>/', media_delete, name='media_delete')



def slider_list(request):
    sliders = Slider.objects.all()
    return render(request, 'sliders/slider_list.html', {'sliders': sliders})

def slider_create(request):
    if request.method == 'POST':
        form = SliderForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('slider_list')
    else:
        form = SliderForm()
    return render(request, 'sliders/slider_form.html', {'form': form})


@login_required
def even_create(request):
    if request.method == 'POST':
        form = EvenForm(request.POST)
        if form.is_valid():
            even = form.save(commit=False)
            even.user = request.user
            even.save()
            return redirect('articles:article_list')
    else:
        form = EvenForm()
    return render(request, 'articles/even_form.html', {'form': form})


@login_required
def even_update(request, pk):
    even = get_object_or_404(Even, pk=pk)
    if request.method == 'POST':
        form = EvenForm(request.POST, instance=even)
        if form.is_valid():
            form.save()
            return redirect('even_list')
    else:
        form = EvenForm(instance=even)
    return render(request, 'articles/even_form.html', {'form': form})

@login_required
def even_delete(request, pk):
    even = get_object_or_404(Even, pk=pk)
    if request.method == 'POST':
        even.delete()
        return redirect('even_list')
    return render(request, 'articles/even_confirm_delete.html', {'even': even})

def even_list(request):
    even_items = Even.objects.all()
    return render(request, 'articles/even_list.html', {'even_items': even_items})