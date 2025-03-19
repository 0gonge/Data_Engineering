FROM python:3.9

RUN pip install pandas

# 컨테이너 내부에서 작업 디렉토리를 /app으로 설정
# 이후 실행되는 명령어들은 모두 /app 디렉토리에서 실행
WORKDIR /app
# 현재(호스트) 디렉토리에 있는 pipeline.py 파일을 컨테이너의 /app/pipeline.py로 복사
COPY pipeline.py pipeline.py

ENTRYPOINT [ "bash" ]