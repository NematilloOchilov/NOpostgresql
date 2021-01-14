""" Men Nematillo Ochilov python dasturlash tilida 3 yil va PostgreSQL MOBTda 3 oylik tajribaga ega dasturchiman.
    MOBT - ma'lumotlar omborini boshqarish tizimi
    Ma'lumotlarni fayllarda saqlash maqbul yechim emas.
    Ma'lumotlarni ma'lumotlar omborida saqlash tavsiya etiladi.
    SQL bu ma'lumotlar bazasida ishlash uchun foydalaniladigan so'rov tili.
    Ma'lumotlar omborini boshqarish tizimlari: SQLite, MySQL, PostgreSQL, MSSQL, Oracle va boshqalar.
    PostgreSQL - bu relyatsion ma'lumotlar omborini boshqarish tizimi.
    psycopg2 - Python dasturlash tili uchun eng mashhur PostgreSQL MOBT adapteri.
    pip3 install psycopg2-binary buyrug'ini terminalga yozish orqali kompyuterga ushbu adapterni o'rnatish mumkin"""

import psycopg2


def base(sql):  # Ushbu funksiya MOdan foydalanish uchun yoziladigan kodlarni ixchamlashtirish uchun yaratilgan
    try:
        conn = psycopg2.connect(user="postgres",
                                host="answerdb-1.c5bne3vsdefk.us-east-2.rds.amazonaws.com",
                                password='adgjmp77',
                                port="5432",
                                database="postgres")
        if 'select' in sql.lower() and 'from' in sql.lower():
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            read = cur.fetchall()
            cur.close()
            conn.close()
            return read
        else:
            cur = conn.cursor()
            cur.execute(sql)
            conn.commit()
            cur.close()
            conn.close()
    except Exception as e:
        print(str(e))


# Ma'lumotlar turlari haqida batafsil  https://www.tutorialspoint.com/postgresql/postgresql_data_types.htm



