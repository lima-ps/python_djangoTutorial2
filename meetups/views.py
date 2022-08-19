from urllib import request
from django.shortcuts import render, redirect
#from django.http import HttpResponse
from .models import Meetup, Participant
from .forms import RegistrationForm

# Create your views here.

def index(request):     #request é parametro obrigatorio pois irá ser passado automaticamente pelo Django
    #return HttpResponse('Hello word')  #retorna uma resposta para o browser indicando o que será mostrado na tela nessa view, quando uma url for requisitada
    
    '''meetups = [   #uso de dicionario pode ser chamado no render pela sua key
        {'title': 'A First Meetup','location': 'New York','slug': 'a-first-meetup'
        },  { 'title': 'A Second Meetup', 'location': 'Paris', 'slug': 'a-second-meetup'
        },
    ]'''

    meetups = Meetup.objects.all() #retorna todos os objetos do nosso modelo.

    return render(request, 'meetups/index.html', {
        'meetups': meetups
        #'show_meetups': True   #precisa de pelo menos dois argumentos. 1 o request trazido pela função e o ficheiro
    })

def meetup_details(request, meetup_slug): #meetup_slug vem do nome escolhido no path pasado no ficheiro 'url'
    
    """selected_meetups = {
        'title': 'A fisrt Meetup',
        'description': 'This is the fisrt meetup!'
    }"""

    try:
        selected_meetups = Meetup.objects.get(slug=meetup_slug)
        if request.method == 'GET': 
            registration_form = RegistrationForm()
           
        else:
            registration_form = RegistrationForm(request.POST)
            if registration_form.is_valid():
                #participants = registration_form.save()  #salva na base de dados, mas nesse caso daria erro se tentamos salvar duas vezes o mesmo mail, mesmo que pra meetups diferentes
                user_email = registration_form.cleaned_data['email']  #função que contem um dicionario
                participants, _ = Participant.objects.get_or_create(email=user_email) #aqui eu olho se o campo chave email na bd ja tem o mesmo user_email registado
                selected_meetups.participant.add(participants)  #add ao modelo relacionado FK
                return redirect('confirm-ragistration', meetup_slug=meetup_slug)  #redireciona pra outra pagina

        return render(request, 'meetups/meetup-details.html', {
            
            #'meetup_title': selected_meetups['title'],
                #'meetup_description': selected_meetups['description']""" #versão sem model, tirando direto do "dummy data" acima
                 #'meetup_title': selected_meetups.title,  //posso usar os atributos dos modelos de forma separados para usar na view diretamente
                 #'meetup_description': selected_meetups.description

                'meetup_found': True,
                'meetup': selected_meetups,    #ou posso apenas referenciar todo o objeto e puxar seus atributos nas views com dot notation
                'form': registration_form,
        })

    except Exception as exc:
        return render(request, 'meetups/meetup-details.html', {
            'meetup_found': False,
        })

def confirm_registration(request, meetup_slug): #parametro vindo da url.
    meetup = Meetup.objects.get(slug=meetup_slug)
    return render(request, 'meetups/registration-success.html', {
        'organizer_email': meetup.organizer_email
    })