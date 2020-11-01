import vehicles as v
import time
import random
points=v.get_points_along_path("AIzaSyBPBiXDpPPLX_w2FYUx-w-A_6rshINox3c","Kengeri","Bidadi")
listOfkeys=list(points.keys())
f1=open("stopGenerated.txt",'w')
for i in range(0,len(listOfkeys),int((len(listOfkeys)/20))):
    print(points[listOfkeys[i]])
    f1.write("insert into stop_info values(\"stop"+str(i)+"\",\""+str(points[listOfkeys[i]][0])+"|"+str(points[listOfkeys[i]][1])+"\",\"STOP "+str(i)+"\");\n")
for i in range(0,len(listOfkeys),int((len(listOfkeys)/20))):
    f1.write("insert into route_stops(route_no,stop_id) values(\"ROUTE1\",\"stop"+str(i)+"\");\n")

f1.close()
