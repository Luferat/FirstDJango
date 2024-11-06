from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'chat/index.html')

def about(request):
    print('\n\n\n', request, '\n\n\n')
    return render(request, 'chat/about.html')

def contact(request):
    return render(request, 'chat/contacts.html')