import mysql.connector


def c_airport_finder(c):
    """
    Fetches all the airport of the area code entered.
    :param c: Area code
    :return: Airport(s) located in country with the area code entered
    """
    sql = (f"SELECT name, type FROM airport WHERE iso_country = '{c}' ORDER BY type")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        for row in result:
            print(row)



connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='dbuser',
        password='1234',
        autocommit=True,
    )

while True:
    u_input = input("Enter Area Code: ")
    if u_input == "EXIT PROGRAM".casefold():
        print("-Program Ended-")
        break
    else:
        c_airport_finder(u_input)
        print("=" * 80)
