from ..models import Post


class PostService:

    @staticmethod
    def get_all_posts():
        return Post.objects.all()

    @staticmethod
    def create_post(post_data, user):
        instance = Post(text=post_data["text"], user_id=user.id)
        instance.save()
        return instance

    @staticmethod
    def get_post_by_id(post_id):
        return Post.objects.filter(pk=post_id).first()
