from django.shortcuts import render
from .models import Hero, Event, Direction, Facility, Story, Giftregistry

# Create your views here.
def	home(request):
	if request.method == 'POST':
		return
	else:
		events=Event.objects.all()
		directions=Direction.objects.all()
		facilities=Facility.objects.order_by('event')
		stories=Story.objects.all()
		registry=Giftregistry.objects.all()
		for info in Hero.objects.all():
			context = {'bride':info.bride_nick,
					'groom':info.groom_nick,
					'wed_date':info.wedin_date,
					'slogan':info.slogan,
					'events':events,
					'directions':directions,
					'facilities':facilities,
					'stories':stories,
					'registry':registry}
		return render(request,'home.html',context)