from django.contrib import admin

from .models import Meetup, Location, Participant

# Register your models here.

class MeetupAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'location')  #altermos as configurações da página de admin do django
    list_filter = ('location', 'date')
    prepopulated_fields = {'slug': ('title', )} #o campo slug sera autopreenchido com o titulo

admin.site.register(Meetup, MeetupAdmin) #indicamos que nosso modelo será mostrado no painel admin com o formato espcificado na classe MeetupAdmin
admin.site.register(Location)
admin.site.register(Participant)