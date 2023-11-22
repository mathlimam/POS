import sqlite3
from database.connection import conn as c


class Client:
    DB = "app/database/clients.db"

    def __init__(self, name, cpf, address, telephone, email):
        """
         Initializes the object with name cpf address telephone and email. This is used to set attributes that are not part of the Cisco Message object.
         
         @param name - The name of the message. This is required.
         @param cpf - The CPF of the message. This is required.
         @param address - The address of the message. This is required.
         @param telephone - The telephone number of the message. This is required.
         @param email - The e - mail address of the message. This is required
        """
        self.name = name
        self.cpf = cpf
        self.address = address
        self.telephone = telephone
        self.email = email

    def __str__(self):
        """
         Returns a string representation of the IP address. This is used for debugging purposes as the IP address may contain non - ASCII characters in their string representation.
         
         
         @return A string representation of the IP address in human readable form e. g. " name = { 0 } - cpf = { 1
        """
        return f"name = {self.name} - cpf = {self.cpf} - address = {self.address} - telephone = {self.telephone} - email = {self.email}"

    @staticmethod
    def create(name, cpf, address, telephone, email):
        """
         Create a new client. This will add the client to the database if it does not already exist.
         
         @param name - The name of the client. This is used to display the client's name on the screen.
         @param cpf - The cryptographic fingerprint of the client.
         @param address - The client's address
         @param telephone - The client's telephone number
         @param email - The
        """
        query = '''
                INSERT INTO clients (name, cpf, address, telephone, email) 
                VALUES (?,?,?,?,?)
                '''
        try:
            conn = c(Client.DB)
            cursor = conn.cursor()
            cursor.execute(query, (name, cpf, address, telephone, email,))
            conn.commit()
        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def read(client_id=None, cpf=None):
        """
         Read a client from the database. This is a wrapper around the SQLAlchemy read function to avoid SQL injection attacks
         
         @param client_id - The client id to read
         @param cpf - The CPF to read ( optional )
         
         @return A list of client data ( tuples in the form ( id cpf ) if client_id is None
        """
        # Return a list of clients that have been connected to the database.
        if client_id is not None:
            query = '''
                    SELECT * FROM clients WHERE id=?
                    '''
            try:
                conn = c(Client.DB)
                cursor = conn.cursor()
                cursor.execute(query, (client_id,))
                result = cursor.fetchall()
                return result
            except sqlite3.Error as e:
                print(e)
            finally:
                conn.close()

        # Return the list of clients that have the specified cpf.
        if cpf is not None:
            query = '''
                    SELECT * FROM clients WHERE cpf=?
                    '''
            try:
                conn = c(Client.DB)
                cursor = conn.cursor()
                cursor.execute(query, (cpf,))
                result = cursor.fetchall()
                return result
            except sqlite3.Error as e:
                print(e)
            finally:
                conn.close()

    @staticmethod
    def update(client_id, name=None, cpf=None, address=None, telephone=None, email=None):
        """
         Update a client in the database. This will update the name cpf address telephone and email fields if they are not None
         
         @param client_id - The id of the client to update
         @param name - The new name of the client ( optional )
         @param cpf - The new CPF of the client ( optional )
         @param address - The new address of the client ( optional )
         @param telephone - The new telephone number of the client ( optional )
         @param email - The new email address of the client ( optional )
        """
        try:
            conn = c(Client.DB)
            cursor = conn.cursor()

            # Update the name of the client
            if name is not None:
                query = '''
                        UPDATE clients SET name=? WHERE client_id=?
                        '''
                cursor.execute(query, (name, client_id,))
                conn.commit()
                print("successful")

            # Update the client s cpf.
            if cpf is not None:
                query = '''
                        UPDATE clients SET cpf=? WHERE client_id=?
                        '''
                cursor.execute(query, (cpf, client_id,))
                conn.commit()
                print("successful")

            # update address of the client
            if address is not None:
                query = '''
                        UPDATE clients SET address=? WHERE client_id=?
                        '''
                cursor.execute(query, (address, client_id,))
                conn.commit()
                print("successful")

            # update the telephone of the client
            if telephone is not None:
                query = '''
                        UPDATE clients SET telephone=? WHERE client_id=?
                        '''
                cursor.execute(query, (telephone, client_id,))
                conn.commit()
                print("successful")

            # update the email of the client
            if email is not None:
                query = '''
                        UPDATE clients SET email=? WHERE client_id=?
                        '''
                cursor.execute(query, (email, client_id,))
                conn.commit()
                print("successful")

        except sqlite3.Error as e:
            print(e)
        finally:
            conn.close()

    @staticmethod
    def delete(client_id=None, cpf=None):
        """
         Delete a client from the database. This is a destructive operation and should be avoided if you want to keep the database intact
         
         @param client_id - The client's id
         @param cpf - The client's CPF ( optional )
         
         @return True if successful False if not ( in which case the database is not modified ) >>> client = client. create ( client_id ='3G '
        """
        # Delete the client_id from the database.
        if client_id is not None:
            query = '''
                    DELETE FROM clients WHERE id=?
                    '''
            try:
                conn = c(Client.DB)
                cursor = conn.cursor()
                cursor.execute(query, (client_id,))
                conn.commit()
                return True
            except sqlite3.Error as e:
                print(e)
            finally:
                conn.close()

        # Delete the client from the database.
        if cpf is not None:
            query = '''
                    DELETE FROM clients WHERE cpf=?
                    '''
            try:
                conn = c(Client.DB)
                cursor = conn.cursor()
                cursor.execute(query, (cpf,))
                conn.commit()
                return True
            except sqlite3.Error as e:
                print(e)
            finally:
                conn.close()