from django.db import models
from django.conf import settings


class Like(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="user_likes"
    )
    post = models.ForeignKey(
        "Post", on_delete=models.CASCADE, related_name="post_likes"
    )
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ('user', 'post')
