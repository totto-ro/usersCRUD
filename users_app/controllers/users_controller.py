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
    return render_template("new_users.html") #Just displays the new_users html page
                                                #with the spaces to fill the form and send info to the database
                                                #that will come from the add route that its connected in the form too   



@app.route( "/users/add", methods=['POST'] )
def add_user():                         #Process the info that comes from the new route through the form
    User.add_data(request.form)
    return redirect("/users")           #receives the data from the model User function add_data,
                                        #stores it in the database and redircts towards the index page

@app.route("/users/show/<int:id>", methods=['GET'])     
def show(id):
    dataID = id
    user = User.get_id(dataID)
    print(user)
    return render_template("show_user.html", users=user[0])

@app.route("/users/edit/<int:id>", methods=['GET'])     #Just displays the page that its link to an id
def edit(id):
    dataID = id
    user = User.get_id(dataID)
    print(user)
    return render_template("edit_users.html", users=user[0])


@app.route("/users/update", methods=['POST']) #actually changes and updates the users from the edit route
def update():                                 #with the form help and a hidden id
    User.update(request.form)
    print(request.form)
    return redirect("/users")


@app.route("/users/destroy/<int:id>", methods=['GET'])
def destroy(id):
    numID = id
    User.destroy( numID )
    return redirect('/users')







