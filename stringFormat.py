# -*- coding: utf-8 -*-
# Использование %
print('------ Использование % ------------')
print('В команде "Мастера кода" участников: %(team1_num)d!' % {"team1_num":5})
print('Итого сегодня в командах участников: %(team1_num)d и %(team2_num)d!' % {"team1_num":5, "team2_num":6})

# Использование .format
print('------ Использование .format ------')
print('Команда "Волшебники данных" решила задач: {score2}!'.format(score2=42))
print('"Волшебники данных" решили задачи за {team1_time:7.1f} с!'.format(team1_time=18015.2))

# Использование f-строк
print('------ Использование f-строк ------')
# Входные данные
team1_name = "Мастера кода"
team2_name = "Волшебники данных"
team1_num = 6  # Количество участников
team2_num = 6
score_1 = 40  # Количество решённых задач
score_2 = 42
team1_time = 1552.512  # Общее время
team2_time = 2153.31451
time1_avg = team1_time / score_1  # Среднее время на 1 задачу
time2_avg = team2_time / score_2
# Вычисление результата игры
if score_1 > score_2 or (score_1 == score_2 and team1_time < team2_time):
    challenge_result = 'Победа команды \"' + team1_name + '\"!'
elif score_1 < score_2 or (score_1 == score_2 and team1_time > team2_time):
    challenge_result = 'Победа команды \"' + team2_name + '\"!'
else:
    challenge_result = "Ничья"
# Вывод результатов
print(f'Соревнуются команды:       |\"{team1_name:12s} \"| \"{team2_name:12s}\"|')
print(f'Количество решённых задач: |   {     score_1:12d}|        {score_2:12d}|')
print(f'Затраченное время:         |   {team1_time:12.5f}|  {team2_time:18.5f}|')
print(f'Среднее время на 1 задачу: |   { time1_avg:12.5f}|    {time2_avg:16.5f}|')
print('-'*65)
print(f'Результат игры: {challenge_result}')
