from Decorators import code_timer_loops
import time
import random

@code_timer_loops(10)
def testing_code_timer(number1, number2):
    time.sleep(random.randint(0, 1))


@code_timer_loops(100)
def testing_code_timer2():
    pointless = []
    for index in list(range(100000)):
        pointless.append(index)


testing_code_timer(2,2)
testing_code_timer2()



