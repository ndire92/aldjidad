from django.shortcuts import get_object_or_404, redirect, render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
from .models import BureauNational, Commission, Membre,Coordination, Secteur, Section
from .forms import BureauNationalForm, CommissionForm, CoordinationForm, MembreForm, SecteurForm,SignUpForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import PasswordChangeForm
from .models import CommissionOrg, CommissionFem, CommissionCommu, CommissionCul, CommissionSocial, CommissionDecen
from .forms import CommissionOrgForm, CommissionFemForm, CommissionCommuForm, CommissionCulForm, CommissionSocialForm, CommissionDecenForm,SectionForm
from django.contrib.auth.decorators import user_passes_test

from django.contrib import messages

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)

            role = form.cleaned_data.get('role')

            if role == 'decideur':
                user.is_decideur = True
            elif role == 'gestionnaire':
                user.is_gestionnaire = True

            user.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            if user and user.is_authenticated:
                # Login successful
                return redirect('login')

    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            if user.is_gestionnaire:
                messages.success(request, 'login successful!')
                return redirect('articles:article_create')
            elif user.is_decideur:
                messages.success(request, 'login successful!')
                return redirect('articles:article_create')
            else:
                messages.success(request, 'login successful!')
                return redirect('membre_stats')
        else:
            messages.error(request, 'Error! Please check your login and password')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('articles:article_list')  # Assurez-vous que 'home' ne redirige pas vers /logout/
def is_admin(user):
    return user.is_authenticated and user.is_staff


def permission_denied_view(request):
    messages.error(request, "Vous devez être administrateur pour accéder à cette page.")
    return redirect('login')

def liste_membres(request):
    membres_list = Membre.objects.all()
    count = membres_list.count()  # Nombre total d'enregistrements
    paginator = Paginator(membres_list,5)  # Paginate par 20 membres par page

    page = request.GET.get('page')
    try:
        membres = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        membres = paginator.page(1)
    except EmptyPage:
        # Si la page est en dehors de la plage de résultats, affichez la dernière page de résultats
        membres = paginator.page(paginator.num_pages)

    return render(request, 'liste_membres.html', {'membres': membres,'count': count})

def ajouter_membre(request):
    if request.method == 'POST':
        form = MembreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm()
    return render(request, 'ajouter_membre.html', {'form': form})

def update_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        form = MembreForm(request.POST, instance=membre)
        if form.is_valid():
            form.save()
            return redirect('liste_membres')
    else:
        form = MembreForm(instance=membre)
    return render(request, 'update_membre.html', {'form': form})

def delete_membre(request, pk):
    membre = get_object_or_404(Membre, pk=pk)
    if request.method == 'POST':
        membre.delete()
        return redirect('liste_membres')
    return render(request, 'delete_membre.html', {'membre': membre})

@user_passes_test(is_admin, login_url='permission_denied')
def coordination_form(request):
    if request.method == 'POST':
        form = CoordinationForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers une autre page après avoir enregistré la coordination
            return redirect('liste_structure')
    else:
        form = CoordinationForm()
    return render(request, 'coordination_form.html', {'form': form})

def coordi(request):
    coord_list = Coordination.objects.all()
    
    count = coord_list.count()  # Nombre total d'enregistrements
    paginator = Paginator(coord_list,5)  # Paginate par 20 membres par page

    page = request.GET.get('page')
    try:
        coordination = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        coordination = paginator.page(1)
    except EmptyPage:
        # Si la page est en dehors de la plage de résultats, affichez la dernière page de résultats
        coordination = paginator.page(paginator.num_pages)

    return render(request, 'liste_coord.html', {'coordination': coordination,'count': count})
#section
@user_passes_test(is_admin, login_url='permission_denied')
def section_form(request):
    if request.method == 'POST':
        form = SectionForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers une autre page après avoir enregistré la coordination
            return redirect('liste_sections')
    else:
        form = SectionForm()
    return render(request, 'section_form.html', {'form': form})

def section_list(request):
    sect_list = Section.objects.all()
    
    count = sect_list.count()  # Nombre total d'enregistrements
    paginator = Paginator(sect_list, 5)  # Paginate par 5 sections par page

    page = request.GET.get('page')
    try:
        section = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        section = paginator.page(1)
    except EmptyPage:
        # Si la page est en dehors de la plage de résultats, affichez la dernière page de résultats
        section = paginator.page(paginator.num_pages)

    return render(request, 'liste_section.html', {'section': section, 'count': count})

@user_passes_test(is_admin, login_url='permission_denied')
def secteur_form(request):
    if request.method == 'POST':
        form = SecteurForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers une autre page après avoir enregistré la coordination
            return redirect('liste_secteurs')
    else:
        form = SecteurForm()
    return render(request, 'secteur_form.html', {'form': form})


