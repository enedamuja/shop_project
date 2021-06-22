from flask import Flask, render_template, redirect, url_for, request, flash
import sqlite3
import urllib.request

app = Flask(__name__)
@app.route("/")  # this sets the route to this page

def home():
	return render_template("faqapar.html", len= len(toy_quantity), toy_quantity = toy_quantity, toy_catalogue = toy_catalogue, toy_price = toy_price, toy_category = toy_category)   # some basic inline html


@app.route('/addprodkk', methods =["GET", "POST"])

def swichtologin():
	return render_template("page.html")

@app.route('/basketadd', methods =["GET", "POST"])

def add_to_basket():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()

	a = request.form.get("emrib")
	b = request.form.get("kategb")
	c = request.form.get("numrib")
	print(a)

	sql = "INSERT INTO basket (toy_name, toy_price, toy_quantity) VALUES (?, ?, ?);"
	val = (a, b, c)
	cursor.execute(sql, val)
	conn.commit()
	print(cursor.rowcount, "record inserted.")
	return home()

@app.route('/basketii', methods =["GET", "POST"])

def list_of_basket_prod():

	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()
    # Extracting from the database the list of product names from the basket table and inserting the data into the list
	cursor.execute("SELECT toy_name FROM basket")
	global toy_catalogue_basket
	toy_catalogue_basket = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_catalogue_basket.append(i)

	# Extracting from the database the list of product prices from the basket table and inserting the data into the list
	cursor.execute("SELECT toy_price FROM basket")
	global toy_price_basket
	toy_price_basket = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    i = str(i).replace("$", "")
	    i = int(i)
	    toy_price_basket.append(i)

	# Extracting from the database the list of products quantities from the basket table and inserting the data into the list
	cursor.execute("SELECT toy_quantity FROM basket")
	global toy_quantity_basket
	toy_quantity_basket = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    i = int(i)
	    toy_quantity_basket.append(i)

	global totalsum
	totalsum = []

	for i, j in zip(toy_quantity_basket, toy_price_basket):
		x = i * j
		totalsum.append(x)
	print(totalsum)



list_of_basket_prod()

@app.route('/basketiaa', methods =["GET", "POST"])


def swichtobasket():
	list_of_basket_prod()
	return render_template("basket.html", totalsum = sum(totalsum), len= len(toy_catalogue_basket), toy_catalogue_basket=toy_catalogue_basket, toy_price_basket = toy_price_basket, toy_quantity_basket =toy_quantity_basket)
@app.route('/rmbask', methods =["GET", "POST"])

def remove_product():
	nametorem = request.form.get("toynamehid")
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()
	sql = "DELETE FROM basket WHERE ? = (toy_name);"
	val = (nametorem,)
	cursor.execute(sql, val)
	conn.commit()
	print(cursor.rowcount, "record deleted.")
	return swichtobasket()


@app.route('/swichlogout', methods =["GET", "POST"])

def logout():
	return home()

@app.route('/', methods =["GET", "POST"])

def gfg():

    #taking the username credentials and uploading to the username list
    if request.method == "POST":
		

	    conn = sqlite3.connect('database.db')
	    cursor = conn.cursor()
	    conn.commit()
	    #taking the username credentials and uploading to the username list
	    global username
	    username = []
	    cursor.execute("SELECT username FROM useri")
	    for i in cursor:
	        i = str(i).replace("(", "")
	        i = str(i).replace(")", "")
	        i = str(i).replace(",", "")
	        i = str(i).replace("'", "")
	        username.append(i)

	    #taking the password credentials and uploading to the password list
	    global password
	    password = []
	    cursor.execute("SELECT password FROM useri")
	    for j in cursor:
	        j = str(j).replace("(", "")
	        j = str(j).replace(")", "")
	        j = str(j).replace(",", "")
	        j = str(j).replace("'", "")
	        password.append(j)

	    x = request.form.get("fname")
	    z = request.form.get("lname")
	    
	    i = 0
	    while i < len(username):
	        # print(i)
	        if x == username[i] and z == password[i]:
	            return swap_to_addprod()
	            break
	        elif x != username[i]and z != password[i]:
	            return render_template("page.html", urname = "failed")
	        elif x == username[i] and z != password[i]:
	        	return render_template("page.html", urname = "failed")
	        else:
	            return render_template("page.html", urname = "failed")
	        i = i + 1
		
def list_of_prod():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()
	cursor.execute("SELECT toy_name FROM product")
	global toy_catalogue
	toy_catalogue = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_catalogue.append(i)

	# Extracting from the database the list of product prices from the basket table and inserting the data into the list
	cursor.execute("SELECT toy_price FROM product")
	global toy_price
	toy_price = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    i = "$" + i
	    toy_price.append(i)

	# Extracting from the database the list of products quantities from the basket table and inserting the data into the list
	cursor.execute("SELECT toy_category FROM product")
	global toy_category
	toy_category = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_category.append(i)

	    # Extracting from the database the list of products quantities from the basket table and inserting the data into the list
	cursor.execute("SELECT toy_quantity FROM product")
	global toy_quantity
	toy_quantity = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_quantity.append(i)

