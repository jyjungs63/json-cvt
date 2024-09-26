import pymysql

def insert_blob(image_path):
    # 데이터베이스 연결 설정
    db_config = {
    'host': 'localhost',       # DB 서버 주소
    'user': 'root',   # MariaDB 사용자 이름
    'password': 'manager', # MariaDB 비밀번호 mac mini
    'database': 'test', # 사용할 데이터베이스 이름
    }

    # 데이터베이스 연결
    connection = pymysql.connect(**db_config)
    cursor = connection.cursor()

    # 테이블이 존재하지 않으면 생성
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS images (
        id INT AUTO_INCREMENT PRIMARY KEY,
        image LONGBLOB NOT NULL
    )
    """)

    # 이미지 파일 읽기
    with open(image_path, 'rb') as file:
        binary_data = file.read()

    # 이미지 삽입 쿼리
    insert_query = "INSERT INTO images (image) VALUES (%s)"
    cursor.execute(insert_query, (binary_data,))

    # 트랜잭션 커밋
    connection.commit()

    print("이미지가 성공적으로 삽입되었습니다.")

    # 커서와 연결 종료
    cursor.close()
    connection.close()

# 사용 예
#insert_blob('/Users/jinyoung/happy.jpeg')
insert_blob('/Users/jinyoung/json-cvt/jsonCh/P_23_001/hydrodynamic_design_results/(P_23_001)ESD_DESIGN_REPORT.pdf')
