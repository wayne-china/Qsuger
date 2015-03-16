import torndb


class LoveModel:
    def __init__(self,db):
        self.db = db
        self.table_name = "love_list"

    def add_love(self,product_id,user_id):
        sql = "INSERT INTO %s VALUES (product_id=%s,user_id=%s)" % (self.table_name,product_id,user_id)
        return self.db.execute(sql)

    def delete_love(self,product_id,user_id):
        sql = "DELETE FROM  %s WHERE product_id=%s AND user_id=%s)" % (self.table_name,product_id,user_id)
        return self.db.execute(sql)

