from django.forms import ModelForm
from .models import Contact
from django import forms


class ContactForm(forms.ModelForm):
    first_name = forms.CharField(min_length=2, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Primer Nombre...', 'class': 'form-control'}))
    second_name = forms.CharField(max_length=25, required=False, widget=forms.TextInput(attrs={'placeholder': 'Segundo Nombre...', 'class': 'form-control'}))
    first_last_name = forms.CharField(min_length=2, max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Primer Apellido...', 'class': 'form-control'}))
    second_last_name = forms.CharField(max_length=25, widget=forms.TextInput(attrs={'placeholder': 'Segundo Apellido...', 'class': 'form-control'}))
    email_adress = forms.EmailField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Correo electrónico...', 'class': 'form-control'}))
    #number_prefix = forms.Select(widget=forms.Select(attrs={'placeholder': '+', 'class': 'form-select'}))
    phone_number = forms.CharField(max_length=9, widget=forms.TextInput(attrs={'placeholder': 'Número telefónico...', 'class': 'form-control'}))
    comment = forms.CharField(max_length=500,required= False, widget= forms.Textarea(attrs={'placeholder': 'Déjanos tu comentario...', 'class':'form-control'}))

    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'number_prefix': forms.Select(attrs={'placeholder': '+', 'class': "form-select"})
        }