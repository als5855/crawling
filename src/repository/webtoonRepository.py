import pymysql

def saveWetoonData(webtoonData: list):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='dnfru9630!@', db='new_webtoon_db')
        try:
            cursor = connection.cursor()
            for data in webtoonData:
                sql = "insert into webtoon_tb values(default, %s,%s,%s,%s,%s,%s)"
                cursor.execute(sql, data["categoryName"])
                category_id = cursor.lastrowid

                values =


