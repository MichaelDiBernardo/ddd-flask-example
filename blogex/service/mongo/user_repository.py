from models import BlogexUser 
from service.mongo import mongo_repository_base

class UserRepository(mongo_repository_base.RepositoryBase):
    class Meta:
        model = BlogexUser
        collection_name = "users"

    def __init__(self, app, db, post_repository):
        super(UserRepository, self).__init__(db)
        self.post_repository = post_repository

    def get_by_username(self, username):
        result = self.c().find_one({"username" : username})
        if result == None: 
            return None

        converted = self.convert_to_model(result)
        converted.posts = self.post_repository.get_for_user(username)
        return converted
