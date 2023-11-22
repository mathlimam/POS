from controller.client_controller import Client as clc
from database.connection import conn as c


class Tools:
    
    
    @staticmethod
    def exists(client_id=None, cpf=None):
        """
        Checks if a client exists. This is a helper function to check if a client exists based on the client_id and cpf if provided.
        
        @param client_id - The client id to check if it exists
        @param cpf - The client package to check if it exists
        
        @return True if the client exists False if it doesn't or an exception if something went wrong during the
        """

        try:
            conn = c(clc.DB)
            cursor = conn.cursor()


            # Returns the client id of the client that has been connected to the specified CPF.
            if cpf is not None:
                query = 'SELECT id FROM clients WHERE cpf = ?'
                cursor.execute(query, (cpf,))
                result = cursor.fetchone()
                return result

            # Return the client object for the client_id.
            if client_id is not None:
                query = 'SELECT cpf FROM clients WHERE id = ?'
                cursor.execute(query, (client_id,))
                result = cursor.fetchone()
                return result

        except Exception as e:
            return e

        finally:
            conn.close()


    def create(name, cpf, address, telephone, email):
        """
         Create a clc client with the given name cpf address telephone and email. This will create a client if it does not exist
         
         @param name - Name of the client to create
         @param cpf - C ++ file to create the client in
         @param address - Address of the client to create ( e. g.
         @param telephone - Phone number of the client to create.
         @param email - Email address of the client to create. If you don't want to specify this parameter it is the same as the address
        """
        try:

            # Create a client if it doesn t exist
            if Tools.exists(cpf=cpf) is None:
                clc.create(name, cpf, address, telephone, email)

            else:
                print("Client already exists")

        except Exception as e:
            print(e)

    def read(client_id=None, cpf=None):
        """
         Read configuration file. This is a wrapper around clc. read that catches errors that occur during read.
         
         @param client_id - Client ID to read configuration for.
         @param cpf - Path to configuration file. If not specified the value of config. cpf is used.
         
         @return None on success error message on failure. Example :. import fabtools >>> fabtools. read ('abc '
        """
        
        # Return the client s contents.
        if Tools.exists(client_id=client_id, cpf=cpf) is not None:
        
            try:
                return clc.read(client_id=client_id, cpf=cpf)
            
            except Exception as e:
                return e
        

    def update(client_id=None, name=None, cpf=None, address=None, telephone=None, email=None):
        """
        Updates Costumer's information. This is a wrapper around clc. update to make sure the parameters are valid
        
        @param client_id - Client ID of the Costumer to update. If you don't specify a client_id it will default to the currently logged in user's Client ID.
        @param name - Name of the Costumer as it appears in the account
        @param cpf - CPKF of the Costumer as it appears in the account
        @param address - Address of the Costumer as it appears in the account
        @param telephone - Telephone number of the Costumer as it appears in the account
        @param email - Email address of the Costumer as it appears in the account
        
        @return None if successful error message if not successful Example :. from iota import Costumer costumer = Costumer. update ( client_id = 1234
        """

        # Costumer doesn t exist.
        if Tools.exists(client_id=client_id, cpf=cpf) is not None:
            try:
                return clc.update(client_id=client_id, name=name, cpf=cpf,address=address, telephone=telephone, email=email)
            
            except Exception as e:
                return e

        else: 
            return "Costumer doesn't exists"
        
    
    def delete(client_id=None, cpf=None):
        """
        Deletes a client from CLC. This is a wrapper for clc. delete that checks if the client exists before deleting it.
        
        @param client_id - The client to delete. If you don't specify a client_id the function will delete the first client with that id.
        @param cpf - The CPF of the client to delete.
        
        @return True if successful False otherwise. >>> from fabtools. test import TestClient >>> client = TestClient ( " abc " )
        """

        # Delete client from the cluster.
        if Tools.exists(client_id=client_id, cpf=cpf) is not None:
            return clc.delete(client_id=client_id, cpf=cpf)
        
        else: 
            return "client doesn't exists"