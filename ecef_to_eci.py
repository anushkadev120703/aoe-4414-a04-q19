# ecef_to_eci.py
#
# Usage: python3 ecef_to_eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km
#  Convert from ECEF coordinates to ECI using the date
# Parameters:
# year = year for the date
# month = month in year
# day = day in month
# hour = hour in day
# minute = minute in hour
# second = second in minute
# ecef_x_km = ECEF x coordinate in km
# ecef_y_km = ECEF y coordinate in km
# ecef_z_km = ECEF z coordinate in km

# Output:
#  Script will output ECI x,y,z coordinates in km
#
# Written by Anushka Devarajan
# Other contributors: None
#
# Optional license statement, e.g., See the LICENSE file for the license.

# import Python modules
import math # math module
import sys # argv

# "constants"
R_E_KM = 6378.137
w=7.292115 * 10**-5 #rad/s

# helper functions

## function description
# def calc_something(param1, param2):
#   pass

# initialize script arguments
year = float('nan') 
month = float('nan') 
day = float('nan') 
hour = float('nan')
minute = float('nan')
second = float('nan')
ecef_x_km = float('nan')
ecef_y_km = float('nan')
ecef_z_km = float('nan')

# parse script arguments
if len(sys.argv)==10:
  year = float(sys.argv[1])
  month = float(sys.argv[2])
  day = float(sys.argv[3])
  hour = float(sys.argv[4])
  minute = float(sys.argv[5])
  second = float(sys.argv[6])
  ecef_x_km= float(sys.argv[7])
  ecef_y_km= float(sys.argv[8])
  ecef_z_km= float(sys.argv[9])
else:
  print(\
   'Usage: '\
   'python3 eci.py year month day hour minute second ecef_x_km ecef_y_km ecef_z_km'\
  )
  exit()

# write script below this line
if month <= 2:
    year -= 1
    month += 12

A = year // 100
B = 2 - A +(A // 4)

# fractional Julian Date
jd_frac = math.floor(365.25 * (year + 4716)) + math.floor(30.6001 * (month + 1)) + day + B - 1524.5 + hour/24 + minute/1440 + second/86400
jd= day- 32075 + 1461 *(year+4800+(month-14)/12)/4+367*(month-2-(month-14)/12*12)/12-3*((year+4900+(month-14)/12)/100)/4
t_ut1=(jd-2451545.0)/(36525)
theta_GMST = 67310.54841+(876600*60*60+8640184.812866)*t_ut1 + 0.093104*math.pow(t_ut1, 2) + math.pow(-6.2,-6)*math.pow(t_ut1,3)
# GMST in radians
GMST_mod=math.fmod(theta_GMST,360)*w
GMST_rad = math.fmod(theta_GMST*(2*math.pi/86400), (2*math.pi))-GMST_mod

#z-rotation matrix
eci_x_km= (ecef_x_km*math.cos(-GMST_rad)+ecef_y_km*math.sin(-GMST_rad))
eci_y_km=(ecef_y_km*math.cos(-GMST_rad)-ecef_x_km*math.sin(-GMST_rad))
eci_z_km=(ecef_z_km)

print(eci_x_km)
print(eci_y_km)
print(eci_z_km)
