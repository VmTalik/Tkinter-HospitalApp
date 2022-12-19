from mysql.connector import connect, Error


class HospitalBase:
    def __init__(self):
        self.connection = None

    def connect(self, user_name='root', user_password=''):
        try:
            self.connection = connect(
                host="localhost",
                user=user_name,
                password=user_password,
                database="Hospital",
                port="3306"
            )
            print('Успешно подключились к базе данных')
        except Error as e:
            print(e)
        return self.connection
