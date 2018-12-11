import datetime

from django.http import HttpResponse
from django.shortcuts import render

from .query import get_rides
from .worker import RideProducer


def produce_rides(request):
    """
        Creates rides as Kafka topics
    """
    # Create 5 rides ? maybe
    RideProducer()
    return HttpResponse('Success', status=200)


def visualize(request):
    latitude = 40.71319580078125
    longitude = -73.81006622314453
    # 2014-01-01T03:25:07Z"
    pickup_time = datetime.datetime(2014, 1, 1, 3, 25, 7)
    rides = get_rides(0.02, 0.02, 10, latitude, longitude, pickup_time)
    print(rides)
    return render(request, 'uber/ride_map.html')


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
