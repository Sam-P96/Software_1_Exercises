import mysql.connector
from geopy.distance import geodesic


connection = mysql.connector.connect(
        host='127.0.0.1',
        port= 3306,
        database='flight_game',
        user='dbuser',
        password='1234',
        autocommit=True,
    )

def c_airport_select(c):
    """
    Fetches all the airport of the area code entered.
    :param c: Area code
    :return: Airport(s) located in country with the area code entered
    """
    sql = (f"SELECT name, longitude_deg, latitude_deg FROM airport WHERE ident = '{c}'")
    cursor = connection.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    if cursor.rowcount > 0:
        return result


# print(c_airport_select("WSSS"))
# print(c_airport_select("VDPP"))
# returns a list of tuples
print("Enter 2 ICAO codes, and I will tell you how far apart they are")
icao_a = input("Enter the first ICAO code: ")
icao_a_t = c_airport_select(icao_a)
icao_b = input("Enter the second ICAO code: ")
icao_b_t = c_airport_select(icao_b)

# note to self: geopy uses latitude longitude, not the other way round.
ll_a = float(icao_a_t[0][2]), float(icao_a_t[0][1])
print(ll_a)
ll_b = float(icao_b_t[0][2]), float(icao_b_t[0][1]),
print(ll_b)

distance_km = geodesic(ll_a, ll_b).kilometers

print(f"Distance between {icao_a_t[0][0]} and {icao_b_t[0][0]}:")
print(f"{distance_km:.2f} km")

