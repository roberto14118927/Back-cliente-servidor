from rest_framework import routers, serializers, viewsets

from Profile.models import Profile

class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ('id','user','name')