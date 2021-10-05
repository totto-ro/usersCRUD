from users_app.config.MySQLConnection import connectToMySQL

class User:
    def __init__(self, data):
        self.id = data["user_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.email = data["email"]
        self.created_at = data["created_at"]
        self.updated_at = data["updated_at"]
        
    @classmethod
    def get_all_users( cls ):
        query = "SELECT * FROM users;"
        result = connectToMySQL( "users_db" ).query_db( query )
        users = []
        for elements in result:
            users.append( cls( elements ) )
        return users

    @classmethod
    def add_data( cls, data ):
        query = "INSERT INTO users(first_name,last_name,email) VALUES(%(first_name)s,%(last_name)s,%(email)s);"
        result = connectToMySQL( "users_db" ).query_db( query, data )
        return result

    @classmethod
    def get_id( cls, data ):
        query = "SELECT* FROM users WHERE user_id=%(user_id)s;"
        result = connectToMySQL( "users_db" ).query_db( query, data )
        return cls(result[0])
        

    @classmethod
    def deleteUser( cls , data):
        query = "DELETE FROM users WHERE user_id=%(user_id)s;"
        return connectToMySQL( "users_db" ).query_db( query, data )
        

    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, updated_at=NOW() WHERE user_id=%(id)s;"
        return connectToMySQL( "users_db" ).query_db( query, data )


    