import pymysql as py
try:
    connector = py.connect(
        host="localhost",
        port=3306,
        user="root",
        password="1234",
        database="board")

    cursor = connector.cursor()
except py.connect.Error as err:
    print("error")

add_data = "INSERT INTO author (name, email) VALUES(%s, %s)"
data = ("John", "hello6@naver.com")
cursor.execute(add_data, data)
connector.commit()
cursor.close()
connector.close()

