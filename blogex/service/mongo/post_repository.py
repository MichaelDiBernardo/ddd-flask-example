import datetime
from pymongo import DESCENDING

from models import Post
from service.mongo import mongo_repository_base
from service.utils import get_from_obj_or_direct

class PostRepository(mongo_repository_base.RepositoryBase):
    class Meta:
        model = Post
        collection_name = "posts"

    def create(self, post):
        post.author = get_from_obj_or_direct(post.author, "username")
        post.post_date = datetime.datetime.now()
        return super(PostRepository, self).create(post)

    def get_for_user(self, user):
        username = get_from_obj_or_direct(user, "username")

        posts = self.c().find({"author" : username }).sort("post_date", DESCENDING)
        converted = (self.convert_to_model(p) for p in posts)
        return converted
