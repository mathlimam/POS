from .controller.user_controller import User as uc



from database.connection import conn as c


class Tools:
    @staticmethod
    def exists(user_id=None, username=None):
        '''
         Checks if a user exists in the users database. This is a helper function to make it easier to use in tests
         
         @param user_id - The id of the user to check
         @param username - The username of the user to check
         
         @return True if the user exists False if it doesn't or an exception if something went wrong during the
        '''
        try:
            conn = c('./database/users.db')
            cursor = conn.cursor()

            # Returns the user id of the user
            if username is not None:
                query = 'SELECT id FROM users WHERE username = ?'
                cursor.execute(query, (username,))
                result = cursor.fetchone()
                return result

            # Returns the username of the user
            if user_id is not None:
                query = 'SELECT username FROM users WHERE id = ?'
                cursor.execute(query, (user_id,))
                result = cursor.fetchone()
                return result

        except Exception as e:
            return e

        finally:
            conn.close()

    @staticmethod
    def create(name, username, password, perm_level):
        '''
         Create a USER account if it doesn't exist. This is a wrapper around user controller. create that handles exceptions that occur during creation
         
         @param name - The name of the account
         @param username - The username to use for the account ( required )
         @param password - The password to use for the account ( required )
         @param perm_level - The permission level to use ( 0 = admin 1 = admin 2 = superuser )
         
         @return None on success error message on failure. Example :. from fabtools import create uc = uc. create ( " john "
        '''
        # Create a new user if not already exists.
        if Tools.exists(username=username) is None:
            try:
                uc.create(name, username, password, perm_level)
            
            except Exception as e:
                return e

    @staticmethod
    def read(user_id=None, username=None):
        '''
         Read data from user's data store. This is a wrapper for uc. read that checks if the user exists before reading data
         
         @param user_id - ID of user to read data for
         @param username - Name of user to read data for ( optional )
         
         @return List of data read from data store ( s ) or empty list if not found ( default ) or
        '''
        # Returns a list of users.
        if Tools.exists(user_id=user_id, username=username) is not None:
            return list(uc.read(user_id=user_id, username=username))
        else:
            print('User not found')

    @staticmethod
    def update(user_id, name=None, username=None, password=None, perm_level=None):
        '''
         Update user's information. This is a wrapper around uc. update that handles exceptions gracefully. If you don't care about exceptions please report them to the developer.
         
         @param user_id - User's id to update.
         @param name - User's new name. Default is None.
         @param username - User's new username. Default is None.
         @param password - User's new password. Default is None.
         @param perm_level - User's permission level. Default is None.
         
         @return None on success or exception on failure. Example :. import fabtools >>> fabtools. update ( 7 ) Traceback ( most recent call last ) : UserAlreadyOwnedException : Unable to update user's own information
        '''
        try:
            uc.update(user_id=user_id, name=name, username=username, password=password, perm_level=perm_level)
        except Exception as e:
            return e

    @staticmethod
    def delete(user_id=None, username=None):
        '''
         Delete a user from UC. This will delete the user's data and all data associated with it
         
         @param user_id - User ID to delete from UC
         @param username - Username of user to delete from UC.
         
         @return None on success Exception on failure. Usage : fab. delete ( [ user_id ] [ username ]
        '''
        try:
            # Delete the user from the database
            if Tools.exists(user_id=None, username=username) is not None:
                uc.delete(user_id=user_id, username=username)
        except Exception as e:
            return e


print(Tools.create("matheus", "Lima", "alicein99", "1"))