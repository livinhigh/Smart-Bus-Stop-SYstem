"""
Keep running this code, it will keep updating the location of the bus in the database
"""

import vehicles as v
import time
import mariadb
import sys
print("Getting Route")
try:
    conn = mariadb.connect(
        user="admin",
        password="password",
        host="localhost",
        port=3306,
        database="iot"

    )
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cur = conn.cursor()
points=v.get_points_along_path("AIzaSyBPBiXDpPPLX_w2FYUx-w-A_6rshINox3c","Kengeri","Bidadi")
listOfkeys=list(points.keys())
print("Starting the bus")
time.sleep(3)
for i in listOfkeys:
    coord=str(points[i][0])+"|"+str(points[i][1])
    cur.execute("update bus_location set gps_coord=\""+coord+"\" where bus_no=\"BUS1\";")
    conn.commit()
    print("reached "+coord)
    time.sleep(1)
