import torndb


class UserModel():
    def __init__(self,db):
        self.db = db
        self.table_name = "user"

    def add_new_user(self,username,password,join_time):
        sql = "INSERT INTO %s (username,password,join_time,last_login_time)VALUES ( '%s','%s','%s','%s')"\
                                                  % (self.table_name,username,password,join_time,join_time)
        return self.db.execute(sql)

    def get_user_by_name(self,username):
        sql = "SELECT * FROM %s WHERE username='%s'" % (self.table_name,username)
        return self.db.get(sql)

    def get_user_by_uid(self,uid):
        sql = "SELECT * FROM %s WHERE id=%s" % (self.table_name,uid)
        return self.db.get(sql)

    def login(self,username,password):
        sql = "SELECT * FROM %s WHERE username = '%s' AND password = '%s' " % (self.table_name,username,password)
        return self.db.get(sql)

    def change_password(self,username,password):
        sql = "UPDDATE %s SET password=%s WHERE username=%s" % (self.table_name,password,username)
        return self.db.execute(sql)

    def last_login(self,username):
        last_login_time = 0
        sql = "UPDDATE %s SET last_login_time=%s WHERE username=%s" % (self.table_name,last_login_time,username)
        return self.db.execute(sql)
