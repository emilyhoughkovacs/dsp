import csv
from collections import defaultdict
from operator import itemgetter

faculty_dict = defaultdict(list)
professor_dict = {}
with open('faculty.csv', 'rb') as fac:
    faculty = csv.reader(fac)
    header = faculty.next()
    for name, degree, title, email in faculty:
        first = name.split()[0]
        sur = name.split()[-1]
        faculty_dict[sur].append([degree, title, email])
        professor_dict[(first, sur)] = [degree, title, email]
# print faculty_dict
# print professor_dict
for key in sorted(professor_dict.keys(), key=itemgetter(1))[0:3]:
    print str(key)+": "+str(professor_dict[key])