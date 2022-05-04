# CSV파일 읽기
import csv

file_name = './Busan bus_211231.csv'

f = open(file_name, mode='r', encoding='cp949')
reader = csv.reader(f, delimiter=',')   # 구분자가 ,일 경우

next(reader)  #제목줄이 있을때 필요없을경우

for line in reader:
    print(line)

f.close()   ## 필수!!