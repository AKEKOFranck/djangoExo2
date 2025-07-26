from django import forms
from django.contrib.auth import get_user_model

User = get_user_model()

class SignForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label="Mot de passe")
    
    class Meta:
        model = User 
        fields = ['username', 'last_name', 'age', 'password']
        help_texts = {
            'last_name': None,
            'username': None,
        }
    
   
        
        
        
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
    
    
    
    
class ModificationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'last_name', 'age']
        labels = {
            'username': "Nom d'utilisateur",
            'last_name': "Nom de famille",
        }