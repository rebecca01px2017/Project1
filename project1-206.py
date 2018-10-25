import os
import filecmp
from dateutil.relativedelta import *
from datetime import date
import datetime


def getData(file):
	inFile = open(file, "r")
	lines = inFile.readlines()
	inFile.close()

#	. rstrip

	lst=[]
	for x in lines:
		a=x.split(",")
		d={}
		first=a[0]
		last=a[1]
		email=a[2]
		clas=a[3]
		DOB=a[4]
		d={"first":first,"last":last,"email":email,"class":clas,"DOB":DOB}
		lst.append(d)
	return lst

	#HOW DO YOU NOT GET IT TO PRINT \N



def mySort(data,col):
	d={}
	sort=[]
	for x in data:
		for y in x:
			if x[y] == col:
				keyw=y
		for a in x:
			if a == keyw:
				sort.append(x[a])
	after=sorted(sort)
	firstsorted=after[0]
	for x in data:
		if x[keyw]==firstsorted:
			firstnamefirst=x["first"]
			lastnamefirst=x["last"]

	return firstnamefirst + " " + lastnamefirst

	pass

	#WHY DOES THIS RUN ON MY TEST AND NOT HERE

def classSizes(data):
	d={}
	lst=[]
	for x in data[1:]:
		c= x["class"]
		if c in d.keys():
			d[c]=d[c]+1
		else:
			d[c]=0
			d[c]=d[c]+1
	for y in d:
		a=(y,d[y])
		lst.append(a)

	sort=sorted(d.items(),key=lambda x:x[1],reverse=True)

	return sort

	pass
#ORDER?

def findMonth(a):
	d={}
	for x in a[1:]:
		birth=x['DOB']
		birth_lst=birth.split("/")
		month=birth_lst[0]
		if month in d.keys():
			d[month]=d[month]+1
		else:
			d[month]=0
			d[month]=d[month]+1

	months=d.keys()
	common=month[0]

	for items in months:
		if d[items] > d[common]:
			common = items
	return int(common)
	pass

def mySortPrint(a,col,fileName):
	file=open(fileName,'w')

	lst=[]

	for x in a:
		for y in x:
			if x[y] == col:
				keyw=y


	test=sorted(a[1:], key=lambda k: k[keyw])


	for x in test:
		first=x['first']
		last=x['last']
		email=x['email']

		file.writelines([first,",",last,",",email, '\n'])


	return None

	pass

def findAge(a):
	now = datetime.datetime.now()
	current=now.year
	length=0
	years_lst=[]
	difference=[]

	for x in a[1:]:
		birth=x['DOB']
		year=birth.split('/')
		years=year[2]
		stripped=years.strip('\n')
		years_lst.append(stripped)

	for x in years_lst:

		difference.append(current-int(x))

	sums=0

	for x in difference:
		sums=sums+x
		length=length+1

	avg=sums/length



	return round(avg)

	pass


################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ", end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),50)

	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',25)
	total += test(mySort(data2,'First'),'Adam Rocha',25)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',25)
	total += test(mySort(data2,'Last'),'Elijah Adams',25)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',25)
	total += test(mySort(data2,'Email'),'Orli Humphrey',25)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],25)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],25)

	print("\nThe most common month of the year to be born is:")
	total += test(findMonth(data),3,15)
	total += test(findMonth(data2),3,15)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,20)

	print("\nTest of extra credit: Calcuate average age")
	total += test(findAge(data), 40, 5)
	total += test(findAge(data2), 42, 5)

	print("Your final score is " + str(total))

# Standard boilerplate to call the main() function that tests all your code
if __name__ == '__main__':
    main()
