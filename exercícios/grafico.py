import matplotlib.pyplot as plt
#x = ["10m", "20m", "30m", "40m", "50m", "60m"]

#y = ["10km/h", "40km/h", "75km/h", "80km/h", "100km/h", "80km/h"]
x = [1, 4, 7, 8, 10 , 12]
y=[]
for i in x:
    #n=50*i - (100 + 20*i)
    y.append(50*i**2 - (100 + 20*i))



plt.plot(x,y)
plt.show()


