import random
import pymysql
import sys

conn = pymysql.connect(host='127.0.0.1',
                             user='*',
                             password='*',
                             db='*',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

i = ['Алексей','Игорь','Александр','Сергей','Антон','Николай','Андрей','Владимир','Станислав','Эдуард']     #Здесь можно поставить
f = ['Иванов','Смирнов','Соболев','Петров','Сидоров','Свечников','Пономарев','Серов','Щеткин','Свистулькин']#любые 10 значений
lst = []
x = 0

#Генерация списка случайных записей из i и f
while x != 1000000:
    lst.append(tuple([i[random.randint(0,9)], f[random.randint(0,9)], 'ТЕСТ', random.randint(10000,100000)]))
    lst.append(', ')
    x += 1
    print (x)
lst.pop()
print('Размер массива',sys.getsizeof(lst), 'bytes')

#Преобразование списка в строку
t = ''
t = t.join(map(str,lst))
print('Размер строки',sys.getsizeof(t), ',bytes')

try:
    with conn.cursor() as cursor:
        sql = """INSERT INTO `your_table`(`column`, `column`, `column`, `column`) VALUES {}""".format(t)  #Подстановка строки t
        cursor.execute(sql)

    conn.commit()

finally:
    conn.close()

#На генерацию и запись 1000000 значений у меня было затрачено ~ 4 мин 30 сек