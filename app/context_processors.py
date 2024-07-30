from .models import Membre, Coordination, Section

def statistics(request):
    total_membres = Membre.objects.count()
    total_coordinations = Coordination.objects.count()
    total_sections = Section.objects.count()

    return {
        'total_membres': total_membres,
        'total_coordinations': total_coordinations,
        'total_sections': total_sections,
    }
