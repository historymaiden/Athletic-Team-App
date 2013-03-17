# Create your views here.

from roster.models import Teams, Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request):
    teamList = Teams.objects.all()
    mens = Teams.objects.filter(sportType__istartswith="m")
    womens = Teams.objects.filter(sportType__istartswith="w")
    context = {
        'mens': mens,
        'womens': womens, 
    }
    return render(request, "roster/home.html", context)

#def teams(request, pk):
    #course = Course.objects.order_by('?')[0]
 #   teamName = get_object_or_404(Teams, id=pk)
  #  return render(request, "roster/home.html", {'teamName': teamName})

def teamRoster(request, pk): #shows list of players
    tempteams = Teams.objects.get(id=pk)
    tempteams = tempteams.players.all()
    team = get_object_or_404(Teams, id=pk)
    context = {
        'teamList': tempteams,
        'team': team,
    }
    return render(request, "roster/teamRoster.html", context)

def players(request, pk): #shows player bio
   # tempplayers = Player.objects.get(id=pk)
    tempplayers = Player.objects.filter(sport__istartswith="T")
    players = get_object_or_404(Player, id=pk)
    context = {
        'playerList':tempplayers,
        'players':players,
    }
    return render(request, "roster/players.html", context)
