from django.shortcuts import render
from django.shortcuts import render, redirect
from .forms import CadastroForm

# Create your views here.


def index(request):
    return render(request, 'chat/index.html')


def about(request):

    return render(request, 'chat/about.html')


def contact(request):
    return render(request, 'chat/contacts.html')


def cadastro(request):
    if request.method == 'POST':
        form = CadastroForm(request.POST)
        if form.is_valid():
            form_data = form.cleaned_data
            print('\n\n\n', form_data, '\n\n\n')
            return redirect('success')
    else:
        form = CadastroForm()

    return render(request, 'chat/cadastro.html', {'form': form, 'titulo': 'Cadastre-se'})


def success(request):
    return render(request, 'chat/success.html')
