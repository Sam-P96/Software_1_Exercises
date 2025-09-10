import mysql.connector


# the ICAO is ident in the airport table
def icao_to_airport(icao):
    """
    Fetches the name of the airport with the assigned input ICAO code
    :param icao: ICAO code of the airport being looked up
    :return: name of the airport
    """
    sql = (f"SELECT name FROM airport WHERE ident = '{icao}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    # print(sql)
    if cursor.rowcount > 0 :
        for row in result:
            print(f"{icao}: {row[0]}")
    else:
        print("No airport found with that ICAO code.")
    return



connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='dbuser',
        password='1234',
        autocommit=True
        )

while True:
    user_entry = input("Please enter an ICAO: ")
    # user_entry = "WSSS"
    if user_entry == "EXIT PROGRAM".casefold():
        print("-Program Ended-")
        break
    else:
        icao_to_airport(user_entry)
        print("=" * 80)