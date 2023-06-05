'''import mysql.connector as ms
$pip install mysql.connector

cnt=ms.connect(host='localhost',port="3306",user='root',password='1234',database='board')

#커서객체는 db에서 쿼리의 결과를 검색하고 순환하는데 사용하는 객체
cursor=cnt.cursor()
add_data=f"insert into author(name,email) values({name},{email})"
name='John'
email='john@test.com'

cnt.commit()
cursor.close()
cnt.close
'''
import mysql.connector
connector = mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="test1234",
    database="board",
    use_pure=True)

# 커서객체는 데이터베이스에서 쿼리의 결과를
# 검색하고 순회하는데 사용되는 객체
cursor = connector.cursor()
add_data = "INSERT INTO author (name, email) VALUES(%s, %s)"
data = ("John", "hello2@naver.com")
cursor.execute(add_data, data)
connector.commit()
cursor.close()
connector.close()

#vs code에선 돌아가네..?
