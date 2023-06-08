from utils import get_ex_class, get_statistics
import random


list_ex = get_ex_class()
random.shuffle(list_ex)

count_point = 0
count_answer = 0

for ex_class in list_ex:
    ex_class.build_question()
    user_answer = input('Ваш ответ: ')
    ex_class.user_answer = user_answer

    if ex_class.is_correct():
        print(ex_class.build_positive_feedback())

        count_point += ex_class.balls
        count_answer += 1
    else:
        print(ex_class.build_negative_feedback())

    print()

get_statistics(count_point, count_answer)
