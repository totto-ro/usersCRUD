from users_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__(self, user_id, first_name, last_name, email, created_at):
        self.user_id = user_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.created_at = created_at
        
    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        results = connectToMySQL( "users_db" ).query_db( query )
        users = []
        for element in results:
            users.append( User( element['user_id'], element['first_name'], element['last_name'], element['email'], element['created_at']) )
        return users
        
        #Data comes backs as a list of dictionaries, we want to output it as a list of users objects. Dictionaries into objects.
        #Displays info (this case table of users) into the index page

    @classmethod
    def add_data( cls, data ):
        query = "INSERT INTO users(first_name,last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL( "users_db" ).query_db( query, data )
        return result

        #Takes from or puts info into/from database, and sends it to add route with a Post method, that redicts to de users 
    

    @classmethod
    def get_id( cls, dataID ):
        query = "SELECT* FROM users WHERE user_id=%(user_id)s;"
        data ={
        "user_id" : dataID
        }
        result = connectToMySQL( "users_db" ).query_db( query, data )
        return result

        #show and add data base on the ids.
        #By connecting the id with the route we can show it in the show route or
        # edit it in the edit route but with the help of the update route
        

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE user_id=%(user_id)s;"
        return connectToMySQL( "users_db" ).query_db( query, data )

    #send info towards update route
    

    @classmethod
    def destroy( cls, numID ):
        query = "DELETE FROM users WHERE user_id=%(user_id)s;"
        data ={
        "user_id" : numID
        }
        result = connectToMySQL( "users_db" ).query_db( query, data )
        return result
