import sqlite3

class SQLiteHelper:
    def __init__(self, name = 'None'):
        self.conn = None
        self.cursor = None
        self.name = name[9:len(name)-3]
        if name:
            self.open(name)
        
    def open(self, name):
        try:
            self.conn = sqlite3.connect(name)
            self.cursor = self.conn.cursor()
            print(sqlite3.version)
        except sqlite3.Error as e:
            print(e)
            print('Failed connecting to database ...')
    
    def create_table(self, query):
        c = self.cursor
        c.execute(query)
    
    #INSERT & UPDATE ~ thêm, sửa dữ liệu
    def edit(self, query):
        c = self.cursor
        c.execute(query)
        self.conn.commit()
            # sau khi thay đổi phải có commit ~ cam kết
    
    def insert(self, term, doc_frequence, list_doc):
        c = self.cursor
        query = "INSERT INTO %s (term, doc_frequence, list_doc) VALUES (\"%s\",%d, \"%s\")"%(self.name, term, doc_frequence, list_doc)
        c.execute(query)
        self.conn.commit()

    # LẤY DỮ LIỆU
    def select(self, query): 
        c = self.cursor
        c.execute(query)
        return c.fetchall() # fetchall sẽ trả về các giá trị đã được lấy từ truy vấn
        # lấy dữ liệu không cần commit !!!

    def get_len(self):
        c = self.cursor
        query = "SELECT count(ROWID) FROM %s"%(self.name)
        c.execute(query)
        return c.fetchall()[0][0] # fetchall sẽ trả về các giá trị đã được lấy từ truy vấn
    
    def add_column(self, colum, type_col):
        c = self.cursor
        query = "ALTER TABLE %s ADD COLUMN %s %s"%(self.name, colum, type_col)
        c.execute(query)
        self.conn.commit()

    def get_row_by_rowid(self, rowid):
        c = self.cursor
        query = "SELECT * FROM %s WHERE rowid = %d"%(self.name, rowid)
        c.execute(query)
        return c.fetchall()[0]
    
    def get_row_by_term(self, term):
        c = self.cursor
        query = "SELECT * FROM %s WHERE term = \"%s\""%(self.name, term)
        c.execute(query)
        row = c.fetchone()
        if row == None:
            return -1
        return row
