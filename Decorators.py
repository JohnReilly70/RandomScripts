from functools import wraps
import time

def code_timer_loops(num_loops):

    def code_timer(test_func):

        @wraps(test_func)
        def timer_wrapper(*args, **kwargs):

            time_list = []
            for loop in range(num_loops):
                time_1 = time.time()
                run_test_func = test_func(*args, **kwargs) #
                time_2 = time.time() - time_1
                time_list.append(time_2)
            avg_time = sum(time_list)/len(time_list)

            print("Function: {}\nAverage Time: {}\nNumber Of Loops:{}\n".format(test_func.__name__, avg_time, num_loops))
            return run_test_func

        return timer_wrapper

    return code_timer


def add_bracket(bracket_type):

    def bracket(func):

        @wraps(func)
        def bracket_wrapper(*args):

            string = func(*args)

            return "<{0}>{1}</{0}>".format(bracket_type,string)

        return bracket_wrapper

    return bracket
