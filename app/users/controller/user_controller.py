from database.connection import conn as c
from authentication.password import Password as p


class User:
    DB = "./database/users.db"
    def __init__(self, name, username, password, permission_level):

        '''
         Initializes the object with the given parameters. This is the constructor for the class. You can call it from any class that inherits from
         
         @param name - The name of the user
         @param username - The username to authenticate with the user. If this isn't provided the user will be prompted for one
         @param password - The password to authenticate with the
         @param permission_level
        '''

        self.name = name
        self.username = username
        self.password = password
        self.permission_level = permission_level

    def __str__(self):

        '''
         Returns a string representation of the object. This is used for debugging purposes to show the information in the log.
         
         
         @return A string representation of the object's information in the log ( without the'-'at the end
        '''

        return f"name = {self.name} - username = {self.username} - password = {self.password} - permission level = {self.permission_level}"

    @staticmethod
    def create(name, username, password, permission_level):
        '''
         Create a new user in the database. This will hash the password before inserting it into the database.
         
         @param name - The name of the user. This is used to distinguish between different users in the database.
         @param username - The username to authenticate as. This is used to authenticate as.
         @param password - The password to authenticate as. This is used to encrypt the password.
         @param permission_level - The permission level to set for this user.
         
         @return None on success error message on failure. >>> user = User. create ( " John Doe " " password " " perm_level " ) >>> user. create ( " John Doe
        '''
        try:
            pw = p.hash(password)
            conn = c(User.DB)
            cursor = conn.cursor()

            query = ''' INSERT INTO users (name, username, password, salt, perm_level)
                        VALUES (?,?,?,?,?)
                    '''

            cursor.execute(query, (name, username, pw[0], pw[1], permission_level,))
            conn.commit()

        except Exception as e:
            return e

        finally:
            conn.close()

    @staticmethod
    def read(user_id=None, username=None):
        '''
         Read a user from the database. If user_id or username are specified the result will be returned otherwise None is returned.
         
         @param user_id - The user's id. Defaults to None.
         @param username - The user's username. Defaults to None.
         
         @return None if no user is found or an exception that was raised while trying to read the user. Otherwise a dictionary
        '''
        try:
            conn = c(User.DB)
            cursor = conn.cursor()

            # Return user_id if user_id is not None
            if user_id is not None:
                query = ''' SELECT * FROM users WHERE  id = (?)'''
                try:
                    cursor.execute(query, (user_id,))
                    result = cursor.fetchone()
                    return result

                except Exception as e:
                    return e

                finally:
                    conn.close()

            # Return the user object for the given username.
            if username is not None:
                query = ''' SELECT * FROM users WHERE  username = (?)'''
                try:
                    cursor.execute(query, (username,))
                    result = cursor.fetchone()
                    return result

                except Exception as e:
                    return e

                finally:
                    conn.close()

        except Exception as e:
            return e

        finally:
            # Close the connection to the server.
            if conn:
                conn.close()

    @staticmethod
    def update(user_id, name=None, username=None, password=None, perm_level=None):
        '''
         Update a user in the database. This will update the name username and password if provided. If the user_id is None nothing will be done.
         
         @param user_id - The id of the user to update.
         @param name - The new name for the user. Default : None.
         @param username - The new username for the user. Default : None.
         @param password - The new password for the user. Default : None.
         @param perm_level - The new permission level for the user. Default : None.
         
         @return True if successful False otherwise. CLI Example. code - block :: bash salt'*'user. update
        '''
        # Check if the user is in the database.
        if user_id is not None:
            try:
                conn = c(User.DB)
                cursor = conn.cursor()

                # Update the name of the user
                if name is not None:
                    query = ''' UPDATE users SET name = (?) WHERE id=(?)'''
                    cursor.execute(query, (name, user_id,))
                    conn.commit()

                # Update the username of the user
                if username is not None:
                    query = ''' UPDATE users SET username = (?) WHERE id=(?)'''
                    cursor.execute(query, (username, user_id,))
                    conn.commit()

                # Update the password of the user
                if password is not None:
                    query = ''' UPDATE users SET password = ?, salt = ? WHERE id=?'''
                    pw = p.hash(password)
                    cursor.execute(query, (pw[0], pw[1], user_id,))
                    conn.commit()

                # Set the user s permission level.
                if perm_level is not None:
                    query = ''' UPDATE users SET perm_level = (?) WHERE id=(?)'''
                    cursor.execute(query, (perm_level, user_id,))
                    conn.commit()

                return True

            except Exception as e:
                return e

            finally:
                conn.close()

        else:
            raise ValueError("User id not found")

    @staticmethod
    def delete(user_id=None, username=None):
        '''
         Delete a user from the database. This is a destructive operation and should be avoided if you want to keep the database intact
         
         @param user_id - The user's id
         @param username - The user's name ( optional ) If both user_id and username are specified the user will be deleted
         
         @return True if successful otherwise
        '''
        # Delete user from database if user_id is not None
        if user_id is not None:
            query = ''' DELETE FROM users WHERE id=(?)'''

            try:
                conn = c(User.DB)
                cursor = conn.cursor()

                cursor.execute(query, (user_id,))
                conn.commit()

                return True

            except Exception as e:
                return e

            finally:
                conn.close()

        # Delete the user with the given username.
        if username is not None:
            query = ''' DELETE FROM users WHERE username=(?)'''

            try:
                conn = c(User.DB)
                cursor = conn.cursor()

                cursor.execute(query, (username,))
                conn.commit()

            except Exception as e:
                return e

            finally:
                conn.close()

