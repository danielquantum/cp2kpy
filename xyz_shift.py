#########################
# A python script to shift xyz coordinates by c
#########################

#Input file
item = 'LiNiO2-opt.xyz'
file_in = open(item, 'r')
c = 0.5

#Readlines
lines = file_in.readlines()

#Operatioon
n=0
list_newlines = []
for line in lines:
    if n > 1:
        linesplit = line.split()
        newz = float(linesplit[3]) + c
        newline = linesplit[0] + '     ' + linesplit[1] + '     ' + linesplit[2] + '     ' + str(newz) + '\n'
        list_newlines.append(newline)
    else:
        linesplit = line.split()
        newline = linesplit[0] + '\n'
        list_newlines.append(newline)
    n += 1
#print(list_newlines)

#Write to file
file_out = open('LiNiO2-opt-shift.xyz', 'w+')
# Write to file
for oline in list_newlines:
    file_out.write(oline)
file_out.close()