from django import template

register = template.Library()

@register.filter
def youtube_embed_url(url):
    # Extraire l'ID de la vidéo de l'URL
    if 'youtube.com/watch?v=' in url:
        video_id = url.split('youtube.com/watch?v=')[-1].split('&')[0]
    elif 'youtu.be/' in url:
        video_id = url.split('youtu.be/')[-1].split('?')[0]
    else:
        return url
    return f'https://www.youtube.com/embed/{video_id}'
