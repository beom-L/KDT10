## ====================================================================
##              Python GUI Programming - TKinter 
## ====================================================================
## Container Layout : Pack
##   * 왼쪽/오른쪽/위/아래/가운데로 지정된 위치에 UI요소 배치
##   * grid()와 같이 사용될 수 없음. place()와 같이 사용할 수 있음
##   * 배치되는 우선 순위
##      - 가장 처음 선언한 pack부터 배치
##      - pack의 매개변수로 인하여 위젯의 크기가 변경될 수 있음
##   * 사용법
##     위젯이름.pack(매개변수1, 매개변수2, 매개변수3, ...)
##   * 주요 매개변수
##     side   : 해당 구역으로 위젯을 이동시킴
##              'left', 'right', 'top', 'bottom'
##     anchor : 현재 배치된 구역 안에서 특정 위치로 이동시킴.
##        n (north): 위젯을 셀의 상단에 붙임
##        e (east) : 위젯을 셀의 오른쪽에 붙임
##        s (south): 위젯을 셀의 하단에 붙임
##        w (west) : 위젯을 셀의 왼쪽에 붙임 
##        nw (north-west): 위젯을 셀의 왼쪽 상단에 붙임
##        ne (north-east): 위젯을 셀의 오른쪽 상단에 붙임
##        sw (south-west): 위젯을 셀의 왼쪽 하단에 붙임
##        se (south-east): 위젯을 셀의 오른쪽 하단에 붙임
##     fill   : 할당된 공간에 맞게 크기가 변경됨
##     expand : 할당되지 않은 미사용 공간 모두 현재 위젯의 할당된 공간으로 변경
## ====================================================================

## --------------------------------------------------------------------
## 모듈 로딩 
## --------------------------------------------------------------------
import tkinter

## --------------------------------------------------------------------
##- 윈도우 관련 
## --------------------------------------------------------------------
##- 윈도우 창 인스턴스 생성 및 설정
window=tkinter.Tk()
window.title("LAYOUT_PACK")
window.geometry("640x400+100+100")
window.resizable(False,False)


## --------------------------------------------------------------------
##- 윈도우에 배치될 UI요소들 - Button 요소
## --------------------------------------------------------------------
## - 버튼 인스턴스 생성
b1=tkinter.Button(window, text="top")
b1_1=tkinter.Button(window, text="top-1")

b2=tkinter.Button(window, text="bottom")
b2_1=tkinter.Button(window, text="bottom-1")

b3=tkinter.Button(window, text="left")
b3_1=tkinter.Button(window, text="left-1")

b4=tkinter.Button(window, text="right")
b4_1=tkinter.Button(window, text="right-1")

b5=tkinter.Button(window, text="center", bg='red')

## - 버튼 인스턴스를 화면에 pack 방식으로 자동 배치
## - [기본] 버튼위에 text가 보여질 만큼 W,H 크기로 버튼 배치
b1.pack(side='top')                 ## fill은 채우기 -> 없으니깐 글짜가 보일만큼만 채우기
b1_1.pack(side='top', fill='x')     ## side='top'인 경우 가로(x축) 공간만 확장 가능함

b2.pack(side='bottom')
b2_1.pack(side='bottom', anchor='e')

b3.pack(side='left')
b3_1.pack(side='left', fill='y')

b4.pack(side='right')
b4_1.pack(side='right', anchor='s')

# b5.pack()                           ## [기본] side='top', anchor='center'
# b5.pack(expand=True, fill='both')   ## both : 양쪽으로, expand : 확장해줘  -> 전체 공간 모두 사용
b5.pack(expand=True)                ## 가운데 위치

## --------------------------------------------------------------------
##- 윈도우에서 발생하는 사용자 이벤트 수신
## --------------------------------------------------------------------
##- 종료 전까지 동작
window.mainloop()