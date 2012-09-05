from presentation import register_filters

class SQLContext(object):

    def __init__(self, app):
        from flask.ext.sqlalchemy import SQLAlchemy
        from service.sql import mappings, user_repository, post_repository
        from service import authentication_service
        db = SQLAlchemy(app)
        mappings.init(db)

        self.db = db

        self.post_repository = post_repository.PostRepository(db)
        self.user_repository = user_repository.UserRepository(app, db)
        self.authentication_service = authentication_service.AuthenticationService(
                app, self.user_repository
        )

        register_filters(app)

    def setup(self):
        self.db.create_all()

class MongoContext(object):

    def __init__(self, app):
        from pymongo import Connection
        from service.mongo import user_repository, post_repository
        from service import authentication_service
        c = Connection()
        db = c.blogex

        self.post_repository = post_repository.PostRepository(db)
        self.user_repository = user_repository.UserRepository(app, db, self.post_repository)
        self.authentication_service = authentication_service.AuthenticationService(
                app, self.user_repository
        )

        register_filters(app)

    def setup(self):
        pass
