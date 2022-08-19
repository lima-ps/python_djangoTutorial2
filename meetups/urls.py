
from django.urls import path
from . import views

urlpatterns = [ #nessa lista indicaremos todas as urls do nosso site e as views que serão executadas para cada uma
    path('', views.index, name='all-meetups'), #path tem dois argumentos mínimos: 1. o caminho(url) e 2. a função no ficheiro views que será requisitada.
                                                        #name é um indicador unico do caminho, que pode ser usado como referencia nas outras paginas 
    path('<slug:meetup_slug>/success', views.confirm_registration, name='confirm-ragistration'),                                                        
    path('<slug:meetup_slug>', views.meetup_details, name='meetup-detail'),  #esse é um caminho(url) dinamico, pois o slug altera de acordo com qual item eu escolho na view
]