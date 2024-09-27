import json
import pymysql
import os


# 현재 디렉토리 경로
current_dir = os.getcwd() + '/jsonCh/P_23_001'
os.chdir(current_dir)
#current_dir = '/Users/jinyoung/json-cvt/jsonCh/P_23_001'

# 읽고자 하는 파일 확장자
target_extension = ".json"

# MariaDB 연결 설정
db_config = {
    'host': 'localhost',       # DB 서버 주소
    'user': 'root',            # MariaDB 사용자 이름S
    'password': 'manager',     # MariaDB 비밀번호 mac mini
    'database': 'test',    # 사용할 데이터베이스 이름
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
    if file_path == "":
        return None
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
            if data['TABLE_NAME'] == "SHIP_PROJECT_DATA":   ## OK 
                sql = """
                INSERT INTO SHIP_PROJECT_DATA (PROJECT_NO, SHIP_TITLE, GENERAL_INFORMATION, SHIP_INFORMATION, ENGINE_ROOM,PROPELLER,ETC) 
                VALUES (%s, %s, %s, %s, %s, %s, %s)
                """
                # 데이터 삽입
                #for entry in data:
                t0 = str(data['PROJECT_NO'])
                t1 = str(data['SHIP_TITLE'])
                t2 = str(data['GENERAL_INFORMATION'])
                t3 = str(data['SHIP_INFORMATION'])
                t4 = str(data['ENGINE_ROOM'])
                t5 = str(data['PROPELLER'])
                t6 = str(data['ETC']) 

                cursor.execute(sql, (t0, t1, t2, t3,t4,t5,t6))

            elif data['TABLE_NAME'] == "DRAFT_CONDITION_DATA":  # OK
                sql = """
                INSERT INTO DRAFT_CONDITION_DATA (PROJECT_NO, DRAFT_CONDITION, VALUE, CP_VALUE, COMMENT) 
                VALUES (%s, %s, %s, %s, %s)
                """
                # 데이터 삽입
                #for entry in data:
                t0 = str(data['PROJECT_NO'])
                b1 = (str(data['DRAFT_CONDITION'])) 
                b2 = (str(data['VALUE'])) 
                b3 = (str(data['CP_VALUE'])) 
                t4 = str(data['COMMENTS'])
                cursor.execute(sql, (t0, b1, b2, b3, t4 ))
            elif data['TABLE_NAME'] == "PROPELLER_DESIGN_RESULTS":  # OK 
                sql = """
                INSERT INTO PROPELLER_DESIGN_RESULTS (PROJECT_NO, PROP_STATUS, VALUE, COMMENTS) 
                VALUES (%s, %s, %s, %s)
                """
                # 데이터 삽입
                #for entry in data:
                cursor.execute(sql, (str(data['PROJECT_NO']), str(data['PROP_STATUS']), str(data['VALUE']),str(data['COMMENTS']) ))                
            elif data['TABLE_NAME'] == "SHIP_INITIAL_DESIGN_RESULTS":  # OK
                sql = """
                INSERT INTO SHIP_INITIAL_DESIGN_RESULTS (PROJECT_NO, BASIC_SCHEME, LIGHTWEIGHT_DISTRIBUTION, GENERAL_ARRANGEMENT, RUDDER_ARRANGEMENT,TRIM_STABILITY,DAMAGE_STABILITY,
                EEDI_CALCULATION,FREEBOARD,SOLAS_VISIBILITY,TONNAGE_CAL,SRTP_RESULT,MIDSHIP_DRAWING,RULE_SCANTLING,OUTLINE_SPEC,POCKET_PLAN,REPORT_SUMMARY,PROJECT_FULL_REPORT,AIP_CERTIFICATION,
                APPENDIX_1,APPENDIX_2,APPENDIX_3,APPENDIX_4,APPENDIX_5,COMMENTS) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,  %s, %s, %s, %s, %s)
                """
                # 데이터 삽입
                #for entry in data:
                t0 = str(data['PROJECT_NO'])
                b1 = read_file_as_blob(str(data['BASIC_SCHEME'])) 
                b2 = read_file_as_blob(str(data['LIGHTWEIGHT_DISTRIBUTION'])) 
                b3 = read_file_as_blob(str(data['GENERAL_ARRANGEMENT'])) 
                b4 = read_file_as_blob(str(data['RUDDER_ARRANGEMENT'])) 
                b5 = read_file_as_blob(str(data['TRIM_STABILITY'])) 
                b6 = read_file_as_blob(str(data['DAMAGE_STABILITY'])) 
                b7 = read_file_as_blob(str(data['EEDI_CALCULATION'])) 
                b8 = read_file_as_blob(str(data['FREEBOARD'])) 
                b9 = read_file_as_blob(str(data['SOLAS_VISIBILITY'])) 
                b10 = read_file_as_blob(str(data['TONNAGE_CAL'])) 
                b11 = read_file_as_blob(str(data['SRTP_RESULT'])) 
                b12 = read_file_as_blob(str(data['MIDSHIP_DRAWING'])) 
                b13 = read_file_as_blob(str(data['RULE_SCANTLING'])) 
                b14 = read_file_as_blob(str(data['OUTLINE_SPEC'])) 
                b15 = read_file_as_blob(str(data['POCKET_PLAN'])) 
                b16 = read_file_as_blob(str(data['REPORT_SUMMARY'])) 
                b17 = read_file_as_blob(str(data['PROJECT_FULL_REPORT'])) 
                b18 = read_file_as_blob(str(data['AIP_CERTIFICATION'])) 
                b19 = read_file_as_blob(str(data['APPENDIX_1'])) 
                b20 = read_file_as_blob(str(data['APPENDIX_2'])) 
                b21 = read_file_as_blob(str(data['APPENDIX_3'])) 
                b22 = read_file_as_blob(str(data['APPENDIX_4'])) 
                b23 = read_file_as_blob(str(data['APPENDIX_5'])) 
                t24 = str(data['COMMENTS'])

                cursor.execute(sql, (t0, 
                b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
                b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,
                b21,b22,b23,t24
                 ))  
            elif data['TABLE_NAME'] == "OUTFITTING DESIGN RESULTS":  # OK
                sql = """
                INSERT INTO OUTFITTING_DESIGN_RESULTS (PROJECT_NO, MACHINARY_ARRANGEMENT, CWATER_HEAT_BALANCE, LFSS_FLOW_DIAGRAM, ACCOMODATION,MOORING_ARRANGEMENT,EQUIPMENT_NUMBER,
                ELECTRIC_LOAD,AIP_CERTIFICATION,APPENDIX_1,APPENDIX_2,APPENDIX_3,APPENDIX_4,APPENDIX_5,APPENDIX_6,APPENDIX_7,APPENDIX_8,APPENDIX_9,COMMENTS) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,    %s, %s, %s, %s, %s, %s, %s, %s , %s)
                """
                # 데이터 삽입
                #for entry in data:
                t0 = str(data['PROJECT_NO'])
                b1 = read_file_as_blob(str(data['MACHINARY_ARRANGEMENT'])) 
                b2 = read_file_as_blob(str(data['CWATER_HEAT_BALANCE'])) 
                b3 = read_file_as_blob(str(data['LFSS_FLOW_DIAGRAM'])) 
                b4 = read_file_as_blob(str(data['ACCOMODATION'])) 
                b5 = read_file_as_blob(str(data['MOORING_ARRANGEMENT'])) 
                b6 = read_file_as_blob(str(data['EQUIPMENT_NUMBER'])) 
                b7 = read_file_as_blob(str(data['ELECTRIC_LOAD']))               
                b8 = read_file_as_blob(str(data['AIP_CERTIFICATION'])) 
                b9 = read_file_as_blob(str(data['APPENDIX_1'])) 
                b10 = read_file_as_blob(str(data['APPENDIX_2'])) 
                b11 = read_file_as_blob(str(data['APPENDIX_3'])) 
                b12 = read_file_as_blob(str(data['APPENDIX_4'])) 
                b13 = read_file_as_blob(str(data['APPENDIX_5'])) 
                b14 = read_file_as_blob(str(data['APPENDIX_6'])) 
                b15 = read_file_as_blob(str(data['APPENDIX_7'])) 
                b16 = read_file_as_blob(str(data['APPENDIX_8'])) 
                b17 = read_file_as_blob(str(data['APPENDIX_9'])) 
                t18 = str(data['COMMENTS'])

                cursor.execute(sql, (t0, 
                b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
                b11,b12,b13,b14,b15,b16,b17,t18
                 )) 
            elif data['TABLE_NAME'] == "HYDRODYNAMIC_DESIGN_RESULTS":  # OK
                sql = """
                INSERT INTO HYDRODYNAMIC_DESIGN_RESULTS (PROJECT_NO, HULLFORM_DEVELOP_REPORT, LINES_IGES_WIRE, LINES_IGES_SURFACE, LINES_HOPT,LINES_DMP,LINES_STL,
                LINES_OFFSET,PNG_BIRD_EYE_VIEW,PNG_SIDE_FRONT_VIEW,ESD_DESIGN_REPORT,ESD_DRAWING,PROPELLER_DESIGN_REPORT,PROPELLER_DRAWING,RUDDER_DRAWING,SP_HYDROSTATIC_DATA,WAKE_MEASUREMENT_RESULT,SP_RESULTS_DESIGN_BARE,
                SP_RESULTS_DESIGN_ESD,SP_RESULTS_SCANT_BARE,SP_RESULTS_SCANT_ESD,SP_RESULTS_EEDI_BARE,SP_RESULTS_EEDI_ESD,SP_RESULTS_BALLAST_BARE,SP_RESULTS_BALLAST_ESD,MODEL_TEST_FULL_REPORT,CAVITATION_TEST_REPORT,APPENDIX_1,APPENDIX_2,
                APPENDIX_3,APPENDIX_4,APPENDIX_5,COMMENTS) 
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s,    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,    %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,   %s, %s, %s )
                """
                # 데이터 삽입
                #for entry in data:
                t0 = str(data['PROJECT_NO'])
                b1 = read_file_as_blob(str(data['HULLFORM_DEVELOP_REPORT'])) 
                b2 = read_file_as_blob(str(data['LINES_IGES_WIRE'])) 
                b3 = read_file_as_blob(str(data['LINES_IGES_SURFACE'])) 
                b4 = read_file_as_blob(str(data['LINES_HOPT'])) 
                b5 = read_file_as_blob(str(data['LINES_DMP'])) 
                b6 = read_file_as_blob(str(data['LINES_STL'])) 
                b7 = read_file_as_blob(str(data['LINES_OFFSET'])) 
                b8 = read_file_as_blob(str(data['PNG_BIRD_EYE_VIEW'])) 
                b9 = read_file_as_blob(str(data['PNG_SIDE_FRONT_VIEW'])) 
                b10 = read_file_as_blob(str(data['ESD_DESIGN_REPORT'])) 
                b11 = read_file_as_blob(str(data['ESD_DRAWING'])) 
                b12 = read_file_as_blob(str(data['PROPELLER_DESIGN_REPORT'])) 
                b13 = read_file_as_blob(str(data['PROPELLER_DRAWING'])) 
                b14 = read_file_as_blob(str(data['RUDDER_DRAWING'])) 
                b15 = read_file_as_blob(str(data['SP_HYDROSTATIC_DATA'])) 
                b16 = read_file_as_blob(str(data['WAKE_MEASUREMENT_RESULT'])) 
                b17 = read_file_as_blob(str(data['SP_RESULTS_DESIGN_BARE'])) 
                b18 = read_file_as_blob(str(data['SP_RESULTS_DESIGN_ESD'])) 
                b19 = read_file_as_blob(str(data['SP_RESULTS_SCANT_BARE'])) 
                b20 = read_file_as_blob(str(data['SP_RESULTS_SCANT_ESD'])) 
                b21 = read_file_as_blob(str(data['SP_RESULTS_EEDI_BARE'])) 
                b22 = read_file_as_blob(str(data['SP_RESULTS_EEDI_ESD'])) 
                b23 = read_file_as_blob(str(data['SP_RESULTS_BALLAST_BARE'])) 
                b24 = read_file_as_blob(str(data['SP_RESULTS_BALLAST_ESD'])) 
                b25 = read_file_as_blob(str(data['MODEL_TEST_FULL_REPORT'])) 
                b26 = read_file_as_blob(str(data['CAVITATION_TEST_REPORT'])) 
                b27 = read_file_as_blob(str(data['APPENDIX_1'])) 
                b28= read_file_as_blob(str(data['APPENDIX_2'])) 
                b29 = read_file_as_blob(str(data['APPENDIX_3'])) 
                b30 = read_file_as_blob(str(data['APPENDIX_4'])) 
                b31 = read_file_as_blob(str(data['APPENDIX_5'])) 
                t32 = str(data['COMMENTS'])

                cursor.execute(sql, (t0, 
                b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,
                b11,b12,b13,b14,b15,b16,b17,b18,b19,b20,
                b21,b22,b23,b24,b25,b26,b27,b28,b29,b30,b31,t32 ))                
            
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
