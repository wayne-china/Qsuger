import torndb


class ProductModel:
    def __init__(self,db):
        self.db = db
        self.table_name = "product"

    def share_product(self,product_name,user_id,share_time,film_id,link):
        share_time
        sql = "INSERT INTO %s SET product_name='%s',share_id='%s',share_time='%s',film_id='%s',link='%s'" \
                                             % (self.table_name,product_name,user_id,share_time,film_id,link)
        return self.db.execute(sql)

    def get_all_product(self):
        sql = "SELECT * FROM %s " % (self.table_name)
        return self.db.query(sql)
  
    def get_product_by_id(self,id):
        sql = "SELECT product_name FROM %s WHERE id = %s" % (self.table_name,id)
        return self.db.query(sql)

    def delete_product(self,id):
        sql = "DELETE from %s WHERE id=%s" % (self.table_name,id)
        return self.db.execute(sql)

    def edit_product(self,id,product_name,share_id,film_id,link):
        sql = "UPDATE  %s set product_name=%s,share_id=%s,film_id=%s,\
                   link=%s WHERE id=%s)" % (self.table_name,product_name,share_id,film_id,linki,id)
        return self.db.execute(sql)

