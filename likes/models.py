from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

class Like(models.Model):
    """
    Like model, related to User and Post.
    A user can like a post only once.
    """
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='likes'
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        unique_together = ['owner', 'post']  # Ensures a user can like a post only once

    def __str__(self):
        return f'{self.owner} liked {self.post}'
