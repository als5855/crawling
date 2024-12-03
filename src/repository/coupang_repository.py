import pymysql
from pymysql import cursors

def saveCoupangData(coupangData: list):

    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', password='dnfru9630!@', db= 'coupang_db')
        try:
            cursor = connection.cursor()
            for data in coupangData:
                sql= "INSERT INTO category_tb VALUSE (default, %s)"
                cursor.execute(sql, data["category"])
                category_id = cursor.lastrowid

                #values = ",\n".join(list(map(lambda product: f"default, \'{product['productName']}\', {product['price'].replace(',', '')}, \'{product['productImgUrl']}\',{category_id}", data['products'])))
                values = ",\n".join(list(map(lambda product: "(default, %s, %s, %s, %s)", data["products"])))
                sql = "insert into product_tb values" + values
                valueDatas = []
                for value in list(map(lambda product: [product["product"], product["price"], product["productImgUrl"], category_id], data["products"]))
                    valueDatas.append(value)
                cursor.execute(sql)
                connection.commit()
        except Exception as e:
            print(e) #SQL 오류
        finally:
            connection.close()

    except Exception as e:
        print("데이터베이스 연결 실패")