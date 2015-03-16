import torndb


class FilmModel(object):
    def __init__(self,db):
        self.db = db
        self.table_name = "film"

    def add_film(self,film_name):
        sql = "INSERT INTO %s SET film_name=%s" \
                                        % (self.table_name,film_name)
        return self.db.execute(sql)

    def get_id_by_name(self,film_name):
        sql = "SELECT id FROM %s WHERE film_name = '%s'" \
                                        % (self.table_name,film_name)
        return self.db.get(sql)

#    @classmethod
    def get_film_by_id(self,id):
        sql = "SELECT film_name FROM %s WHERE id = %s" \
                                        % (self.table_name,id)
        return self.db.query(sql) 

