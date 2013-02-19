# Vraagt de gebruiker om een jaartal en bepaalt of dat jaar een schrikkeljaar is
# 2013 02 13

jaartal = int(input("Geef een jaartal: "))

is_veelvoud_4 = ((jaartal % 4) == 0)
is_veelvoud_100 = ((jaartal % 100) == 0)
is_veelvoud_400 = ((jaartal % 400) == 0)

if is_veelvoud_4 and ((not is_veelvoud_100) or is_veelvoud_400):
    print "Schrikkeljaar"
else:
    print "Geen schrikkeljaar"
