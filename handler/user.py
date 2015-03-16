#!/usr/bin/env python
# coding=utf-8


from handler.base import BaseHandler
import hashlib
import time
import tornado.web


def do_login(self,user_id):
    user_info = self.user_model.get_user_by_uid(user_id)
    username = user_info["username"]
    try:
        self.set_secure_cookie("username", str(username)) 
    except Exception,e:
        print e

def login_out(self):
    self.clear_cookie("username") 

class RegisterHandler(BaseHandler):
    def get(self,template_variables = {}):
        self.render("user/register.html",**template_variables)

    def post(self,template_variables = {}):
        user_name = self.get_argument("username")
        pass_word = self.get_argument("password")
        password_confirm = self.get_argument("password_confirm") 
        
        if pass_word != password_confirm:
            return self.write("password is not the same")
        secure_password = hashlib.sha1(pass_word).hexdigest()

        join_time = time.strftime('%Y-%m-%d %H:%M:%S')

        self.user_model.add_new_user(user_name,secure_password,join_time)
        self.redirect("/login")


class LoginHandler(BaseHandler):
    def get(self,template_variables = {}):
        user_info = self.get_current_user() 
        if user_info:
            self.redirect("/")
        else:
            self.render("user/login.html",**template_variables)

    def post(self,template_variables = {}):
        username = self.get_argument("username")
        password = self.get_argument("password")

        secure_password = hashlib.sha1(password).hexdigest()

        userinfo = self.user_model.login(username,secure_password)
        if userinfo:
            do_login(self,userinfo["id"])
            template_variables["username"] = userinfo["username"]
            self.render("user/person.html",**template_variables) 
        else:
            self.write("Password wrong!")
 
class LoginOutHandler(BaseHandler):
    def get(self,template_variables = {}):
        login_out(self)
        self.redirect("/login")


        
        


        



