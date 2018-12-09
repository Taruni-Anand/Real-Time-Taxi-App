from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from .worker import RideProducer


def produce_rides(request):
    """
        Creates rides as Kafka topics
    """
    # Create 5 rides ? maybe
    RideProducer()
    return HttpResponse('Success', status=200)


def visualize(request):
    return render(request, 'uber/ride_map.html')


def default_map(request):
    mapbox_access_token = 'pk.my_mapbox_access_token'
    return render(request, 'default.html',
                  {'mapbox_access_token': mapbox_access_token})


# def consume_rides(request):
#     RideConsumer()
#     return HttpResponse('Success', status=200)


# def ride_list(request):
#     rides = Ride.objects.filter(ride_date__lte=timezone.now()).order_by('ride_date')
#     return render(request, 'uber/ride_list.html', {'rides': rides})
#
#
# def ride_detail(request,pk):
#     ride = get_object_or_404(Ride, pk=pk)
#     return render(request, 'uber/ride_detail.html')
