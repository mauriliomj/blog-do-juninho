from src.infrastructure.models import PostModel

class PostService:
    @staticmethod
    def create_post(title: str, content: str, author):
        return PostModel.objects.create(title=title, content=content, author=author)

    @staticmethod
    def get_all_posts():
        return PostModel.objects.all()

    @staticmethod
    def get_post_by_id(post_id: int):
        return PostModel.objects.filter(id=post_id).first()

    @staticmethod
    def update_post(post_id: int, title: str, content: str):
        post = PostModel.objects.filter(id=post_id).first()
        if post:
            post.title = title
            post.content = content
            post.save()
        return post

    @staticmethod
    def delete_post(post_id: int):
        post = PostModel.objects.filter(id=post_id).first()
        if post:
            post.delete()
            return True
        return False
