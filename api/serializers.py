from rest_framework import serializers
from api.models import Profile


class ProfielSerializer(serializers.ModelSerializer):
    class Meta : 
        model = Profile
        fields = "__all__"