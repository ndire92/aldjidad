from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Coordination, Membre, BureauNational, Commission, CommissionOrg, CommissionFem, CommissionCommu, CommissionCul, CommissionSocial, CommissionDecen, Secteur, Section

User = get_user_model()

class SignUpForm(UserCreationForm):
    username = forms.CharField(
        label='Utilisateur',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom d\'utilisateur'}),
        error_messages={'unique': "Ce nom d'utilisateur est déjà utilisé. Veuillez en choisir un autre."}
    )
    password1 = forms.CharField(
        label='Mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Mot de passe'}),
        error_messages={'min_length': "Le mot de passe doit contenir au moins 8 caractères.", 'password_entirely_numeric': "Le mot de passe ne peut pas être entièrement numérique."}
    )
    password2 = forms.CharField(
        label='Confirmer le mot de passe',
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Confirmer le mot de passe'}),
        error_messages={'password_mismatch': "Les mots de passe ne correspondent pas."}
    )
    role = forms.ChoiceField(
        choices=(('decideur', 'Décideur'), ('gestionnaire', 'Gestionnaire')),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Role'
    )

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'role')

    def clean_username(self):
        username = self.cleaned_data.get('username')
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise forms.ValidationError(self.fields['username'].error_messages['unique'])
        return username

    def clean_password1(self):
        password1 = self.cleaned_data.get('password1')
        if len(password1) < 8:
            raise forms.ValidationError(self.fields['password1'].error_messages['min_length'])
        if password1.isdigit():
            raise forms.ValidationError(self.fields['password1'].error_messages['password_entirely_numeric'])
        return password1

    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(self.fields['password2'].error_messages['password_mismatch'])
        return password2

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get('password1')
        if password1 and not any(char.isdigit() for char in password1):
            raise forms.ValidationError(self.fields['password1'].error_messages['password_entirely_numeric'])
        return cleaned_data

# forms.py
class CoordinationForm(forms.ModelForm):
    class Meta:
        model = Coordination
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
        }

class SectionForm(forms.ModelForm):
    class Meta:
        model = Section
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
        }

class SecteurForm(forms.ModelForm):
    class Meta:
        model = Secteur
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
        }


class MembreForm(forms.ModelForm):
    class Meta:
        model = Membre
        fields = '__all__'
        
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
      
        }


class BureauNationalForm(forms.ModelForm):
    class Meta:
        model = BureauNational
        fields = '__all__'
        
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }
    

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = '__all__'
        
        
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
      
        }


class CommissionOrgForm(forms.ModelForm):
    class Meta:
        model = CommissionOrg
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }

class CommissionFemForm(forms.ModelForm):
    class Meta:
        model = CommissionFem
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }

class CommissionCommuForm(forms.ModelForm):
    class Meta:
        model = CommissionCommu
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }

class CommissionCulForm(forms.ModelForm):
    class Meta:
        model = CommissionCul
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }

class CommissionSocialForm(forms.ModelForm):
    class Meta:
        model = CommissionSocial
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }

class CommissionDecenForm(forms.ModelForm):
    class Meta:
        model = CommissionDecen
        fields = '__all__'
        widgets = {
            'nom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'prenom': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'adresse': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'profession': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'fonction': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'mobile': forms.TextInput(attrs={'placeholder': '', 'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'coordination': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'secteur': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'section': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
            'commission': forms.Select(attrs={'style': 'border: 1px solid #557029; border-radius: 10px;', 'class': 'form-control'}),
           
      
        }

