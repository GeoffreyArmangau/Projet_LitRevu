from django import forms
from .models import Ticket

class TicketForm(forms.ModelForm):
    class Meta:
        model = Ticket
        fields = ['title', 'description', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Titre du ticket'}),
            'description': forms.Textarea(attrs={'placeholder': 'Décris ta demande'}),
        }
