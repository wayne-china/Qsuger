#!/usr/bin/env python
# coding=utf-8

from tornado.web import RequestHandler
from db import user,product,film,reply,love
import lib.session

class BaseHandler(RequestHandler):
    def __init__(self, *argc, **argkw):
         super(BaseHandler, self).__init__(*argc, **argkw)
         self.session = session.Session(self.application.session_manager, self)
   
    @property
    def db(self):
        return self.application.db

    @property
    def user_model(self):
        return user.UserModel(self.application.db)

    @property
    def product_model(self):
        return product.ProductModel(self.application.db)

    @property
    def film_model(self):
        return film.FilmModel(self.application.db)

    @property
    def reply_model(self):
        return reply.ReplyModel(self.application.db)

    @property
    def love_model(self):
        return love.LoveModel(self.application.db)


    def get_current_user(self):
        username = self.get_secure_cookie("username")
        if not username: return None
        return self.user_model.get_user_by_name(username)
