from starbase import Connection

c = Connection("127.0.0.1", "8000")

ratings = c.table('ratings')



print ("Get back ratings for some users...\n")
print ("Ratings for user ID 1:\n")
print (ratings.fetch("1"))
print ("Ratings for user ID 33:\n")
print (ratings.fetch("33"))

ratings.drop()
print("Parsing the ml-100k ratings data...\n")
ratingFile = open("e:/Downloads/ml-100k/ml-100k/u.data", "r")
