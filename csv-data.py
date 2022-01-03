# Usefull SQL commands

# SHOW TABLE STATUS WHERE `Name` = 'test_table';
# CREATE TABLE test_table(
#    table_id INT( 10 ) NOT NULL AUTO_INCREMENT ,
#    date DATE NOT NULL DEFAULT  '2020-01-01'  ,
#    note TEXT NOT NULL ,
#    PRIMARY KEY ( table_id )
# );
# INSERT INTO `test_table` (`id`,  `date`, `note`) VALUES ('3', '2020-01-03',  'TT');
# UPDATE test_table
# SET note = 'Not Random Anymore', date = '2022-01-01'
# WHERE table_id = 2 ;

import csv

def database_viewer(file):
	with open(file, newline='') as csvfile:
		database = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in database:
			print(row)

def sql_create(file):
	with open(file, newline='') as csvfile:
		database = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in database:
			text_write("INSERT INTO `test_table` (`table_id`,  `date`, `note`) VALUES ('"+row[0]+"','"+row[1]+"','"+row[2]+"');")

def sql_update(table,file):
	database_viewer(file)
	with open(file, newline='') as csvfile:
		database = csv.reader(csvfile, delimiter=',', quotechar='"')
		for row in database:
			text_write("UPDATE "+table)
			text_write("SET note = '"+row[1]+"'")			
			text_write("WHERE table_id = '"+row[0]+"';")			

def text_write(line):
	with open('command.txt','a') as txtfile:
		txtfile.write(line)
		txtfile.write('\n')

def text_erase():
	with open('command.txt','w') as txtfile:
		txtfile.write("")	

if __name__ == "__main__":
	text_erase()
	#sql_create('data.csv')
	sql_update('test_table','data2.csv')