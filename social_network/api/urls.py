from .views.user_views import UserView
from .views.user_views import UserActivityView

from .views.login_views import LoginView

from .views.register_views import RegisterView

from .views.post_view import PostView
from .views.post_view import LikePostView
from .views.post_view import UnlikePostView

from .views.analytics_view import LikesAnalyticsView

from django.urls import path


urlpatterns = [
    path("v1/users/", UserView.as_view()),
    path("v1/user/activity", UserActivityView.as_view()),
    path("v1/analytics/", LikesAnalyticsView.as_view()),
    path("v1/login/", LoginView.as_view()),
    path("v1/register/", RegisterView.as_view()),
    path("v1/post/", PostView.as_view()),
    path("v1/post/<int:id>/like", LikePostView.as_view()),
    path("v1/post/<int:id>/unlike", UnlikePostView.as_view()),
]
