from rest_framework import serializers
from .models import Follower
from django.contrib.auth.models import User

class FollowerSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    followed_name = serializers.ReadOnlyField(source='followed.username')

    class Meta:
        model = Follower
        fields = ['owner', 'followed_name', 'created_at']

    def create(self, validated_data):
        owner = validated_data['owner']
        followed = validated_data['followed']
        
        # Check if the user is already following the followed user
        if Follower.objects.filter(owner=owner, followed=followed).exists():
            raise serializers.ValidationError("You are already following this user.")
        
        return Follower.objects.create(**validated_data)
