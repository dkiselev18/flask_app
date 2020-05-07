import psycopg2


class DatabaseConnection(object):
    def __enter__(self):
        # make a database connection and return it
        ...
        self.conn = psycopg2.connect(dbname='nbstdbtx', user='nbstdbtx',
                                password='NHWMfgmkbxoifk36K_JQT6IX_I3KGVqy', host='drona.db.elephantsql.com')
        return self.conn

    def __exit__(self, exc_type, exc_val, exc_tb):
        # connection gets closed
        self.conn.close()