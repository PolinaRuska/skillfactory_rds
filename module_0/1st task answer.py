#!/usr/bin/env python
# coding: utf-8
​
# ## Проект 0. GitHub. Угадай число.
​
# Алгоритм бинарного поиска: 
# 1. Находим середину отсортированного массива.
# 2. Сравниваем ее с искомым значением: если предсказанное число меньше загаданного, отсекаем левую часть, если больше, отсекаем правую.
# 3. Повторяем, пока не найдем загаданное число. 
​
# **Код NataliaDein**
​
# In[24]:
​
​
import numpy as np
​
​
def score_game(game_core):
    '''We start the game 1000 times to find out how quickly the game guesses the number'''
    count_ls = []
    np.random.seed(1)  # RANDOM SEED :  so the experiment could be reproducible
    random_array = np.random.randint(1,101, size=(1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Your algorithm guesses the average number per {score} attempts")
    return(score)
​
​
def game_core_v3(number):
    '''As a predict we take always the middle of the interval.
       In depend of the comparison the lowest limit (limit_min) or the highest limit (limit_max) 
       will be appropriate moved, until the solution will be found.'''
    count = 1
    limit_min = 0
    limit_max = 101
    predict = (limit_min+limit_max) // 2
    while number != predict:
        count+=1
        if number > predict:
            limit_min = predict
        else: 
            limit_max = predict
        predict = (limit_min+limit_max) // 2
    return(count) # Return the count of attemptions from the function, if the number is guessed
​
​
# Check:
score_game(game_core_v3)
