from django.db import models
from django.contrib.auth.models import AbstractUser




class User(AbstractUser):
    is_decideur = models.BooleanField(default=False)
    is_gestionnaire = models.BooleanField(default=False)
    is_visiteur = models.BooleanField(default=False)
    
    
    
    

    
class Coordination(models.Model):
    nom = models.CharField(max_length=100)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom

class Section(models.Model):
    nom = models.CharField(max_length=100)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom

class Secteur(models.Model):
    nom = models.CharField(max_length=100)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    # Ajoutez d'autres champs selon les besoins

    def __str__(self):
        return self.nom

class Membre(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nom} {self.prenom}"


class Commission(models.Model):
    nom = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.nom

class CommissionOrg(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
 
    # Add other fields as needed

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CommissionFem(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
 
    # Add other fields as needed

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CommissionCommu(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)

    # Add other fields as needed

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CommissionCul(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
   
    # Add other fields as needed

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CommissionSocial(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class CommissionDecen(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return f"{self.nom} {self.prenom}"

class BureauNational(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    adresse = models.CharField(max_length=200)
    profession = models.CharField(max_length=100)
    fonction = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    coordination = models.ForeignKey(Coordination, on_delete=models.CASCADE)
    secteur = models.ForeignKey(Secteur, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE)
    commission = models.ForeignKey(Commission, on_delete=models.CASCADE)
    # Add other fields as needed

    def __str__(self):
        return self.nom
