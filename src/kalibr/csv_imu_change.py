import csv
import io
r = csv.reader(open('imu.csv')) # Here your csv file
lines = list(r)
print(len(lines))
print(type(lines))
print(type(lines[0]))

for i in lines:
    i[1] = float(i[1]) * 3.1415926535897 * (1/180.0)
    i[2] = float(i[2]) * 3.1415926535897 * (1/180.0)
    i[3] = float(i[3]) * 3.1415926535897 * (1/180.0)
	
with io.open("imu0.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(lines)