def secteur_list(request):
    sect_list = Secteur.objects.all()
    
    count = sect_list.count()  # Nombre total d'enregistrements
    paginator = Paginator(sect_list, 5)  # Paginate par 5 secteurs par page

    page = request.GET.get('page')
    try:
        secteurs = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        secteurs = paginator.page(1)
    except EmptyPage:
        # Si la page est en dehors de la plage de résultats, affichez la dernière page de résultats
        secteurs = paginator.page(paginator.num_pages)

    return render(request, 'liste_secteur.html', {'secteurs': secteurs, 'count': count})


def combined_list(request):
    coordinations = Coordination.objects.all()
    sections = Section.objects.all()
    secteurs = Secteur.objects.all()

    # Créez une liste combinée
    combined_data = []

    for coordination in coordinations:
        coord_sections = sections.filter(coordination=coordination)
        for section in coord_sections:
            sect_secteurs = secteurs.filter(section=section)
            for secteur in sect_secteurs:
                combined_data.append({
                    'coordination_nom': coordination.nom,
                    'section_nom': section.nom,
                    'secteur_nom': secteur.nom,
                })

    return render(request, 'combined_list.html', {'combined_data': combined_data})




@user_passes_test(is_admin, login_url='permission_denied')
def bureau_form(request):
    if request.method == 'POST':
        form = BureauNationalForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_bureau_national')  # Rediriger après enregistrement
    else:
        form = BureauNationalForm()
    return render(request, 'bureau.html', {'form': form})

def list_bureau_national(request):
    bureaus = BureauNational.objects.all()
    paginator = Paginator(bureaus, 5)  # Nombre d'instances par page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'list_bureau_national.html', {'page_obj': page_obj})

@user_passes_test(is_admin, login_url='permission_denied')
def update_bureau_national(request, pk):
    bureau = get_object_or_404(BureauNational, pk=pk)
    if request.method == 'POST':
        form = BureauNationalForm(request.POST, instance=bureau)
        if form.is_valid():
            form.save()
            return redirect('list_bureau_national')
    else:
        form = BureauNationalForm(instance=bureau)
    return render(request, 'update_bureau_national.html', {'form': form})

@user_passes_test(is_admin, login_url='permission_denied')
def delete_bureau_national(request, pk):
    bureau = get_object_or_404(BureauNational, pk=pk)
    if request.method == 'POST':
        bureau.delete()
        return redirect('list_bureau_national')
    return render(request, 'delete_bureau_national.html', {'bureau': bureau})


