from openpyxl import Workbook
from openpyxl.reader.excel import load_workbook
import datetime

money = load_workbook('money.xlsx')
sheet = money["Sheet"]
날짜 = str(datetime.datetime.now().date())
# 가장 최근 항목을 삭제할 것인지 묻는 코드
if input("삭제하고 싶은 내역이 있으신가요?(Y/N)") == "Y":
    삭제_여부 = True
else:
    삭제_여부 = False

def 삭제(sheet):
    row = 1
    while True:
        if sheet["A" + str(row)].value == None:
            break
        else:
            row += 1
    row -= 1
    row = str(row)
    print(row)
    if row == "1":
        print("존재하는 데이터가 없습니다.")
    else:
        sheet["A" + row] = None
        sheet["B" + row] = None
        sheet["C" + row] = None
        sheet["D" + row] = None
        sheet["E" + row] = None
        sheet["F" + row] = None
    수정_여부 = input("새로운 데이터를 삽입하시겠습니까?(Y/N)")
    if 수정_여부 == "Y":
        수정_여부 = True
    else:
        수정_여부 = False
    return 수정_여부

def 삽입(sheet):
    내역 = input("돈을 어떻게 사용하셨나요?")
    받은_돈 = int(input("받은 돈은 얼마인가요?"))
    if 받은_돈 >= 1:
        사용한_돈 = 0
    else:
        사용한_돈 = int(input("얼마를 사용하셨나요?"))
    그날_남은_돈 = int(input("남은 돈은 얼마인가요?"))

    row = 1
    while True:
        if sheet["A" + str(row)].value == None:
            break
        else:
            row += 1

    if (row == 2 or sheet["F" + str((row - 1))].value == None):
        기존_전체_남은_돈 = 그날_남은_돈 + 사용한_돈 - 받은_돈
    else:
        기존_전체_남은_돈 = int(sheet["F" + str((row - 1))].value)

    if 받은_돈 == 0:
        전체_남은_돈 = 기존_전체_남은_돈 - 사용한_돈
    else:
        전체_남은_돈 = 기존_전체_남은_돈 + 받은_돈

    row = str(row)

    sheet["A" + row] = 날짜
    sheet["B" + row] = 내역
    sheet["C" + row] = 받은_돈
    sheet["D" + row] = 사용한_돈
    sheet["E" + row] = 그날_남은_돈
    sheet["F" + row] = 전체_남은_돈

# 실제로 데이터를 삭제하는 코드
# 1. 데이터가 있는 가장 아랫줄 판단
# 2. 아랫줄의 데이터를 초기화
if 삭제_여부 == True:
    수정_여부 = 삭제(sheet)
if 삭제_여부 == False or 수정_여부 == True:
    삽입(sheet)

money.save("money.xlsx")
# 용돈 기입장
# 1. 날짜
# 2. 내역
# 3. 받은 돈
# 4. 사용한 돈
# 5. 남은 돈
# money