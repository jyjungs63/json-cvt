#!/bin/bash

# 변경할 확장자 설정
old_ext="json"  # 기존 확장자
new_ext="jsn"


# 현재 디렉토리에서 확장자가 .txt인 파일들을 .md로 변경
for file in *.$old_ext; do
  # 파일이 존재하는지 확인
  if [[ -f "$file" ]]; then
    # 파일 이름에서 확장자를 제거하고 새 확장자를 붙여서 새 이름 생성
    
    new_file="${file%.*}.$new_ext"

    sed 's,//.*,,g' < "$file" > "$new_file"
    # 파일 이름 변경
    #mv "$file" "$new_file"
    echo "Json Work  $new_file finished !!!"
  fi
done

