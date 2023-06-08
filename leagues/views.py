from django.shortcuts import render, redirect
from .models import League, Team, Player
from . import team_maker


def index(request):
	context = {
		"leagues": League.objects.all(),
		"Baseball_leagues": League.objects.filter(sport="Baseball"),
		"Women_leagues": League.objects.filter(name__contains="Women"),
		"Hockey_leagues": League.objects.filter(sport__contains="Hockey"),
		"Not_Football_leagues": League.objects.exclude(sport="Football"),
		"Conference_leagues": League.objects.filter(name__contains="conference"),
		"Atlantic_leagues": League.objects.filter(name__contains="Atlantic"),

		"teams": Team.objects.all(),
		"dallas_teams": Team.objects.filter(location__contains="Texas"),
		"raptors_teams": Team.objects.filter(team_name__contains="Raptors"),
		"city_teams": Team.objects.filter(location__contains="City"),
		"startwith_teams": Team.objects.filter(team_name__startswith="T"),
		"teams_order_location": Team.objects.order_by('location'),
		"teams_order_name_reverse": Team.objects.order_by('-team_name'),

		"players": Player.objects.all(),
		"players_cooper": Player.objects.filter(last_name="Cooper"),
		"players_joshua": Player.objects.filter(first_name="Joshua"),
		"players_cooper_no_joshua": Player.objects.filter(last_name="Cooper").exclude(first_name="Joshua"),
		"players_alexander_ayatt": Player.objects.filter(first_name__in=["Alexander", "Wyatt"]),
	}
	return render(request, "leagues/index.html", context)


def make_data(request):
	team_maker.gen_leagues(10)
	team_maker.gen_teams(50)
	team_maker.gen_players(200)

	return redirect("index")