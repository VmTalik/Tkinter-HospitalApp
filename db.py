from mysql.connector import connect, Error


class HospitalBase:
    def __init__(self):
        self.connection = None
        self.connect()

    def connect(self):
        try:
            self.connection = connect(
                host="localhost",
                user="root",
                database="Hospital",
                port="3306"
            )
            print('Успешно подключились к базе данных')
        except Error as e:
            print(e)
