from github import Github
from zoneinfo import ZoneInfo
import sqlite3, os, datetime, requests,json, re, jaconv, random

class MySQLite():
    def __init__(self, db = f"{os.path.dirname(os.path.abspath(__file__))}/sqlite3.db"):
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

class CreateMessage(MySQLite):
    def __init__(self, admin, db = f"{os.path.dirname(os.path.abspath(__file__))}/sqlite3.db"):
        self.nowTime = datetime.datetime.now(ZoneInfo("Asia/Tokyo"))
        self.weekdayName = ("月","火","水","木","金","土","日")
        super().__init__(db)
        self.admin = admin
        self.hiragana = re.compile(r'[\u3041-\u3096]') #ひらがなの登録
        self.katakana = re.compile(r'[\u30A0-\u30FA]') #カタカナの登録

    def classify_message(self, message):
        self.message = message
        try:
            self.categoryData = self.send_sql(f"""
                SELECT category FROM emotion 
                    WHERE "{self.message}" LIKE CONCAT("%",data,"%")
                    ORDER BY id ASC
            """)[0][0]
        except Exception as e:
            print(e)
            self.categoryData = "Thank you for comment."
    
    def get_message(self):
        if self.categoryData.count("date")>0:
            return  f"{self.nowTime.year}年 {self.nowTime.month}月 {self.nowTime.day}日 {self.weekdayName[self.nowTime.weekday()]}曜日です"
        elif self.categoryData.count("time")>0:
            return f"{self.nowTime.hour}:{self.nowTime.minute}だよ"
        elif self.categoryData.count("weather")>0:
            return self.get_weather()
        
        elif self.categoryData.count("morse")>0:
            return self.exchange(
                morsestr = self.message.split("モールス信号:")[1]
            )
        
        elif self.categoryData.count("jamcode")>0:
            return self.morse_decode(
                morseCode = self.message.split("日文モールス復号:")[1],
                lang = "ja"
            )
        elif self.categoryData.count("eumcode")>0:
            return self.morse_decode(
                morseCode = self.message.split("欧文モールス復号:")[1],
                lang = "eu"
            )
        
        elif self.categoryData.count("help")>0:
            with open(f"{os.path.dirname(os.path.abspath(__file__))}/README.md") as readme:
                return readme.read()
        
        else:
            try:
                replyData = self.send_sql(f"""
                    SELECT value FROM keywordlist
                    WHERE key = "nevertheless"
                """)
                for n in replyData:
                    if int(self.message.count(n[0])) > 0:
                        self.message = self.message.split(n[0])[1]

                self.categoryData = self.send_sql(f"""
                    SELECT category FROM emotion 
                        WHERE "{self.message}" LIKE CONCAT("%",data,"%")
                        ORDER BY id ASC
                """)[0][0]

                if self.categoryData.count("おやすみ")>0:
                    return "おやすみzzz..."
                
                elif self.categoryData.count("おかえり")>0:
                    return "ただいま"

                elif self.categoryData.count("ただいま")>0:
                    return "おかえり"

                elif self.categoryData.count("ありがと")>0:
                    return "どういたしまして(*´ω｀*)〜♪"

                elif self.categoryData.count("どうした")>0:
                    return "コメントに反応しただけだよ"

                elif self.categoryData.count("どした")>0:
                    return "コメントに反応しただけだよ"
                
                else:
                    rep = self.send_sql(f"""
                        SELECT value FROM keywordlist
                            WHERE key = "{self.categoryData}"
                    """)

                ansIndex = random.randint(0, len(rep)-1) # 最小値以上最大値未満の浮動小数点数
                return rep[ansIndex][0]
            except Exception as e:
                print(e)
                return self.categoryData

    def get_weather(self):
        if self.message.count("明日") > 0:
            dateNumber = 1
        elif self.message.count("明後日") > 0:
            dateNumber = 2
        else:
            dateNumber = 0
        jsonURL = "https://weather.tsukumijima.net/api/forecast/city/"
        if (self.message.count("都")>0):
            prefecture = self.message.split("都")[0]
        elif (self.message.count("道")>0):
            prefecture = self.message.split("道")[0]
        elif (self.message.count("府")>0 ):
            prefecture = self.message.split("府")[0]
        elif(self.message.count("県")>0 ):
            prefecture = self.message.split("県")[0]
        else:
            prefecture = "東京"
        if (prefecture.count("神奈川") > 0 or prefecture.count("和歌山") > 0 or prefecture.count("鹿児島") > 0):
            prefecture = prefecture[-3:]
        else:
            prefecture = prefecture[-2:]
        
        try:
            cityID = self.send_sql(f"""
                SELECT id FROM weather 
                    WHERE prefecture = "{prefecture}"
                    ORDER BY id ASC
            """)[0][0]
        except:
            cityID = "130010"
        url = f"{jsonURL}{cityID}"
        
        weatherData = requests.get(url)
        weatherJSONData = json.loads(weatherData.text)
        weatherDate = weatherJSONData["forecasts"][dateNumber]["date"]
        weartherTitle = weatherJSONData["title"]
        if dateNumber == 2:
            weather = weatherJSONData["forecasts"][dateNumber]["telop"]
        else:
            weather = weatherJSONData["forecasts"][dateNumber]["detail"]["weather"]
        tempMin = weatherJSONData["forecasts"][dateNumber]["temperature"]["min"]["celsius"]
        tempMax = weatherJSONData["forecasts"][dateNumber]["temperature"]["max"]["celsius"]
        telop = weatherJSONData["description"]["text"].replace("　","")
        chanceOfRain0_6 = weatherJSONData["forecasts"][dateNumber]["chanceOfRain"]["T00_06"]
        chanceOfRain6_12 = weatherJSONData["forecasts"][dateNumber]["chanceOfRain"]["T06_12"]
        chanceOfRain12_18 = weatherJSONData["forecasts"][dateNumber]["chanceOfRain"]["T12_18"]
        chanceOfRain18_24 = weatherJSONData["forecasts"][dateNumber]["chanceOfRain"]["T18_24"]
        chanceOfRain = f"""
0時～6時 : {chanceOfRain0_6}
6時～12時 : {chanceOfRain6_12}
12時～18時 : {chanceOfRain12_18}
18時～24時 : {chanceOfRain18_24}"""
        svgWeatherURL = weatherJSONData["forecasts"][dateNumber]["image"]["url"]

        return f"""
# {str(weatherDate)}の{weartherTitle}は{weather}

<p align="right">
    <a href = "{url}">
        <img src = "{svgWeatherURL}">
    </a>
</p>

{telop}

## 最高気温
{tempMax}℃
## 最低気温
{tempMin}℃
## 降水確率
{chanceOfRain}  
        """
    
    def exchange(self, morsestr):
        val = []
        for code in morsestr:
            if code == "　":
                code = "space"
            elif code == " ":
                code = "space"
            elif code == "゛":
                code = "濁点"
            elif code == "゜":
                code = "半濁点"
                
            elif (self.hiragana.search(code) is not None):
                hkataka = jaconv.hira2hkata(code)
                hkm = jaconv.h2z(hkataka[0])
                try:
                    hka = jaconv.h2z(hkataka[1])
                    val.append(
                        self.send_sql(f"""
                            SELECT value FROM morse
                            WHERE data = "{jaconv.kata2hira(hkm)}"
                        """)[0][0]
                    )
                    if hka == '\uFF9E':
                        code = "濁点"
                    elif hka == '\uFF9F':
                        code = "半濁点"
                
                except IndexError:
                    hka = ""

            elif (self.katakana.search(code) is not None):
                hkataka = jaconv.z2h(code)
                hkm = jaconv.h2z(hkataka[0])
                try:
                    hka = jaconv.h2z(hkataka[1])
                    val.append(
                        self.send_sql(f"""
                            SELECT value FROM morse
                            WHERE data = "{jaconv.kata2hira(hkm)}"
                        """)[0][0]
                    )
                    if hka == '\uFF9E':
                        code = "濁点"
                    elif hka == '\uFF9F':
                        code = "半濁点"
                
                except IndexError:
                    hka = ""
                    code = jaconv.kata2hira(hkm)
            else:
                code = code.lower()

            try:
                val.append(
                    self.send_sql(f"""
                        SELECT value FROM morse
                        WHERE data = "{code}"
                    """)[0][0]
                )
            except:
                val.append("")

        return " ".join(val)
    
    def morse_decode(self, morseCode:str, lang = "ja"):
        morseCodeData = morseCode.split(" ")
        ans = ""
        language = lang
        if language != "ja":
            language = "en"
        for mcode in morseCodeData:
            try:
                
                code = self.send_sql(f"""
                    SELECT data FROM morse
                    WHERE value = "{mcode}"
                    AND (
                        lang = "{language}" OR
                        lang = "base"
                    )

                """)[0][0]
                if code == "濁点":
                    ans += "゛"
                elif code == "半濁点":
                    ans += "゜"
                else:
                    ans += code
            except:
                ans += " "
        return ans



