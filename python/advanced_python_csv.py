import csv

with open('faculty.csv', 'rb') as faculty:
    with open('emails.csv', 'wb') as emails:
        fy = csv.reader(faculty)
        wr = csv.writer(emails)
        header = fy.next()
        for name, degree, title, email in fy:
            wr.writerow([email])