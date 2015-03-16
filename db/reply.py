import torndb


class ReplyModel:
    def __init__(self,db):
        self.db = db
        self.table_name = "reply"

    def add_reply(self,product_id,user_id,reply_content):
        sql = "INSERT INTO %s VALUES (product_id=%s,user_id=%s,reply_content=%s)" \
                                        % (self.table_name,product_id,user_id,reply_content)
        return self.db.execute(sql)

    def delete_reply(self,product_id,user_id):
        sql = "DELETE FROM  %s WHERE product_id=%s AND user_id=%s)" % (self.table_name,product_id,user_id)
        return self.db.execute(sql)

    def get_reply_by_product_id(self,product_id):
        sql = "SELECT * from %s WHERE product_id=%s " % (self.table_name,product_id)
        return self.db,execute(sql)
