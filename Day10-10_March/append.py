file=open('JECRC.txt', 'a+')

# file.write("JECRC is the world's best university")
# file.write("JECRC is also popular for its placements")


file.writelines([
    '\nhere food is amazing\n',
    '\nhere faculty is very supportive\n'
])
file.seek(0)

print(file.read())


file.close()