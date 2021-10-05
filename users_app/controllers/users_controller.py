# endpoints related to the users

from flask import render_template, redirect, request
from users_app import app
from users_app.models.User import User

@app.route( "/users", methods=['GET'] )
def getAllUsers():
    users = User.get_all_users()
    return render_template( "index.html", users=users )

@app.route( "/users/new", methods=['GET'] )
def displayAddNewUser():
    return render_template("new_users.html")


@app.route( "/users/add", methods=['POST'] )
def add_user():
    User.add_data(request.form)
    return redirect("/users")

@app.route("/users/edit/<id>", methods=['GET'])
def edit(id):
    id = int(id)
    data ={
        "user_id" : id
    }
    users = User.get_id(data)
    return render_template("edit_users.html", users=users)

@app.route("/users/update", methods=['POST'])
def update():
    User.update(request.form)
    print(request.form)
    return redirect("/users")

@app.route("/users/delete/<id>", methods=['GET'])
def deleteUser(id):
    id = int(id)
    data ={
        "user_id" : id
    }
    User.deleteUser(data)
    print(request.form)
    return redirect("/users")

@app.route("/users/show/<id>", methods=['GET'])
def show(id):
    id = int(id)
    data ={
        "user_id" : id
    }
    users = User.get_id(data)
    return render_template("show_user.html", users=users)





