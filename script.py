import mysql.connector as mysql
import json, requests

#Connect to db
cnx = mysql.connect(user='root', password='root',
                              host='localhost',
                              database='testedb')

cursor = cnx.cursor()

query = 'SELECT nome FROM clientes'

cursor.execute(query)
dados = cursor.fetchall()                         

for i in dados:
    print(i[0])

#Call API
url='http://localhost:8081/api/person/get-document'
response = requests.get(url, params={'document': '123'})

print(response.content)