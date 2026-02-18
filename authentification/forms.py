from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password

User = get_user_model()

class CustomSignupForm(forms.Form):
    username = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={'placeholder': "Nom d'utilisateur"}),
        label=''
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "Mot de passe"}),
        label=''
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(attrs={'placeholder': "Confirmer mot de passe"}),
        label=''
    )

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise forms.ValidationError("Ce nom d'utilisateur existe déjà.")
        return username

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        if password1 and password2:
            if password1 != password2:
                self.add_error('password2', "Les mots de passe ne correspondent pas.")
            else:
                validate_password(password1)
        return cleaned_data
