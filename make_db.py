import sqlite3

conn = sqlite3.connect('test.db')

# conn.execute('''DROP TABLE tes;''')
# conn.execute('''drop table subs;''')
# conn.execute('''drop table marks;''')

conn.execute('''
    create table if not exists tes 
    (id INTEGER not null PRIMARY KEY autoincrement,
    name text not null, 
    mother INTEGER default 1);''')

conn.execute('''
    create table if not exists subs 
    (id INTEGER not null primary key autoincrement,
    name text not null,
    love INTEGER default 0,
    tes_id INTEGER not null,
    foreign key (tes_id) references tes(id)
    );
''')

conn.execute('''
    create table if not exists marks 
    (id INTEGER not null primary key autoincrement,
    mark INTEGER not null,
    sub_id INTEGER not null,
    date_time text default 'date', 
    foreign key (sub_id) references subs(id)
    );
''')

conn.commit()
conn.close()
