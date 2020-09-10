# Originally completed May 27/2020
#importing file
!curl https://raw.githubusercontent.com/MicrosoftLearning/intropython/master/world_temp_mean.csv -o mean_temp.txt

#addition of new entry
mean_temp = open('mean_temp.txt','a+')
new_line = "Rio de Janeiro,Brazil,30.0,18.0\n"
mean_temp.write(new_line)
print("\n")

#create header
mean_temp.seek(0)
header = mean_temp.readline().strip().split(',') #note: strip the newline char

#remainder of data
city_temp = []
line = mean_temp.readline().strip()
while line:
    city_temp += line.split(',')
    line = mean_temp.readline().strip()
    
#printing out the data
length2 = int(len(city_temp)/4)
ctr = 0
while ctr != length2:
    print(header[0],"of",city_temp[0+ctr*4],header[2],"is",city_temp[2+ctr*4],"Celcius")
    ctr += 1

#close file
mean_temp.close()
