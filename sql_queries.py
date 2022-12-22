"SQL запросы"

"""
Внесение данных в базу данных
"""

insert_into_add_patient = 'INSERT INTO patient (fio, birth_date, phone_number, home_address, policy, sector) ' \
                     'VALUES (%s,%s,%s,%s,%s,%s)'


"""
Запросы к базе данных
"""


# выборка по заданному диапазону веса
select_patient_data = """SELECT fio, birth_date, phone_number, home_address,policy, sector
                           FROM patient
                          WHERE patient_id = {};
                        """

select_doctor_examination = """SELECT med_examination_id, med_examination_date, visit_purpose, complaint
                                 FROM med_examination
                                 WHERE patient = {};
                            """


select_disease = """SELECT disease_id, disease_type ,injury
                      FROM disease;
                  """


select_sick_list = """SELECT * FROM sick_list
                              WHERE patient = {};"""

select_shift = """SELECT shift_date, shift_time, fio, speciality
                    FROM shift
                    JOIN doctor
                      ON shift.shift_id = doctor.shift
                      WHERE doctor_id = {}; """