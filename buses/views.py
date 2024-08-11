from django.shortcuts import render

# Create your views here.
def businfo(request):
    d={'routes':[{'id':'bus1','area':'dharmavaram',},
    {'id':'bus2','area':'atp'},
    {'id':'bus3','area':'bks'},
    {'id':'bus4','area':'tdp'},
    {'id':'bus5','area':'singanamala'}]}
    return render(request,'info.html',d)