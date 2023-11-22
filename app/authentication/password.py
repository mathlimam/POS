import bcrypt as bc


class Password:


    def req_verify(password):
        '''the conditions to make a password are:
            - at least 8 characters , where two must be numbers
        '''

        letters, numbers = list("abcdefghijklmnopqrstuvwxyz"), list("0123456789")
        l = 0
        n = 0

        for p in range(len(password)):
            if password[p] in letters:
                l+=1

            
            
            elif password[p] in numbers:
                n+=1

            

            else: 
                print(f"invalid character: {password[p]}")
                return False

        
        if l>=6 and n>=2: 
            return True
        
        else:
            return False


    def hash(password):

        if Password.req_verify(password):
            try:
                
                salt = bc.gensalt()
                hashed_pw = bc.hashpw(password.encode(), salt)

                return hashed_pw.decode(), salt.decode()
            

            except Exception as e:
                return None
        
    def hash_with_salt(password, salt_req):
        if Password.req_verify(password):
            try:
                hashed_pw = bc.hashpw(password.encode(), salt_req.encode())

                return hashed_pw.decode()
            
            except Exception as e:
                return e

