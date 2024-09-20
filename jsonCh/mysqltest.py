import json
import pymysql
import os


# 현재 디렉토리 경로
current_dir = os.getcwd()

# 읽고자 하는 파일 확장자
target_extension = ".json"

# MariaDB 연결 설정
db_config = {
    'host': 'localhost',       # DB 서버 주소
    'user': 'root',   # MariaDB 사용자 이름
    'password': 'manager', # MariaDB 비밀번호 mac mini
    'database': 'happyzip', # 사용할 데이터베이스 이름
}

# MariaDB 연결 함수
def connect_to_db():
    connection = pymysql.connect(
        host=db_config['host'],
        user=db_config['user'],
        password=db_config['password'],
        database=db_config['database'],
        cursorclass=pymysql.cursors.DictCursor
    )
    return connection

# JSON 파일 읽기 함수
def read_json_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data

# 데이터베이스에 데이터 삽입 함수
def insert_data_to_db(data):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            # JSON 데이터를 삽입할 테이블명 및 컬럼 구성
            sql = """
            INSERT INTO project_data (PROJECT_NO, SHIP_TITLE, GENERAL_INFORMATION, SHIP_INFORMATION, ENGINE_ROOM,PROPELLER,ETC) 
            VALUES (%s, %s, %s, %s, %s, %s,%s)
            """
            # 데이터 삽입
            #for entry in data:
            cursor.execute(sql, (str(data['PROJECT_NO']), str(data['SHIP_TITLE']), str(data['GENERAL_INFORMATION']),str(data['SHIP_INFORMATION']),
         str(data['ENGINE_ROOM']),str(data['PROPELLER']),str(data['ETC']) ))
            connection.commit()  # 커밋
    finally:
        connection.close()  # 연결 종료

# 메인 함수
if __name__ == "__main__":
    # 현재 디렉토리 내 모든 파일 중 특정 확장자 파일만 읽기
    for filename in os.listdir(current_dir):
        # 파일 경로 생성
        file_path = os.path.join(current_dir, filename)

        # 파일인지 확인하고, 확장자가 target_extension과 일치하는지 확인
        if os.path.isfile(file_path) and filename.endswith(target_extension):
            #json_file_path = '1.json'  # 읽어올 JSON 파일 경로
            json_data = read_json_file(file_path)
            insert_data_to_db(json_data)
