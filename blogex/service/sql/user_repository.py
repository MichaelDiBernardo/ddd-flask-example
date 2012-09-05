from models import BlogexUser 
from service.sql import orm_repository_base

class UserRepository(orm_repository_base.RepositoryBase):
    def __init__(self, app, db):
        super(UserRepository, self).__init__(db)

    def get_by_username(self, username):
        try:
            return self.session().query(BlogexUser).filter_by(username=username).one()
        except:
            return None
