momsSats = 0.25

prisUtanMoms = input("Mata in pris i kr, utan moms: ")
moms = float(prisUtanMoms) * momsSats
print("Moms: ", moms)
prisMedMoms = moms + float(prisUtanMoms)
print("Pris med moms: ", prisMedMoms)