list_of_prod()


@app.route('/addprod', methods =["GET", "POST"])

def insert_prod():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()

	

	toy_ID = request.form.get("toy_ID")
	toy_name = request.form.get("toy_catalogue")
	toy_category = request.form.get("toy_category")
	toy_quantity = request.form.get("toy_quantity")
	toy_discription = request.form.get("toy_description")
	toy_price = request.form.get("toy_price")
	toy_image = request.form.get("toy_image")

	filename = "static/dollimages/" + toy_name + ".png"
	urllib.request.urlretrieve(toy_image, filename)

	sql = "INSERT INTO product (toy_ID, toy_name, toy_category, toy_price, toy_quantity, toy_discription) VALUES (?, ?, ?, ?, ?, ?)"
	val = (toy_ID, toy_name, toy_category, toy_price, toy_quantity, toy_discription)
	cursor.execute(sql, val)
	conn.commit()
	print(cursor.rowcount, "record inserted.")

	return swap_to_addprod()

def full_list_of_prod():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()
	global toy_category
	toy_category = []
	cursor.execute("SELECT toy_category FROM product")
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_category.append(i)
	#print(toy_categoty)
	# Extracting from the database the list of product names and inserting the data into the list
	cursor.execute("SELECT toy_name FROM product")
	global toy_catalogue
	toy_catalogue = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_catalogue.append(i)

	# Extracting from the database the list of product prices and inserting the data into the list
	cursor.execute("SELECT toy_price FROM product")
	global toy_price
	toy_price = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    i = "$" + i
	    toy_price.append(i)

	# Extracting from the database the list of products quantities and inserting the data into the list
	cursor.execute("SELECT toy_quantity FROM product")
	global toy_quantity
	toy_quantity = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_quantity.append(i)

	# Extracting from the database the list of product ID's and inserting the data into the list
	cursor.execute("SELECT toy_ID FROM product")
	global toy_ID
	toy_ID = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_ID.append(i)

	cursor.execute("SELECT toy_discription FROM product")
	global toy_description
	toy_description = []
	for i in cursor:
	    i = str(i).replace("(", "")
	    i = str(i).replace(")", "")
	    i = str(i).replace(",", "")
	    i = str(i).replace("'", "")
	    toy_description.append(i)

full_list_of_prod()

def swap_to_addprod():
	full_list_of_prod()
	return render_template("addprod.html", len= len(toy_quantity), toy_description = toy_description,  toy_ID = toy_ID,  toy_quantity = toy_quantity, toy_catalogue = toy_catalogue, toy_price = toy_price, toy_category = toy_category)

@app.route('/delprod', methods =["GET", "POST"])


def swaptodelprod():
	full_list_of_prod()
	return render_template("delprod.html", len= len(toy_quantity), toy_description = toy_description,  toy_ID = toy_ID,  toy_quantity = toy_quantity, toy_catalogue = toy_catalogue, toy_price = toy_price, toy_category = toy_category)

@app.route('/deletingprod', methods =["GET", "POST"])

def delete_prod():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()

	prod_id = request.form.get("toy_ID")
	sql = "DELETE FROM product WHERE toy_ID = ?"
	cursor.execute(sql, (prod_id,))
	conn.commit()
	print(cursor.rowcount, "record(s) deleted")
	return swaptodelprod()

@app.route('/editprod', methods =["GET", "POST"])

def swaptoeditprod():
	full_list_of_prod()
	return render_template("editprod.html", len= len(toy_quantity), toy_description = toy_description,  toy_ID = toy_ID,  toy_quantity = toy_quantity, toy_catalogue = toy_catalogue, toy_price = toy_price, toy_category = toy_category)

@app.route('/editingprod', methods =["GET", "POST"])

def edit_product():
	conn = sqlite3.connect('database.db')
	cursor = conn.cursor()
	conn.commit()

	toy_ID = request.form.get("toy_ID")
	toy_name = request.form.get("toy_catalogue")
	toy_category = request.form.get("toy_category")
	toy_quantity = request.form.get("toy_quantity")
	toy_discription = request.form.get("toy_description")
	toy_price = request.form.get("toy_price")
	toy_image = request.form.get("toy_image")
	oldid = request.form.get("oldid")

	sql = "UPDATE product SET toy_id= ?, toy_name= ?, toy_category= ?, toy_price= ?, toy_quantity= ?,toy_discription= ? WHERE toy_id = ?"
	val = (toy_ID, toy_name, toy_category, toy_price, toy_quantity, toy_discription, oldid)
	cursor.execute(sql, val)
	conn.commit()
	return swaptoeditprod()

@app.route('/addprodu', methods =["GET", "POST"])

def swaptoaddprod():
	full_list_of_prod()
	return render_template("addprod.html", len= len(toy_quantity), toy_description = toy_description,  toy_ID = toy_ID,  toy_quantity = toy_quantity, toy_catalogue = toy_catalogue, toy_price = toy_price, toy_category = toy_category)





if __name__ == "__main__":
    app.run(port="5002")