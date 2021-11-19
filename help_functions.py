import sqlite3


def mean_mark_of_les(lesson):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.execute(f'''select AVG(mark) from marks
                                where sub_id = (select id from subs
                                    where name='{lesson}')
                              ''')
        avg_mark = list(cursor)[0][0]
        if not avg_mark:
            raise ValueError('Не найден предмет')
        conn.close()
        return round(avg_mark, 2)
    except ValueError as error:
        # print(str(error))
        return str(error)


def lesson_from_tes(teacher):
    try:
        conn = sqlite3.connect('test.db')
        cursor = conn.execute(f'''select name from subs
                                where tes_id = (select id from tes
                                    where name='{teacher}')
                              ''')
        lesson = list(cursor)
        if not lesson:
            raise ValueError('Не найден учитель или он не ведёт уроков')
        conn.close()
        return lesson[0][0], True
    except ValueError as error:
        # print(str(error))
        return str(error), False


# print(lesson_from_tes('Репгангста'))
