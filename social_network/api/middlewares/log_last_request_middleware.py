from ..services.user_service import UserService


class LogLastRequestMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if request.user.is_authenticated:
            UserService.update_last_user_request_date(user=request.user)
        return response

