from rest_framework import serializers, viewsets
from .models import Room
# determine which fields you want to export to api (from models)


class RoomSerializer(serializers.HyperlinkedModelSerializer):
    # register model interested in with meta data
    class Meta:
        #  connects this class to Room model in models.py
        model = Room
        # what fields we want to return from Room class: title, description, n_to, s_to, e_to, w_to
        fields = ("title", "description", "n_to", "s_to", "e_to", "w_to")

    # def create(self, validated_data):
    #     # import pdb; pdb.set_trace()
    #     user = self.context['request'].user
    #     # pass in validated data as keyword arguments (title description, n_to, s_to, e_to, w_to)
    #     room = Room.objects.create(user=user, **validated_data)
    #     return room

# define which rows you want to export to api (do this using viewsets)


class RoomViewSet(viewsets.ModelViewSet):
    # attach to RoomSerializer class above
    serializer_class = RoomSerializer
    # define what we want to return
    queryset = Room.objects.all()
    # queryset = Room.objects.none()

    # # Making sure user is logged in and gets their specific data
    # def get_queryset(self):
    #     # get user
    #     user = self.request.user
    #     # user is not logged in, return nothing
    #     if user.is_anonymous:
    #         return Room.objects.none()
    #     # user is logged in, filter objects displayed based on logged in user (grabbed out of the request)
    #     else:
    #         return Room.objects.filter(user=user)

 # had an error: class Room has no objects member
   # steps to resolve -
   # 1. pip install pylint-django
   # 2. command + shift + p => preferences: Configure Language specific settings => Python
   # 3. "python.linting.pylintArgs": ["--load-plugins=pylint_django", ]
