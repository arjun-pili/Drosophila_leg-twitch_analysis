import csv
import matplotlib.pyplot as plt

l1=[]
l2=[]
l3=[]
l4=[]
t=[]

with open('MLP.csv','r') as csvf:
    plots=csv.reader(csvf,delimiter=',')
    
    for row in plots:
        t.append(row[0])
        l1.append(row[1])
        l2.append(row[2])
        l3.append(row[3])
        l4.append(row[4])
plt.title('LEG MOVEMENT')
plt.xlabel('TIME')
plt.ylabel('DISTANCE')
plt.plot(t,l1,'r')
plt.plot(t,l2,'b')
plt.plot(t,l3,'b')
plt.plot(t,l4,'r')
plt.savefig('leg_movement.png')
plt.show()
