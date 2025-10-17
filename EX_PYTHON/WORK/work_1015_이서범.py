##
import tkinter

## 윈도우 창 만들기
window = tkinter.Tk()
window.title("게산기")
window.geometry('800x800')

## 버튼 레이블 정의 (4x4 격자)
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

## 함수 만들기
def calc():
    pass

def cellButton(cell):
    if cell == '00':
        return 1
    elif cell == '01':
        return 2
    elif cell == '02':
        return 3
    elif cell == '03':
        return '+'
    elif cell == '01':
        return 4
    elif cell == '02':
        return 5
    elif cell == '03':
        return 6
    elif cell == '03':
        return '-'
    elif cell == '01':
        return 7
    elif cell == '02':
        return 8
    elif cell == '03':
        return 9
    elif cell == '03':
        return '*'
    elif cell == '01':
        return 0
    elif cell == '02':
        return 5
    elif cell == '03':
        return 6
    elif cell == '03':
        return '-'


## - 전역변수
ROWS = 4
COLS = 4

## 인스턴스 생성
# 세로 3등분  => weight=1 행별 동일한 값 설정 즉, 균등
for r in range(ROWS):
    # window.grid_rowconfigure(r, weight=1, uniform="row")
    window.grid_rowconfigure(r,weight=1, uniform="row")  ## 행별로 다른값 부여

# 가로 3등분  => weight=1 컬럼별 동일한 값 설정 즉, 균등
for c in range(COLS):
    window.grid_columnconfigure(c, weight=1, uniform="col")


## Grid 실행
for r in range(ROWS):
    for c in range(COLS):
        cell = f'{r}{c}'
        button = cellButton(cell)
        f = tkinter.Button(window, text=f'{button}')
        f.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)
    f.grid



## 반복 실행
window.mainloop()


## ===============================================
import tkinter
from tkinter import messagebox

## 윈도우 창 만들기
window = tkinter.Tk()
window.title("계산기")
window.geometry('400x500')
window.resizable(False, False)

## - 전역변수
# StringVar 대신 사용할 일반 문자열 변수 (입력 값을 추적하는 용도)
current_expression = "" 

## 위젯 생성
# 입력 필드 (Entry 위젯)
entry_field = tkinter.Entry(window, bd=10, width=14)
entry_field.grid(row=0, column=0, columnspan=4, sticky='nsew', padx=5, pady=5)


## 버튼 레이블 정의 (4x4 격자)
button_labels = [
    ('7', '8', '9', '/'),
    ('4', '5', '6', '*'),
    ('1', '2', '3', '-'),
    ('C', '0', '=', '+')
]

ROWS = 5 # Entry 필드 (0) + 버튼 (4) = 5
COLS = 4

## 함수 만들기
# 입력 필드를 초기화하는 함수
def clear_entry():
    global current_expression
    current_expression = ""
    # Entry 위젯의 0 인덱스부터 끝(END)까지 모든 텍스트를 삭제합니다.
    entry_field.delete(0, 'end')

# 수식을 계산하는 함수
def calc():
    global current_expression

    # Entry 위젯의 현재 텍스트를 가져와 수식으로 사용
    expression = entry_field.get()
    result = eval(expression)   ## str을 진짜 연산자로 바꿔주는것
    
    # 계산 결과를 Entry 위젯에 설정
    clear_entry() # 기존 내용을 지우고
    entry_field.insert(0, str(result)) # 결과를 0 인덱스에 삽입
    current_expression = str(result) # 전역 변수도 결과로 업데이트


# 버튼 클릭 시 호출되는 함수
def click_button(label):
    global current_expression
    
    # 'C' (Clear) 버튼이 눌렸을 때
    if label == 'C':
        clear_entry()
    # '=' (Equal) 버튼이 눌렸을 때
    elif label == '=':
        calc()
    # 숫자 또는 연산자 버튼이 눌렸을 때
    else:
        # 전역 변수에 레이블을 추가
        current_expression += label
        # Entry 위젯의 끝(END)에 레이블을 삽입하여 화면에 표시
        entry_field.insert(tkinter.END, label)


## 인스턴스 생성 및 Grid 설정

# 전체 행 설정: Entry 필드 (row 0)는 고정 높이, 나머지 버튼 행 (row 1~4)은 균등 분배
window.grid_rowconfigure(0, weight=0)    # Entry 필드
for r in range(1, ROWS):                 # 버튼 행 (1, 2, 3, 4)
    window.grid_rowconfigure(r, weight=1, uniform="row")

# 가로 설정: 4개의 컬럼 모두 균등 분배
for c in range(COLS):
    window.grid_columnconfigure(c, weight=1, uniform="col")


## Grid 실행 (버튼 생성 및 배치)
# 버튼은 row 1부터 시작합니다.
for r in range(len(button_labels)):
    for c in range(len(button_labels[r])):
        label = button_labels[r][c]
        
        # 버튼 위젯 생성
        button = tkinter.Button(
            window, 
            text=label, 
            font=('Arial', 18), 
            bg='#f0f0f0',
            # 클릭 시 동작 함수 연결
            command=lambda l=label: click_button(l) 
        )
        
        # 버튼을 그리드에 배치 (Entry 필드 아래인 row r+1 부터 시작)
        button.grid(row=r+1, column=c, sticky='nsew', padx=2, pady=2)


## 반복 실행
window.mainloop()