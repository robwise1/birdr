from django.shortcuts import render

# Create your views here.
def station_view(request):
    return render(request, 'stations/stations.html', {})