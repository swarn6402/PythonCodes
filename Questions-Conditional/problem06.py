Distance_kms = 14
Transport = " "

if Distance_kms < 3:
    Transport = "Walking"

elif Distance_kms < 15:
    Transport = "Bike"

elif Distance_kms > 15:
    Transport = "Car"

print("Based on distance:", Distance_kms, "Your mode of transport is:", Transport)