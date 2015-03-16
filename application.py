#!/usr/bin/env python
# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding("utf8")

import os.path
import re
import torndb
import tornado.httpserver
import tornado.ioloop
import tornado.options
import tornado.web

import handler.base
import handler.product
import handler.user

from tornado.options import define, options
from lib.session import Session, SessionManager

#import daemon

define("port", default = 80, type = int)
define("mysql_host", default = "127.0.0.1")
define("mysql_database", default = "knewone")
define("mysql_user", default = "root")
define("mysql_password", default = "daoli123")

class Application(tornado.web.Application):
    def __init__(self):
        settings = dict(
            title = u"趣糖",
            template_path = os.path.join(os.path.dirname(__file__), "templates"),
            static_path = os.path.join(os.path.dirname(__file__), "static"),
           # xsrf_cookies = True,
            cookie_secret = "cookie_secret_code",
            login_url = "/login",
        )

        handlers = [
            (r"/", handler.product.IndexHandler),
            (r"/register", handler.user.RegisterHandler),
            (r"/login", handler.user.LoginHandler),
            (r"/loginout", handler.user.LoginOutHandler),
            (r"/share", handler.product.ShareHandler),
 #           (r"/t/(\d+)", handler.topic.ViewHandler),
 #           (r"/t/create/(.*)", handler.topic.CreateHandler),
 #           (r"/t/edit/(.*)", handler.topic.EditHandler),
 #           (r"/reply/edit/(.*)", handler.topic.ReplyEditHandler),
 #           (r"/node/(.*)", handler.topic.NodeTopicsHandler),
 #           (r"/u/(.*)/topics", handler.topic.UserTopicsHandler),
 #           (r"/u/(.*)/replies", handler.topic.UserRepliesHandler),
 #           (r"/u/(.*)/favorites", handler.topic.UserFavoritesHandler),
 #           (r"/u/(.*)", handler.topic.ProfileHandler),
 #           (r"/vote", handler.topic.VoteHandler),
 #           (r"/favorite", handler.topic.FavoriteHandler),
 #           (r"/unfavorite", handler.topic.CancelFavoriteHandler),
 #           (r"/notifications", handler.notification.ListHandler),
 #           (r"/members", handler.topic.MembersHandler),
 #           (r"/setting", handler.user.SettingHandler),
 #           (r"/setting/avatar", handler.user.SettingAvatarHandler),
 #           (r"/setting/avatar/gravatar", handler.user.SettingAvatarFromGravatarHandler),
 #           (r"/setting/password", handler.user.SettingPasswordHandler),
 #           (r"/forgot", handler.user.ForgotPasswordHandler),
 #           (r"/login", handler.user.LoginHandler),
 #           (r"/logout", handler.user.LogoutHandler),
 #           (r"/register", handler.user.RegisterHandler),

            (r"/(favicon\.ico)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
 #           (r"/(sitemap.*$)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
 #           (r"/(bdsitemap\.txt)", tornado.web.StaticFileHandler, dict(path = settings["static_path"])),
 #           (r"/(.*)", handler.topic.ProfileHandler),
        ]

        tornado.web.Application.__init__(self, handlers, **settings)

        self.session_manager = SessionManager(settings["cookie_secret"], ["127.0.0.1:11211"], 0)

        # Have one global connection to the blog DB across all handlers
        self.db = torndb.Connection(
            host = options.mysql_host, database = options.mysql_database,
            user = options.mysql_user, password = options.mysql_password
        )

if __name__ == "__main__":
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(options.port)
    tornado.ioloop.IOLoop.instance().start()