@user_passes_test(is_admin, login_url='permission_denied')
def commission_form(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            # Rediriger vers une autre page après avoir enregistré la coordination
    else:
        form = CommissionForm()
    return render(request, 'commission.html', {'form': form})




def coordi(request):
    coord_list = Coordination.objects.all()
    count = coord_list.count()  # Nombre total d'enregistrements
    paginator = Paginator(coord_list,5)  # Paginate par 20 membres par page

    page = request.GET.get('page')
    try:
        coordination = paginator.page(page)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, affichez la première page
        coordination = paginator.page(1)
    except EmptyPage:
        # Si la page est en dehors de la plage de résultats, affichez la dernière page de résultats
        coordination = paginator.page(paginator.num_pages)

    return render(request, 'liste_coord.html', {'coordination': coordination,'count': count})





def commission_list(request):
    commissions = Commission.objects.all()
    return render(request, 'commission_list.html', {'commissions': commissions})


@user_passes_test(is_admin, login_url='permission_denied')
def commission_create(request):
    if request.method == 'POST':
        form = CommissionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('commission_list')
    else:
        form = CommissionForm()
    return render(request, 'commission.html', {'form': form})

@user_passes_test(is_admin, login_url='permission_denied')
def commission_update(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        form = CommissionForm(request.POST, instance=commission)
        if form.is_valid():
            form.save()
            return redirect('commission_list')
    else:
        form = CommissionForm(instance=commission)
    return render(request, 'commission.html', {'form': form})

@user_passes_test(is_admin, login_url='permission_denied')
def commission_delete(request, pk):
    commission = get_object_or_404(Commission, pk=pk)
    if request.method == 'POST':
        commission.delete()
        return redirect('commission_list')
    return render(request, 'commission_confirm_delete.html', {'commission': commission})

@user_passes_test(is_admin, login_url='permission_denied')
def create_commission_org(request):
    if request.method == 'POST':
        form = CommissionOrgForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commission_org')  # Redirigez vers une page de succès après l'ajout
    else:
        form = CommissionOrgForm()
    return render(request, 'create_commission_org.html', {'form': form})

def list_commission_org(request):
    commissions = CommissionOrg.objects.all()
    
    paginator = Paginator(commissions, 5)  # Paginate par 5 enregistrements par page
    page = request.GET.get('page')
    try:
        commissions = paginator.page(page)
    except PageNotAnInteger:
        commissions = paginator.page(1)
    except EmptyPage:
        commissions = paginator.page(paginator.num_pages)
    return render(request, 'list_commission_org.html', {'commissions': commissions})

@user_passes_test(is_admin, login_url='permission_denied')
def update_commission_org(request, pk):
    commission = get_object_or_404(CommissionOrg, pk=pk)
    if request.method == 'POST':
        form = CommissionOrgForm(request.POST, instance=commission)
        if form.is_valid():
            form.save()
            return redirect('list_commission_org')
    else:
        form = CommissionOrgForm(instance=commission)
    return render(request, 'create_commission_org.html', {'form': form})


@user_passes_test(is_admin, login_url='permission_denied')
def delete_commission_org(request, pk):
    commission = get_object_or_404(CommissionOrg, pk=pk)
    if request.method == 'POST':
        commission.delete()
        return redirect('list_commission_org')
    return render(request, 'delete_commission_org.html', {'commission': commission})


@user_passes_test(is_admin, login_url='permission_denied')
def create_commission_fem(request):
    if request.method == 'POST':
        form = CommissionFemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commission_fem')  # Nom d'URL correct
    else:
        form = CommissionFemForm()
    return render(request, 'create_commission_fem.html', {'form': form})

def list_commission_fem(request):
    commissionfem = CommissionFem.objects.all()
    paginator = Paginator(commissionfem, 5)  # Paginate par 5 enregistrements par page
    page = request.GET.get('page')
    try:
        commissions = paginator.page(page)
    except PageNotAnInteger:
        commissions = paginator.page(1)
    except EmptyPage:
        commissions = paginator.page(paginator.num_pages)
    return render(request, 'list_commission_fem.html', {'commissions': commissions})



@user_passes_test(is_admin, login_url='permission_denied')
def update_commission_fem(request, pk):
    commissionfem = get_object_or_404(CommissionFem, pk=pk)
    if request.method == 'POST':
        form = CommissionFemForm(request.POST, instance=commissionfem)
        if form.is_valid():
            form.save()
            return redirect('list_commission_fem')  # Nom d'URL correct
    else:
        form = CommissionFemForm(instance=commissionfem)
    return render(request, 'create_commission_fem.html', {'form': form})


@user_passes_test(is_admin, login_url='permission_denied')
def delete_commission_fem(request, pk):
    commissionfem = get_object_or_404(CommissionFem, pk=pk)
    if request.method == 'POST':
        commissionfem.delete()
        return redirect('list_commission_fem')  # Nom d'URL correct
    return render(request, 'delete_commission_fem.html', {'commissionfem': commissionfem})


@user_passes_test(is_admin, login_url='permission_denied')
def create_commission_commu(request):
    if request.method == 'POST':
        form = CommissionCommuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commission_commu')  
    else:
        form = CommissionCommuForm()
    return render(request, 'create_commission_commu.html', {'form': form})

def list_commission_commu(request):
    commissioncomm = CommissionCommu.objects.all()
    paginator = Paginator(commissioncomm, 3)  # Paginate par 5 enregistrements par page
    page = request.GET.get('page')
    try:
        commissioncomm = paginator.page(page)
    except PageNotAnInteger:
        commissioncomm = paginator.page(1)
    except EmptyPage:
        commissioncomm = paginator.page(paginator.num_pages)
    
    return render(request, 'list_commission_commu.html', {'commissioncomm': commissioncomm})




@user_passes_test(is_admin, login_url='permission_denied')
def update_commission_commu(request, pk):
    commissioncomm = get_object_or_404(CommissionCommu, pk=pk)
    if request.method == 'POST':
        form = CommissionCommuForm(request.POST, instance=commissioncomm)
        if form.is_valid():
            form.save()
            return redirect('list_commission_commu')
    else:
        form = CommissionCommuForm(instance=commissioncomm)
    return render(request, 'create_commission_commu.html', {'form': form})


@user_passes_test(is_admin, login_url='permission_denied')
def delete_commission_commu(request, pk):
    commissioncomm = get_object_or_404(CommissionCommu, pk=pk)
    if request.method == 'POST':
        commissioncomm.delete()
        return redirect('list_commission_commu')
    return render(request, 'delete_commission_commu.html', {'commissioncomm': commissioncomm})


@user_passes_test(is_admin, login_url='permission_denied')
def create_commission_cul(request):
    if request.method == 'POST':
        form = CommissionCulForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commission_cul')  # Rediriger vers la liste après la création
    else:
        form = CommissionCulForm()
    return render(request, 'create_commission_cul.html', {'form': form})

def list_commission_cul(request):
    commissioncul = CommissionCul.objects.all()
    paginator = Paginator(commissioncul, 5)  # Paginate par 5 enregistrements par page
    page = request.GET.get('page')
    try:
        commissioncul = paginator.page(page)
    except PageNotAnInteger:
        commissioncul = paginator.page(1)
    except EmptyPage:
        commissioncul = paginator.page(paginator.num_pages)
    return render(request, 'list_commission_cul.html', {'commissioncul': commissioncul})

@user_passes_test(is_admin, login_url='permission_denied')
def update_commission_cul(request, pk):
    commissioncul = get_object_or_404(CommissionCul, pk=pk)
    if request.method == 'POST':
        form = CommissionCulForm(request.POST, instance=commissioncul)
        if form.is_valid():
            form.save()
            return redirect('list_commission_cul')
    else:
        form = CommissionCulForm(instance=commissioncul)
    return render(request, 'create_commission_cul.html', {'form': form})

@user_passes_test(is_admin, login_url='permission_denied')
def delete_commission_cul(request, pk):
    commissioncul = get_object_or_404(CommissionCul, pk=pk)
    if request.method == 'POST':
        commissioncul.delete()
        return redirect('list_commission_cul')
    return render(request, 'delete_commission_cul.html', {'commissioncul': commissioncul})



@user_passes_test(is_admin, login_url='permission_denied')
def create_commission_social(request):
    if request.method == 'POST':
        form = CommissionSocialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commission_social')  
    else:
        form = CommissionSocialForm()
    return render(request, 'create_commission_social.html', {'form': form})

def list_commission_social(request):
    commissionsocial = CommissionSocial.objects.all()
    paginator = Paginator(commissionsocial, 5)  # Paginate par 5 enregistrements par page
    page = request.GET.get('page')
    try:
        commissionsocial = paginator.page(page)
    except PageNotAnInteger:
        commissionsocial = paginator.page(1)
    except EmptyPage:
       commissionsocial = paginator.page(paginator.num_pages)
    
    return render(request, 'list_commission_social.html', {'commissionsocial': commissionsocial})




@user_passes_test(is_admin, login_url='permission_denied')
def update_commission_social(request, pk):
    commissionsocial = get_object_or_404(CommissionSocial, pk=pk)
    if request.method == 'POST':
        form = CommissionSocialForm(request.POST, instance=commissionsocial)
        if form.is_valid():
            form.save()
            return redirect('list_commission_social')
    else:
        form = CommissionSocialForm(instance=commissionsocial)
    return render(request, 'create_commission_social.html', {'form': form})



@user_passes_test(is_admin, login_url='permission_denied')
def delete_commission_social(request, pk):
    commissionsocial = get_object_or_404(CommissionSocial, pk=pk)
    if request.method == 'POST':
        commissionsocial.delete()
        return redirect('list_commission_social')
    return render(request, 'delete_commission_social.html', {'commissionsocial': commissionsocial})




@user_passes_test(is_admin, login_url='permission_denied')
def create_commission_decen(request):
    if request.method == 'POST':
        form = CommissionDecenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('list_commission_decen')  
    else:
        form = CommissionDecenForm()
    return render(request, 'create_commission_decen.html', {'form': form})


def list_commission_decen(request):
    commissionde = CommissionDecen.objects.all()
    paginator = Paginator(commissionde, 5)  # Paginate par 5 enregistrements par page
    page = request.GET.get('page')
    try:
        commissionde = paginator.page(page)
    except PageNotAnInteger:
        commissionde = paginator.page(1)
    except EmptyPage:
        commissionde = paginator.page(paginator.num_pages)
    return render(request, 'list_commission_decen.html', {'commissionde': commissionde})

@user_passes_test(is_admin, login_url='permission_denied')
def update_commission_decen(request, pk):
    commissionde = get_object_or_404(CommissionDecen, pk=pk)
    if request.method == 'POST':
        form = CommissionDecenForm(request.POST, instance=commissionde)
        if form.is_valid():
            form.save()
            return redirect('list_commission_decen')
    else:
        form = CommissionDecenForm(instance=commissionde)
    return render(request, 'create_commission_decen.html', {'form': form})


@user_passes_test(is_admin, login_url='permission_denied')
def delete_commission_decen(request, pk):
    commissionde = get_object_or_404(CommissionDecen, pk=pk)
    if request.method == 'POST':
        commissionde.delete()
        return redirect('list_commission_decen')
    return render(request, 'delete_commission_decen.html', {'commissionde': commissionde})



def membre_stats(request):
    
    
    return render(request, 'membre_stats.html')
def admin(request):
    
    
    return render(request, 'administrateur.html')

