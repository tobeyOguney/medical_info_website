from rest_framework import serializers
from .models import User

class UserSerializer(serializers.ModelSerializer):
	class Meta:
	    model = User
	    fields = [
			'id', 'first_name', 'last_name', 'age', 'sex',
			'blood_type', 'genotype', 'AIDS_status', 'malaria_status',
			'ebola_status', 'COVID19_status',
		]
