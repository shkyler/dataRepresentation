# testing CSV functions
import csv

employee_file = open('employee_file.csv', mode='w')
employee_writer = csv.writer(employee_file, delimiter=',',quotechar='"', quoting=csv.QUOTE_MINIMAL)

employee_writer.writerow(['Paddy Moore', 'Production', 'March'])
employee_writer.writerow(['Anthony Dooley', 'Maintenacne', 'November'])

employee_file.close()