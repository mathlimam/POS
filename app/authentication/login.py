from users.tools import Tools as user_tools
from authentication.password import Password as pw


class Auth:
    

    def compare_password(username, password_to_compare):
        
        try:
            user = user_tools.read(username=username)
            salt = user[4]
            password = user[3]


            hashed_pw_to_compare = pw.hash_with_salt(password=password_to_compare, salt_req=salt)


            if password == hashed_pw_to_compare: 
                return True
            
            else: 
                return False

        except Exception as e:

            return e


    def login(username, password):
        if user_tools.exists(username=username) is not None:
            if Auth.compare_password(username,password):
                return True
        
        else:
            return False



