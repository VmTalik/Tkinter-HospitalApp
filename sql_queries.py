"""Скрипт с SQL запросами и данными"""
"""
========================
Создание базы данных
========================
"""
vessel_table = """CREATE TABLE IF NOT EXISTS vessel (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        vessel_name TEXT, 
                        side_number TEXT UNIQUE
                        );"""

catch_table = """CREATE TABLE IF NOT EXISTS catch (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        fish_name TEXT,
                        catch_date TEXT,
                        weight REAL,
                        vessel_id INTEGER,
                        FOREIGN KEY (vessel_id) REFERENCES vessel (id)
                        );"""
"""
===============================
Внесение данных в базу данных
===============================
"""
insert_into_add_patient = 'INSERT INTO patient (fio, birth_date, phone_number, home_address, policy, sector) ' \
                     'VALUES (%s,%s,%s,%s,%s,%s)'


"""
===============================
Запросы к базе данных
===============================
"""

select_view_patient = """SELECT fish_name, weight, catch_date, vessel_name, side_number 
                FROM catch INNER JOIN vessel
	              ON catch.vessel_id = vessel.id
               WHERE catch.weight BETWEEN {} AND {};
               """
