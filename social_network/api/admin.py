from .models import User
from .models import Like
from .models import Post

from django.contrib import admin


admin.site.register(User)
admin.site.register(Like)
admin.site.register(Post)
