"""AirQuality Views."""

from django.shortcuts import render

def dashboard(request, *args, **kwargs):
    return render(request, 'index.html')


def air_quality(request, *args, **kwargs):
    year = kwargs.get('year', None)
    context = {
        'year': year
    }
    return render(request, 'graph.html', context)
