import timeCalculator
import mariadb
import sys
import time
stop_coord="12.89134,77.45594"
while True:
    print("Updating Webpage")
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
    cur = conn.cursor()
    cur.execute("select * from bus_location;")

    code="""<!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <link rel="stylesheet" href="css/master.css">
        <meta charset="utf-8">
        <title>Display</title>
      </head>
      <body onload="AutoRefresh(1000);">
  <script type="text/javascript">
  function AutoRefresh( t ) {
             setTimeout("location.reload(true);", t);
          }

  </script>
  <h1 >
          Kanmanike Bus Stop
        </marquee>

        <table>
          <tr>
            <th>BUS No.</th>
            <th>ETA</th>
          </tr>"""
    for (bus_no, bus_coord) in cur:
        ETAtime=timeCalculator.getTime(bus_coord.replace("|",","),stop_coord)
        code=code+"""
        <tr>
            <td>"""+bus_no+"""</td>
            <td>"""+ETAtime+"""</td>
         </tr>"""
        code=code+"""
        </table>
      </body>
    </html>
    """
    f1=open("display.html","w")
    f1.write(code)
    f1.close()
    conn.close()
    time.sleep(1)
