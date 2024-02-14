from django import forms


class ContactForms(forms.Form):
    
    name = forms.CharField(label='Nome')
    email = forms.EmailField(label='E-mail')
    menssage = forms.CharField(label='Mesagem', widget=forms.Textarea)