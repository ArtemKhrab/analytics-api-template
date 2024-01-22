from ..models import Like


class LikeService:

    @staticmethod
    def _get_like(post, user):
        return Like.objects.filter(post=post, user=user).first()

    @staticmethod
    def create_like(post, user):
        like = LikeService._get_like(post, user)
        if like:
            return
        instance = Like(post=post, user=user)
        instance.save()

    @staticmethod
    def delete_like(post, user):
        like = LikeService._get_like(post, user)
        if like:
            like.delete()