class GitProject(Github):
    def __init__(self, admin, target, db = f"{os.path.dirname(os.path.abspath(__file__))}/sqlite3.db"):
        # 環境変数を取得
        self.token          = os.getenv('ACCESS_TOKEN')
        self.repo_name      = os.getenv('GITHUB_REPOSITORY')
        self.issue_number   = os.getenv('GITHUB_EVENT_ISSUE_NUMBER')
        self.target         = target
        self.directory      = os.path.dirname(os.path.abspath(__file__))
        self.admin          = admin
        
        super().__init__(self.token) # GitHubクライアントを初期化
        self.repo       = self.get_repo(self.repo_name)
        self.issue      = self.repo.get_issue(int(self.issue_number))
        self.comments   = list(self.issue.get_comments())
        self.db         = db
    
    def recv_issue(self): # issueにコメントを追加
        # self.username:
        self.data = ""
        try:
            latest_comment = self.comments[-1]
            if latest_comment.body.count("$") > 0:
                self.data = latest_comment.body.replace("$","")
        except:
            self.data = "issue"
    
    def send_issue(self):
        if self.data != "":
            with CreateMessage(self.admin, self.db) as msg:
                msg.classify_message(self.data)
                message = msg.get_message()
            
            self.issue.create_comment(message)


if __name__ == "__main__":
    gitissue = GitProject("BX293APEN", "$", f"{os.path.dirname(os.path.abspath(__file__))}/db/sqlite3.db")
    gitissue.recv_issue()
    gitissue.send_issue()
