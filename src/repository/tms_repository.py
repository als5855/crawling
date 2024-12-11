import pymysql
from pymysql import cursors



def findBoard(webtoonDict: dict, title: str):
    try:
        connection = pymysql.connect(host='localhost', port=3306, user='root', passwd='dnfru9630!@', db='naver_webtoon_db', cursorclass=cursors.DictCursor)
        try:
            cursor = connection.cursor()
            sql = '''
            select 
                wt.webtoon_id 
                wt.title
                wt.image_url
                wt.author
                
                from wetoon_db wt 
                where title = %s
            '''
            cursor.execute(sql, title)
            foundwebtoon = cursor.fetchone()
            foundwebtoon['rating'] = float(foundwebtoon['rating'])
        except Exception as e:
            print(e)
        finally:
            connection.close()
    except Exception as e:
        print("데이터베이스 연결 실패")
    return

'''
    1. console에서 input() webtoon 제목을 하나 입력 받는다.
    2. 해당 제목의 webtoon 정보를 DB에서 select한다.
    {
        webtoonId: 1,
        title: "참교육",
        author: "채용택/ 한가람"
        rating: 9.89,
        imgUrl: "https://~~",
        categoryName: "월"
    }
    3.  제목 -> 김준일(웹툰제목: 참교육)
        내용 -> webtoonId: 1, title: "참교육"
'''

