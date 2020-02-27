import mysql.connector

#here we should connect to free mysqlDB containing english dictionary'
con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)

cursor = con.cursor()

word = input('Enter your word, please: ')

query = cursor.execute('SELECT * FROM Dictionary WHERE Expression = "%s"' %word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print('Sorry, I can not find this word :c')