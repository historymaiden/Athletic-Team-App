# Create your views here.

from roster.models import Teams, Player
from django.shortcuts import render, render_to_response, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

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
    tempteams = Teams.objects.get(id=pk) #return name of team clicked on
    tempteams = tempteams.players.all() #
    team = get_object_or_404(Player, id=pk) #get all teams
    teamName = get_object_or_404(Teams, id=pk)
    coach = get_object_or_404(Teams, id=pk)
    gender = get_object_or_404(Teams, id=pk)
    context = {
        'teamList': tempteams,
        'team': team,
        'teamname': teamName,
        'gender': gender,
        'coaches':coach,
    }
    return render(request, "roster/teamRoster.html", context)

def players(request, pk): #shows player bio
   # tempplayers = Player.objects.get(id=pk)
    tempplayers = Player.objects.get(id=pk)
    players = get_object_or_404(Player, id=pk)
    teamName = get_object_or_404(Teams, id=pk)
    gender = get_object_or_404(Teams, id=pk)
    images = get_object_or_404(Player, id=pk)
    context = {
        'tempplayers':tempplayers,
        'players':players,
        'teamname': teamName,
        'gender': gender,
        'images': images,
    }
    return render(request, "roster/players.html", context)
