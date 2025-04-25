import sys
from PyQt6.QtWidgets import *
from PyQt6.QtGui import *
from PyQt6 import uic
from sympy import sympify, SympifyError


from_class = uic.loadUiType("Calculator.ui")[0]

class CalculatorClass(QMainWindow, from_class):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Calculator")

        self.pushButton_0.clicked.connect(self.input_zero)
        self.pushButton_1.clicked.connect(lambda: self.input_nonzero_digit("1"))
        self.pushButton_2.clicked.connect(lambda: self.input_nonzero_digit("2"))
        self.pushButton_3.clicked.connect(lambda: self.input_nonzero_digit("3"))
        self.pushButton_4.clicked.connect(lambda: self.input_nonzero_digit("4"))
        self.pushButton_5.clicked.connect(lambda: self.input_nonzero_digit("5"))
        self.pushButton_6.clicked.connect(lambda: self.input_nonzero_digit("6"))
        self.pushButton_7.clicked.connect(lambda: self.input_nonzero_digit("7"))
        self.pushButton_8.clicked.connect(lambda: self.input_nonzero_digit("8"))
        self.pushButton_9.clicked.connect(lambda: self.input_nonzero_digit("9"))
        self.pushButton_plus.clicked.connect(lambda: self.input_operator("+"))
        self.pushButton_sub.clicked.connect(lambda: self.input_operator("-"))
        self.pushButton_mul.clicked.connect(lambda: self.input_operator("*"))
        self.pushButton_div.clicked.connect(lambda: self.input_operator("/"))
        self.pushButton_mod.clicked.connect(lambda: self.input_operator("%"))
        self.pushButton_sign.clicked.connect(self.input_reverse_sign)
        self.pushButton_dot.clicked.connect(self.input_dot)
        self.pushButton_all_clear.clicked.connect(self.input_all_clear)
        self.pushButton_clear.clicked.connect(self.input_clear)
        self.pushButton_equal.clicked.connect(self.input_equal)

        self.calculation_string = "0"
        self.prev_text = ""
        self.equal_onetime_check = False
        self.prev_display_onetime_check = False

        self.display()


