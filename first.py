from flask import Flask,jsonify,request
from flask_mysqldb import MySQL

app=Flask(__name__)


Bike_part = [ ]

show_id=[]

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='cars24@123'
app.config['MYSQL_DB']='Bike_part'
mysql=MySQL(app)

# All data show 
@app.route('/database',methods=['GET'])
def mysql_data():
    cur=mysql.connection.cursor()
    cur.execute('''SELECT * FROM part''')
    cre=cur.fetchall()
    cur.close()
    show_id.append(cur)
    return jsonify(cre)

# Only id data is show
# @app.route('/id/<int:id>')
# def all_id(id):
#     for q in show_id:
#         if q['id'] == id:
#             return jsonify(q)
        
# Create new data 
@app.route('/create',methods=['POST'])
def create_data():
    if request.method == 'POST':

        
        data=request.get_json()
        name=data.get('name')
        garde=data.get('garde')
        price=data.get('price')
        id=len(Bike_part)
        
        

        cur=mysql.connection.cursor()
        q=cur.execute("INSERT INTO part (name, garde, price, id)VALUES(%s,%s,%s,%s)",(name,garde,price,id))
        mysql.connection.commit()
        Bike_part.append(q)
        cur.close()

        return jsonify({'message':'data is successfully add'}),201
    else:
        return jsonify({'error':'not add'}),405

@app.route('/api/<name>',methods=['DELETE'])

@app.route('/api/<name>', methods=['DELETE'])
def delete(name):
    cursor = mysql.connection.cursor()
    cursor.execute("drop table if exists {}".format(name))
    mysql.connection.commit()
    cursor.close()
    return jsonify({'message': 'Table {} deleted successfully'.format(name)})


# mycursor=mydb.cursor()

# insert="insert into part(name,garde,price,id) values(%s,%s,%s,%s)"



# Bike_part = [
#     {
#         "name":"gaurav",
#         "grade":"A1",
#         "price":123
#     }
# ]

# mycursor.executemany(insert,my_data)
# mydb.commit()
# print(mycursor.rowcount,("record inserted"))

# flask api

# @app.route('/part')
# def all_part():
#     return jsonify({'part':Bike_part})

# @app.route('/id/<int:id>')
# def all_id(id):
#     for q in Bike_part:
#         if q['id'] == id:
#             return jsonify(q)


# @app.route('/name/<string:name>')
# def name_part(name):
#     for parts in Bike_part:
#         if parts['name'] == name:
#             return jsonify(parts)
        
# @app.route('/grade/<string:grade>')
# def grade_part(grade):
#     for i in Bike_part:
#         if i['grade']==grade:
#             return jsonify(i)
         

# @app.route('/price/<int:price>')
# def price_part(price):
#     for n in Bike_part:
#         if n['price']==price:
#             return jsonify(n)
                
#     return jsonify({'message':'data not found'})


# how to create new data
# @app.route('/part/<int:id>')
# def id_data():
#     return Bike_part[id]

# @app.route('/part',methods=['POST'])
# def create_new():
#     data=request.get_json()
#     new_file={"name":data["name"],"id":len(Bike_part),"grade":data["grade"],"price":data["price"]}
#     Bike_part.append(new_file)
#     # return new_file,201

#     return jsonify(new_file),201





@app.delete('/part/<int:id>')
def delete_data(id):
    del Bike_part[id]
    return jsonify({"message":"data is delete"}),200


if __name__ == "__main__":
    app.run(debug=True)