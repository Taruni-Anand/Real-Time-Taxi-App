from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Ride

def ride_list(request):
    rides = Ride.objects.filter(ride_date__lte=timezone.now()).order_by('ride_date')
    return render(request, 'uber/ride_list.html', {'rides': rides})

def ride_detail(request,pk):
    ride = get_object_or_404(Ride, pk=pk)
    return render(request, 'uber/ride_detail.html')
