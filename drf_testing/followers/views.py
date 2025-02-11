from rest_framework import generics, permissions, serializers
from .models import Follower
from .serializers import FollowerSerializer
from drf_testing.permissions import IsOwnerOrReadOnly

class FollowerList(generics.ListCreateAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        # Ensure the follower is only created if the user isn't already following the target user
        owner = self.request.user
        followed = serializer.validated_data['followed']
        if Follower.objects.filter(owner=owner, followed=followed).exists():
            raise serializers.ValidationError("You are already following this user.")
        serializer.save(owner=owner)

class FollowerDetail(generics.RetrieveDestroyAPIView):
    serializer_class = FollowerSerializer
    queryset = Follower.objects.all()
    permission_classes = [IsOwnerOrReadOnly]