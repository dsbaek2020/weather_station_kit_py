from voltage_divider import voltage_divider


resistances = [
  33000, 6570, 8200, 891,
  1000, 688, 2200, 1410,
  3900, 3140, 16000, 14120,
  120000, 42120, 64900, 21880
]

for r2 in resistances:
  print(r2, voltage_divider(4700, r2, 3.3))



