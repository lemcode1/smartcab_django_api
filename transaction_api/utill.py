import mysql.connector
import pyqrcode
import png
import Dbutil
from pyqrcode import QRCode

def generate_QR(DriverID,Drivername, Drivermobileno,DriverVehicleNo, DriverLicenceNo, DriverAddress):
       QRCodeString="Name: " + Drivername + "\n Mobile : " + Drivermobileno + "\n Vehicleno:"+ DriverVehicleNo + "\n Licenceno:" + DriverLicenceNo + "\n Address:" + DriverAddress
       url = pyqrcode.create(QRCodeString)
       url.svg(str(DriverID)+".svg", scale=8)
       url.png(str(DriverID)+'.png', scale=6)

db_conn = Dbutil.get_db_conn()

cursor_obj=db_conn.cursor()

query= "select * from pythonproject.driver_details";
cursor_obj.execute(query)
driver_info=cursor_obj.fetchall()
db_conn.close()
for driver in driver_info:
    generate_QR(driver[0],driver[1],driver[2],driver[4],driver[3],driver[5])
