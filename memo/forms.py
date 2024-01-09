from django import forms
import datetime
from .models import Memoire, Niveau, Utilisateur, Etudiant, Enseignant, Specialite
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm



class NiveauForm:
    class Meta:
        model = Niveau
        fields = ['libelle', 'specialite']

class MemoireForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(MemoireForm, self).__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field.widget, forms.CheckboxInput) or isinstance(field.widget, forms.ChoiceField):
                field.widget.attrs['class'] = 'form-check-input'
            elif isinstance(field.widget, forms.Select):
                field.widget.attrs['class'] = 'form-select'
            else:
                field.widget.attrs['class'] = 'form-control'


    class Meta:
        model = Memoire
        fields = '__all__'

## creation des formulaires de creation de compte etudiant et enseignant 
        
class UtilisateurCreationForm(UserCreationForm):
    class Meta:
        model = Utilisateur
        fields = ('username', 'password1', 'password2', 'date_naiss', 'telephone', 'adresse')

class EtudiantCreationForm(forms.ModelForm):
    class Meta:
        model = Etudiant
        fields = ('specialite', 'num_etudiant')

class EnseignantCreationForm(forms.ModelForm):
    class Meta:
        model = Enseignant
        fields = ('code_enseignant', 'matiere')

class ConnexionForm(AuthenticationForm):
    class Meta:
        model = Utilisateur
        fields = ['username', 'password']