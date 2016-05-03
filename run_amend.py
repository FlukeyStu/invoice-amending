# SB 16/3/16
# SRK018776
import os
import shutil
completed_folder = 'completed/'
name = ''
address1 = ''
address2 = ''
address3 = ''
city = ''

fileName = raw_input('enter file name: ')
existing_file = open(fileName, 'rb')
data = existing_file.read()
with open('newfile.txt','w') as newFile:
	newFile.write(data)
	
tempFile = open('newfile.txt','rb')
	
count = 0
for line in tempFile:
	count += 1
	if count == 88:
		name = line.split('>')[2].split('<')[0]
		print name
	elif count == 96:
		address1 = line.split('>')[2].split('<')[0]
		print address1
	elif count == 104:
		address2 = line.split('>')[2].split('<')[0]
		print address2
	elif count == 112:
		address3 = line.split('>')[2].split('<')[0]
		print address3
	elif count == 120:
		city = line.split('>')[2].split('<')[0]
		print city
	
tempFile.close()
os.remove('newfile.txt')

changes = [('ACCOUNTS PAYABLE', name),('Electrical Emporium', address1),('Link House',address2),('Bute Street',address3),('Staffordshire',city),('ST4 3PR', ' '),('R K Wholesale Limited', 'Electrical  Emporium'), ('Sutton House','Link House'),('Berry Hill Ind Estate, Berry Hill Rd','Bute Street, Fenton'),('ST4 2NL','ST4 3PR'),("TV's","TVs"),('Dishwashers and large TVs (20" & Over) are not returnable as in-house guarantee applies. Please revert to manual.',' '),('Sales', ' '),(' - ', ' '),('0844 826 9361', ' '), ('0844 826 9363', ' '), ('0844 826 9354', ' '),('Accounts', ' '),('Fax No.', ' ')]

for change in changes:
	data = data.replace(change[0],change[1])

data = data.replace('Goods remain the property of  Electrical  Emporium  until paid for in full', ' ')
new_file_name = 'Edited ' + fileName.split('.')[0] + '.html'
with open(new_file_name,'wb') as file:
	file.write(data) 

existing_file.close()
if not os.path.exists(completed_folder):
	os.mkdirs(completed_folder)
shutil.move(existing_file.name, completed_folder)
