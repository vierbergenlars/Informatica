# Dit programma formatteert de gegeven seconden naar het formaat uu:mm:ss
# 2013 02 14

inp = int(raw_input('Tijd in seconden: '))

hours = inp//(60*60)
while(hours >= 24):
    hours -= 24
mins = (inp%(60*60)//60)
secs = inp%60

print "Tijd: ", hours, ":", mins, ":", secs
