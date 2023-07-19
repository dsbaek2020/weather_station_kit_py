from gpiozero import MCP3008
import time
from voltage_divider import voltage_divider

adc = MCP3008(channel =1)

count = 0
values = []

resistances = [
  33000, 6570, 8200, 891,
  1000, 688, 2200, 1410,
  3900, 3140, 16000, 14120,
  120000, 42120, 64900, 21880
]

r1 = 4700
#volts = [round(voltage_divider(r1, r2, 3.3), 1) for r2 in resistances]
voltsToDegree = {} 

deg = 0
cases = len(resistances)
different = 22.5 #360/cases

for i in range(cases):
  r2 = resistances[i]
  deg = deg+different
  voltsToDegree[round(voltage_divider(r1, r2, 3.3), 1)] = deg

print("volts = {}, size = {}".format(voltsToDegree, len(voltsToDegree)))


while True:
  wind_voltage =round(adc.value*3.3, 1)
  if not wind_voltage in voltsToDegree:
    print('unknown value '+ str(wind_voltage))
#    time.sleep(1)
  else:
    print('found '+ str(wind_voltage) + ' ' + str(voltsToDegree[wind_voltage]))

  #print('wind=', wind)
  #if not wind in values:
    #values.append(wind)
    #count+=1
    #print(count, values)

