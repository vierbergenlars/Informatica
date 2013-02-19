# Negeer al die try en except zever, dat is gewoon om effe fouten te vermijden
#
invoer = raw_input("Tekst voor de invoer > ")

print "Invoer: "
print invoer, "type: ",
print type(invoer) # Welk is het type van deze variabele?

# Omzetten naar een int

try:
    print "Omzetten naar int: "
    omgezet = int(invoer)
    print omgezet, "type: ",
    print type(omgezet)
# // Negeer onderstaand
except ValueError: 
    print "Oké, dat kan duidelijk geen int zijn!" 

# Of naar een float
try:
    print "Omzetten naar float: "
    omgezet = float(invoer)
    print omgezet, "type: ",
    print type(omgezet)
# // Negeer onderstaand
except ValueError:
    print "Oké, dit is geen float"
