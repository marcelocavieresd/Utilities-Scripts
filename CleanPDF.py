"""Script developed by Marcelo Cavieres, Unab student, Santiago-Chile"""

print "Note: This script take as root folder in the running"
ruta = raw_input("From: ")
rutadestino = raw_input("To: ")
try:
    f = open(ruta, "r")
    d = open(rutadestino, "w")
    for x in f:
        if "/Producer" not in x:
            d.write(x)
    d.close()
    f.close()
    print "*** Metadata were deleted ***"
    print "Clean file was saved in: ",rutadestino
