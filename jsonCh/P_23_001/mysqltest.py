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
    'user': 'root',            # MariaDB 사용자 이름
    'password': 'manager',     # MariaDB 비밀번호 mac mini
    'database': 'happyzip',    # 사용할 데이터베이스 이름
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

def read_file_as_blob(file_path):
    """주어진 파일을 바이너리 모드로 읽고 BLOB 데이터를 반환"""
    try:
        with open(file_path, 'rb') as file:
            return file.read()
    except FileNotFoundError:
        print(f"파일을 찾을 수 없습니다: {file_path}")
        return None

def insert_files_into_db(file_paths):
    """파일을 MySQL에 BLOB 형태로 저장"""
    # MySQL에 연결
    connection = pymysql.connect(**db_config)
    
    try:
        with connection.cursor() as cursor:
            # INSERT 쿼리 준비
            insert_query = """
                INSERT INTO files_data (file_name, file_data) 
                VALUES (%s, %s)
            """
            for file_path in file_paths:
                # 파일 경로에서 파일 이름 추출
                file_name = os.path.basename(file_path) if file_path else None
                # 파일을 읽어 BLOB 데이터로 변환 (파일이 없을 경우 None 반환)
                file_blob = read_file_as_blob(file_path) if file_path else None

                # 파일 이름이 없을 경우 'NULL_FILE'로 대체 (필요한 경우)
                if not file_name:
                    file_name = 'NULL_FILE'
                
                # 파일 데이터를 DB에 저장 (파일이 없으면 None을 BLOB에 넣음)
                cursor.execute(insert_query, (file_name, file_blob))
                print(f"{file_name} 파일이 성공적으로 저장되었습니다.")
            
            # 변경 사항 커밋
            connection.commit()
    except Exception as e:
        print(f"오류 발생: {e}")
        connection.rollback()
    finally:
        # MySQL 연결 종료
        connection.close()

# 데이터베이스에 데이터 삽입 함수
def insert_data_to_db(data):
    connection = connect_to_db()
    try:
        with connection.cursor() as cursor:
            # JSON 데이터를 삽입할 테이블명 및 컬럼 구성
            if data['TABLE_NAME'] == "SHIP_PROJECT_DATA":
                sql = """
                INSERT INTO project_data (PROJECT_NO, SHIP_TITLE, GENERAL_INFORMATION, SHIP_INFORMATION, ENGINE_ROOM,PROPELLER,ETC) 
                VALUES (%s, %s, %s, %s, %s, %s,%s)
                """
                # 데이터 삽입
                #for entry in data:
                cursor.execute(sql, (str(data['PROJECT_NO']), str(data['SHIP_TITLE']), str(data['GENERAL_INFORMATION']),str(data['SHIP_INFORMATION']),
                str(data['ENGINE_ROOM']),str(data['PROPELLER']),str(data['ETC']) ))
            elif data['TABLE_NAME'] == "DRAFT_CONDITION_DATA":
                sql = """
                INSERT INTO project_data (PROJECT_NO, SHIP_TITLE, GENERAL_INFORMATION, SHIP_INFORMATION, ENGINE_ROOM,PROPELLER,ETC) 
                VALUES (%s, %s, %s, %s, %s, %s,%s)
                """
                # 데이터 삽입
                #for entry in data:
                cursor.execute(sql, (str(data['PROJECT_NO']), str(data['SHIP_TITLE']), str(data['GENERAL_INFORMATION']),str(data['SHIP_INFORMATION']),
                str(data['ENGINE_ROOM']),str(data['PROPELLER']),str(data['ETC']) ))
            elif data['TABLE_NAME'] == "PROPELLER_DESIGN_RESULTS":
                sql = """
                INSERT INTO project_data (PROJECT_NO, SHIP_TITLE, GENERAL_INFORMATION, SHIP_INFORMATION, ENGINE_ROOM,PROPELLER,ETC) 
                VALUES (%s, %s, %s, %s, %s, %s,%s)
                """
                # 데이터 삽입
                #for entry in data:
                cursor.execute(sql, (str(data['PROJECT_NO']), str(data['SHIP_TITLE']), str(data['GENERAL_INFORMATION']),str(data['SHIP_INFORMATION']),
                str(data['ENGINE_ROOM']),str(data['PROPELLER']),str(data['ETC']) ))                
            elif data['TABLE_NAME'] == "SHIP_INITIAL_DESIGN_RESULTS":
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
