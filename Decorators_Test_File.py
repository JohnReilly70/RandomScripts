from Decorators import code_timer_loops, add_bracket
import time
import random


'''
FUNCTION TIMER DECORATOR
'''

@code_timer_loops(10)
def testing_code_timer(number1, number2):
    time.sleep(random.randint(0, 1))


@code_timer_loops(100)
def testing_code_timer2():
    pointless = []
    for index in list(range(100000)):
        pointless.append(index)



'''
HTML TAG STRING DECORATOR
'''


@add_bracket("I") #Hard coded, not very user friendly
def bracket_test(string):
    return string



def user_bracket(tag, text): #Soft coded, user can decide what the brackets are by simple passing it in the function

    @add_bracket(tag)
    def bracket_test(string):
        return string

    return bracket_test(text)


testing_code_timer(2,2)
testing_code_timer2()
print(bracket_test("2"))
print(user_bracket("S","HELLO"))



