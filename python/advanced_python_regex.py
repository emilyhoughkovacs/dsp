# note: I did have to do some manual parsing of the data.
# This approach would have to be modified for a larger dataset.

import csv

with open('faculty.csv', 'rb') as faculty:
    fy = csv.reader(faculty)
    header = fy.next()
    degrees = {}
    titles = {}
    domains = {}
    emails = []
    for name, degree, title, email in fy:
        for d in degree.split():
            d = d.translate(None, '.')
            if d in degrees:
                degrees[d] += 1
            else:
                degrees[d] = 1
        if title in titles:
            titles[title] += 1
        else:
            titles[title] = 1
        e = email.partition('@')
        if e[2] in domains:
            domains[e[2]] += 1
        else:
            domains[e[2]] = 1
        emails.append(email)
for k, v in degrees.iteritems():
    print k + ": " + str(v)
print "=============="
for k, v in titles.iteritems():
    print k + ": " + str(v)
print "=============="
print emails
print "=============="
for k, v in domains.iteritems():
    print k + ": " + str(v)