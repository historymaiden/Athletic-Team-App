# Create your views here.

from roster.models import Teams, Player
from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def home(request, pk):
    context = {
        'teamName': Teams.object.all()
    #mens = Teams.objects.filter(sportType__exact="mens")
    #womens = Teams.objects.filter(sportType__exact="womens")
    }
    return render(request, "roster/home.html", context)

#def teams(request, pk):
    #course = Course.objects.order_by('?')[0]
 #   teamName = get_object_or_404(Teams, id=pk)
  #  return render(request, "roster/home.html", {'teamName': teamName})

def teamRoster(request): #shows list of players
    player_list = Players.objects.all()
    paginator = Paginator(student_list, 25) #1st is what to pass in and 2nd is how many to show
    page = request.GET.get('page')
    #players = get_object_or_404(Player, id=pk)
    return render(request, "roster/teamRoster.html", {'players': players})

def players(request, pk): #shows player bio
    #course = Course.objects.order_by('?')[0]
    #name = request.GET['name']
    #try:
     #   student = Student.objects.filter(name__istartswith=name)[0]
    #except:
     #   return render(request, "roster/student.html", {'student': Student(), 'error_message': 'No student exists with the name ' + name})
    #else: 
     #   return render(request, "roster/student.html", {'student': student})
    players = get_object_or_404(TeamMember, id=pk)
    return render(request, "roster/players.html", {'players': players})
