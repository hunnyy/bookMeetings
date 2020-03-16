from rest_framework import serializers
from .models import CompanyRegister, RoomAdd, HrLogin, EventAdd

class AddcompSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = CompanyRegister
		fields = ('name', 'Credits', 'DefaultCredits', 'Property')

class RoomaddSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = RoomAdd
		fields = ('Roomname', 'CreditsPerHr', 'Capacity', 'Property')

class HrLoginSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = HrLogin
		fields = ('Company', 'Name', 'Email')

class EventAddSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = EventAdd
		fields = ('Title', 'Event_description', 'Event_sponsor', 'Event_location', 'Event_date')