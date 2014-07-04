#author: Paul Dolan
#date: July 2014

import pymongo
import sys

connection_string = "mongodb://localhost"
connection = pymongo.MongoClient(connection_string)
db = connection.students

scores = db.grades

def drop_lowest():
	print "Droping lowest, started"
	#this will return all documents with the type = homework
	query = {'type':'homework'}
	
	#here a sort is done on the query which will output the results by student_id and then score in ascending order, 
	#i.e from lowest to highest
	try:
		cursor = scores.find(query).sort([('student_id',pymongo.ASCENDING),('score',pymongo.ASCENDING)])
	
	except:
		print "Unexpected error:", sys.exc_info()[0]
		
	
	
	#initialize pointer to zero
	student = 0
	
	#loop through each document in the collection where the query is equal to 'cursor'
	for doc in cursor:
	
		#check to see if the student_id is equal to the value of the pointer, e.g 'student_id':0 == 0
		#there will be two document where student_id = 0, however we will only delete the first one.  The next time
		#the loop checks the pointer will have been incremented, therefore we move over the second instance where 
		#student_id = 0 and onto the first instance of student_id =1, and so on!
		if doc['student_id'] == student:
		
			#if true remove this document from the collection
			scores.remove(doc)
			
			#increment the pointer by 1
			student += 1
			
#call the function		
drop_lowest()
