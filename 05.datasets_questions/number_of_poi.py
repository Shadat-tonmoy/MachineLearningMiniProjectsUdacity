file = open("poi_names.txt","r")
text = file.read()
persons = text.split()
numberOfPOI = 0
# for person in persons:
#     if person=="(y)":
#         numberOfPOI+=1
# print numberOfPOI
print len(persons)