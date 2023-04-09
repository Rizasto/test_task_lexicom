import random
import string
import psycopg2
import time


conn = psycopg2.connect(dbname='test', user='postgres', password='postgres', host='localhost')

#Функция для генерации случайных строк заданной длины
def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


cursor = conn.cursor()

#Заполнение БД случайными названиями и статусом
def fill_data(cursor, names):
    cursor.execute('CREATE TABLE short_name '
                   '(NAME TEXT NOT NULL PRIMARY KEY,'
                   'STATUS INT NULL);')
    cursor.execute('CREATE TABLE full_name '
                   '(NAME TEXT NOT NULL PRIMARY KEY,'
                   'STATUS INT NULL);')

    unique_list = []
    for counter in range(700000):
        name = generate_random_string(6)
        status = random.randint(0, 1)
        if name not in unique_list:
            unique_list.append(name)
            cursor.execute(f'INSERT INTO short_name (name, status) VALUES (%s, %s);', (name, status))
            conn.commit()

    for i in names:
        name = i[0] + '.' + generate_random_string(random.randint(1, 4))
        status = random.randint(0, 1)
        cursor.execute(f'INSERT INTO full_name (name, status) VALUES (%s, %s);', (name, None))
        conn.commit()

cursor.execute('SELECT name, status FROM short_name ORDER BY name;')
names = cursor.fetchall()
cursor.execute('SELECT name FROM full_name ORDER BY name;')
names_second = cursor.fetchall()


#UPDATE статуса в соответствии с названием
start = time.time()
counter = 0
for item in names:
    while item[0] != names_second[counter][0].split('.')[0]:
        counter += 1
    sql = 'UPDATE full_name SET status = %s WHERE name = %s'
    args = [item[1], names_second[counter][0]]
    cursor.execute(sql, args)
    counter += 1
conn.commit()
end = time.time() - start


