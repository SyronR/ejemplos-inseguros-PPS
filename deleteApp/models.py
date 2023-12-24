from django import forms


class DeleteUserForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario')
