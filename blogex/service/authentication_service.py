from flask.ext.login import LoginManager
from flask.ext.login import login_user as god_login, logout_user as god_logout
from flask.ext.login import login_required as flask_login_required
import flask.ext.login

class AuthenticationService(object):
    def __init__(self, app, user_repository):
        self.user_repository = user_repository

        login_manager = LoginManager()
        login_manager.user_loader(self.user_repository.get_by_username)
        login_manager.setup_app(app)

        self.login_manager = login_manager

    def login_user(self, user):
        god_login(user, remember=True)

    def logout_current_user(self):
        god_logout()

    def get_current_user(self):
        return self.user_repository.get_by_username(flask.ext.login.current_user.username)
    
    def login_required(self, callable): 
        return flask_login_required(callable)