###############################    처리 함수    ###############################
    def input_zero(self):
        self.reset_display_info()

        if self.equal_onetime_check:
            self.calculation_string = "0"
        else:
            if len(self.calculation_string) >= 2:
                if ((self.calculation_string[-2] in ('+', '-', '/', '%', '*')) and (self.calculation_string[-1] == '0')):
                    pass
                else:
                    self.calculation_string += "0"
            else:
                if self.calculation_string != "0":
                    self.calculation_string += "0"
        
        self.reset_equal_check("0")
        self.display()


    def input_nonzero_digit(self, input_char:str):
        self.reset_display_info()

        if self.equal_onetime_check:
            self.calculation_string = input_char
        else:
            if len(self.calculation_string) >= 2:
                if((self.calculation_string[-2] in ('+', '-', '/', '%', '*')) and (self.calculation_string[-1] == '0')):
                    self.calculation_string = self.calculation_string[:-1] + input_char
                else:
                    self.calculation_string += input_char                  
            elif self.calculation_string == "0":
                self.calculation_string = input_char
            else:
                self.calculation_string += input_char

        self.reset_equal_check(input_char)
        self.display()


    def input_operator(self, input_char:str):
        self.reset_display_info()   

        if (len(self.calculation_string) == 1) and (self.calculation_string[0] == '-'):
            pass
        elif (len(self.calculation_string) >= 2) and (self.calculation_string[-2] in ('+', '-', '/', '%', '*') and self.calculation_string[-1] == '-'):
            pass
        elif self.calculation_string[-1] in ('+', '-', '/', '%', '*'):
            self.calculation_string = self.calculation_string[:-1] + input_char
        else:
            self.calculation_string += input_char

        self.reset_equal_check(input_char)
        self.display()             


    def input_reverse_sign(self):
        self.reset_display_info()

        if (len(self.calculation_string) == 1) and (self.calculation_string[0] == "0"):
            self.calculation_string = "-"  
        elif (len(self.calculation_string) == 1) and (self.calculation_string[0] == "-"):
            self.calculation_string = "0" 
        else:
            # '-'는 부호로 쓰일 수 있어서 제외
            last_op_idx = max(self.calculation_string.rfind(op) for op in ('+', '*', '/', '%'))

            current_number_start = last_op_idx + 1 if last_op_idx != -1 else 0
            current_number = self.calculation_string[current_number_start:]

            if current_number.startswith('-'):  # 현재 숫자가 -로 시작하면 제거 (음수 → 양수)
                if '-' not in current_number[1:] and current_number[0] == '-':
                    self.calculation_string = (self.calculation_string[:current_number_start] + current_number[1:])
            elif '-' in current_number:
                pass
            else:
                self.calculation_string = (self.calculation_string[:current_number_start] + '-' + current_number)

        self.reset_equal_check("-")
        self.display()


    def input_dot(self):
        self.reset_display_info()

        # 연산자 위치 파악: 가장 최근 연산자의 인덱스 찾기
        last_op_idx = max(self.calculation_string.rfind(op) for op in ('+', '-', '/', '%', '*'))

        if last_op_idx != -1: # 연산자가 있었다면, 그 연산자 다음부터가 대상 숫자임
            current_number_start = last_op_idx + 1
        else:
            current_number_start = 0 # 연산자가 없다면, 전체 수식이 하나의 숫자니까 시작은 0

        current_number = self.calculation_string[current_number_start:]


        if self.equal_onetime_check:
            self.calculation_string = "0."
        else:
            if self.calculation_string[-1] in ('+', '-', '/', '%', '*'):
                self.calculation_string += "0."
            elif '.' in current_number:
                pass # current_number에 이미 소수점이 있는 숫자면 무시
            else:
                self.calculation_string += '.'

        self.reset_equal_check(".")
        self.display()


    def input_all_clear(self):
        self.reset_display_info()

        self.calculation_string = "0"
        self.prev_text = ""
        self.prev_display_onetime_check = False

        self.reset_equal_check("a")
        self.display()


    def input_clear(self):
        self.reset_display_info()

        if len(self.calculation_string) == 1: 
            self.calculation_string = "0" # 한 자리수이면 0으로 초기화.
        else:
            self.calculation_string = self.calculation_string[:-1]

        self.reset_equal_check("c")
        self.display()


    def input_equal(self):
        self.reset_display_info()

        # 수식이 연산자로 끝나는 경우 → 잘못된 수식
        if self.calculation_string[-1] in ('+', '-', '/', '%', '*'):
            pass

        else:
            try:                
                result = sympify(self.calculation_string).evalf() # 수식 계산

                # 계산 불가한 값 필터링
                if str(result) in ("zoo", "oo", "-oo", "nan"):
                    self.prev_text = "Cannot be divided by zero."
                    self.calculation_string = "0"
                    self.equal_onetime_check = True
                    self.prev_display_onetime_check = False                    

                else:
                    self.prev_text = self.calculation_string + ' ='

                    # 정상 계산 결과 처리                    
                    if float(result).is_integer():
                        self.calculation_string = str(int(result)) # 정수 형태면 .0 제거
                    else:
                        self.calculation_string = f"{float(result):g}" # 만약, 소수점이 길다면 필요한 것만 출력

                    self.equal_onetime_check = True
                    self.prev_display_onetime_check = False

            except ZeroDivisionError:
                self.prev_text = "Cannot be divided by zero."
                self.calculation_string = "0"         
                self.equal_onetime_check = True
                self.prev_display_onetime_check = False                                

            except Exception:
                self.prev_text = "Unknown ERROR. Please retry"
                self.calculation_string = "0"         
                self.equal_onetime_check = True
                self.prev_display_onetime_check = False                   
                

        self.reset_equal_check("=")
        self.display()



###############################    처리 함수    ###############################



###############################    그 외 함수    ###############################
    def display(self):
        self.lineEdit_curr.setText(self.calculation_string)
        self.lineEdit_prev.setText(self.prev_text)

    def reset_equal_check(self, input_char: str):
        if input_char != '=' and self.equal_onetime_check:
            self.equal_onetime_check = False

    def reset_display_info(self):

        # 수식 완성 후 입력이 있을 때 or 처음 시작 후 입력이 있을 때 Ans 출력.
        if self.prev_display_onetime_check == False:
            self.prev_text = "Ans = " + self.calculation_string
            self.prev_display_onetime_check = True
###############################    그 외 함수    ###############################


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindows = CalculatorClass()
    myWindows.show()
    sys.exit(app.exec())