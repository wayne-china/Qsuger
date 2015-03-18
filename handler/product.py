#!/usr/bin/env python
# coding=utf-8


from handler.base import BaseHandler
import tornado.web
import os.path
import random
import string
import time

class IndexHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,template_variables = {}):
        user_info = self.get_current_user()
   #     if not user_info:  return self.render("/login")
        self.product_timeline = self.product_model.get_all_product()
    #    template_variables["products"] = product_timeline
        template_variables["username"] = user_info["username"] 
        self.render("index.html",**template_variables)

class ShareHandler(BaseHandler):
    @tornado.web.authenticated
    def get(self,template_variables = {}):
        self.render("product/share.html",**template_variables)

    def post(self,template_variables = {}):
        user_info = self.current_user 
        product_name = self.get_argument("product_name")
        product_link = self.get_argument("product_link")
        film_name = self.get_argument("film_name")
        film_id = self.film_model.get_id_by_name(film_name)
        film_id = film_id["id"]
        share_time = time.strftime('%Y-%m-%d %H:%M:%S')

        #image upload
        product_image = self.request.files['file'][0]
        original_fname = product_image['filename']
      #  extension = os.path.splitext(original_fname)[1]
      #  fname = ''.join(random.choice(string.ascii_lowercase + string.digits) for x in range(6))
      #  final_filename= fname+extension
        final_filename = original_fname
        output_file = open("static/" + final_filename, 'w')
        output_file.write(product_image['body'])

         
        product_info = self.product_model.share_product(product_name,user_info["id"],share_time,film_id,product_link)
        if product_info:
            template_variables["product_name"] = product_name
            template_variables["product_link"] = product_link
            template_variables["film_name"] = film_name
            template_variables["username"] = user_info["username"]
            template_variables["final_filename"] = final_filename
            self.render("product/product.html",**template_variables)
        else:
            self.write("Share Failed")

            

#class IndexHandler(BaseHandler):
#    
#    def get(self, template_variables = {}):
#        film_name = self.film_model.get_film_by_id(21) 
#        template_variables["film_name"] = list_to_dict(film_name)["film_name"] 
#        self.render("index.html", **template_variables)
        



def list_to_dict(list):
    for i in list:
        return i
        



