import sqlite3, os, json

class MySQLite():
    def __init__(self, db = f"{os.path.dirname(__file__)}/sqlite3.db"):
        # データベースとの接続
        self.databaseHost = sqlite3.connect(database = db)
    
    def __enter__(self):
        # カーソルを作る
        self.database = self.databaseHost.cursor()
        return self
    
    def send_sql(self, sql): # SQL文送信
        self.database.execute(sql)
        self.db_commit()
        return self.database.fetchall() # タプル形式で全て取得
    
    def db_commit(self):
        self.databaseHost.commit()

    def __exit__(self, *args):
        self.db_commit()
        self.database.close()
        self.databaseHost.close()

if __name__ == "__main__":
    with MySQLite()as database:
        database.send_sql(f"""
            CREATE TABLE emotion(
                id       INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                data     TEXT UNIQUE NOT NULL,
                category TEXT NOT NULL
            )
        """)
    with open("emotion.csv",'r',encoding="utf-8_sig") as emotionFile:
        emotionData = emotionFile.read()
        emotionLine = emotionData.split('\n')
    
    with MySQLite()as database:
        for e in emotionLine:
            if int(e.count(",")) > 0:
                emotion = e.split(",")
                try:
                    database.send_sql(
                        f"""INSERT INTO emotion (data, category) VALUES(\"{emotion[0]}\", \"{emotion[1]}\")"""
                    )
                except Exception as er:
                    print(f"""ERROR : {e}""")

    with open("morse.json", "r", encoding="UTF-8") as m:
        mdata = json.loads(m.read())

    with MySQLite()as database:
        database.send_sql(f"""
            CREATE TABLE morse(
                data        TEXT NOT NULL,
                value       TEXT NOT NULL,
                lang        TEXT NOT NULL
            )
        """)
    
    with MySQLite()as database:
        for d, v in mdata["ja"].items():
            try:
                database.send_sql(
                    f"""INSERT INTO morse (data, value, lang) VALUES("{d}", "{v}", "ja")"""
                )
            except Exception as e:
                print(f"""ERROR : {d}""")
        
        for d, v in mdata["en"].items():
            try:
                database.send_sql(
                    f"""INSERT INTO morse (data, value, lang) VALUES("{d}", "{v}", "en")"""
                )
            except Exception as er:
                print(f"""ERROR : {e}""")
        
    

    with MySQLite()as database:
        database.send_sql(f"""
            CREATE TABLE weather(
                id              TEXT UNIQUE NOT NULL,
                prefecture      TEXT UNIQUE NOT NULL
            )
        """)
    
    with open("areaid.csv", "r", encoding="shift-jis") as w:
        wdata = w.read().split("\n")

    with MySQLite()as database:
        for wd in wdata:
            if int(wd.count(",")) > 0:
                weather = wd.split(",")
                try:
                    database.send_sql(
                        f"""INSERT INTO weather (prefecture, id) VALUES(\"{weather[0]}\", \"{weather[1]}\")"""
                    )
                except Exception as er:
                    print(f"""ERROR : {e}""")
    

    with MySQLite()as database:
        database.send_sql(f"""
            CREATE TABLE keywordlist(
                key        TEXT,
                value      TEXT
            )
        """)

    with open("replyword.json", "r", encoding="UTF-8") as r:
        rData = json.loads(r.read())
    
    with MySQLite()as database:
        for wd in rData:
            for w in rData[wd]:
                try:
                    database.send_sql(
                        f"""INSERT INTO keywordlist (key, value) VALUES(\"{wd}\", \"{w}\")"""
                    )
                except Exception as er:
                    print(f"""ERROR : {wd} {er}""")