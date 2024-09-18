import json

# JSON 파일 경로
file_path = '1.json'

# JSON 파일 읽기
with open(file_path, 'r', encoding='utf-8') as file:
    data = json.load(file)

# 읽어온 JSON 데이터 출력
print(data)
print(f"PROJECT_NO: {data['PROJECT_NO']}")
print(f"GENERAL_INFORMATION: {data['GENERAL_INFORMATION']}")
print(f"GENERAL_INFORMATION: {', '.join(data['GENERAL_INFORMATION'])}")
