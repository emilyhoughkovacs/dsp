# Hint:  use Google to find python function
from datetime import datetime
import dateutil.relativedelta

####a) 
date_start1 = '01-02-2013'  
date_stop1 = '07-28-2015'   

####b)  
date_start2 = '12312013'  
date_stop2 = '05282015'  

####c)  
date_start3 = '15-Jan-1994'  
date_stop3 = '14-Jul-2015'  

def date_diff(date1, date2):
	try:
		date1 = datetime.fromtimestamp(int(date1))
		date2 = datetime.fromtimestamp(int(date2))
	except ValueError:
		try: 
			date1 = datetime.strptime(date1, '%m-%d-%Y')
			date2 = datetime.strptime(date2, '%m-%d-%Y')
		except ValueError:
			date1 = datetime.strptime(date1, '%d-%b-%Y')
			date2 = datetime.strptime(date2, '%d-%b-%Y')
	date_diff = date2-date1
	print date_diff.days

print "mm-dd-yyyy:"
date_diff(date_start1, date_stop1)
print
print "timestamp"
date_diff(date_start2, date_stop2)
print
print "dd-mon-yyyy:"
date_diff(date_start3, date_stop3)