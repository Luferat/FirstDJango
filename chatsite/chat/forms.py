from django import forms


class CadastroForm(forms.Form):
    email = forms.EmailField(label='Email', max_length=100)
    nascimento = forms.DateField(
        label='Data de Nascimento',
        widget=forms.DateInput(attrs={'type': 'date'})
    )
    nome = forms.CharField(label='Nome', max_length=100)
    senha = forms.CharField(label='Senha', widget=forms.PasswordInput())
