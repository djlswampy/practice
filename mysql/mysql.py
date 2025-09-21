import mysql.connector
from mysql.connector import Error

# 데이터베이스 연결
try:
    connection = mysql.connector.connect(
        host='localhost',
        database='your_database',
        user='your_username',
        password='your_password',
        port=3306  # 기본 포트
    )
    
    if connection.is_connected():
        print("MySQL 연결 성공")
        
except Error as e:
    print(f"연결 오류: {e}")
finally:
    if connection.is_connected():
        connection.close()