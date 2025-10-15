##
import tkinter

## 윈도우 창 만들기
window = tkinter.Tk()
window.title("게산기")
window.geometry('800x800')

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


for r in range(ROWS):
    for c in range(COLS):
        f = tkinter.Button(window, text=f'cell_{r}')

        # - 컬럼병합(columnspan)으로 1행에 1개 Label 배치
        # - 행 크기만큼 widget 늘려서 채우기  : sticky='nsew'
        # - 행과 행 사이 여백 공간 설정       : pady, padx
        f.grid(row=r, column=c, sticky='nsew', padx=2, pady=2)



## Grid 실행



## 반복 실행
window.mainloop()