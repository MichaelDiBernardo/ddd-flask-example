import datetime
from sqlalchemy import desc

from models import Post
from service.sql import orm_repository_base
from service.utils import get_from_obj_or_direct

class PostRepository(orm_repository_base.RepositoryBase):
    def create(self, post):
        post.author = get_from_obj_or_direct(post.author, "username")
        post.post_date = datetime.datetime.now()
        return super(PostRepository, self).create(post)
    
    def get_for_user(self, user):
        username = get_from_obj_or_direct(user, "username")
        posts = self.session().query(Post).filter_by(author=username).order_by(desc("post_date"))
        return posts
