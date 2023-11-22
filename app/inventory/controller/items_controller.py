from database.connection import conn as c
import sqlite3


class Items:
    DB = "app/database/items.db"

    def __init__(self, code, name, manufacturer, barcode, quantity_in_stock,  value):
        self.name = name
        self.manufacturer = manufacturer
        self.bar_code = barcode
        self.quantity_in_stock = quantity_in_stock
        self.value = value

    def __str__(self):
        return f"name = {self.name} - manufacturer = {self.manufacturer} - bar_code = {self.bar_code} - quantity in stock = {self.quantity_in_stock} - value = {self.value}"
    

    def create(code, name, manufacturer, quantity_in_stock, value, barcode=None):
        query = '''
                INSERT INTO items (code, name, manufacturer, barcode, quantity_in_stock, value)
                VALUES (?,?,?,?,?)
                '''
        
        try:
            conn = c(Items.DB)
            cursor = conn.cursor()

            cursor.execute(query, (code, name, manufacturer, barcode, quantity_in_stock, value,))
            conn.commit()

            
        
        except sqlite3.Error as e:
            return e
        
        finally:
            conn.close()


    def read(item_id):
        query = '''
                SELECT * FROM items WHERE id=?
                '''
        
        try:
            conn = c(Items.DB)
            cursor = conn.cursor()

            cursor.execute(query, (item_id,))
            

            return cursor.fetchall()
    
        except sqlite3.Error as e:
            return e
        
        finally:
            conn.close()

    
    def update(item_id, name=None, manufacturer=None, barcode=None, quantity_in_stock=None, value=None):
        
        try:
            conn = c(Items.DB)
            cursor = conn.cursor()
            
            if name is not None:
                query = '''
                        UPDATE items SET name=?  WHERE id=?
                        '''


                cursor.execute(query, (name,))
                conn.commit()
                
            if manufacturer is not None:
                query = '''
                        UPDATE items SET manufacturer=?  WHERE id=?
                        '''
                

                cursor.execute(query, (manufacturer,))
                conn.commit()
            
            if barcode is not None:
                query = '''
                        UPDATE items SET barcode=?  WHERE id=?
                        '''
                


                cursor.execute(query, (barcode,))
                conn.commit()
            
            if quantity_in_stock is not None:
                query = '''
                        UPDATE items SET quantity_in_stock=?  WHERE id=?
                        '''


                cursor.execute(query, (quantity_in_stock,))
                conn.commit()
            
            if value is not None:
                query = '''
                        UPDATE items SET value=?  WHERE id=?
                        '''
                


                cursor.execute(query, (value,))
                conn.commit()
            
        except sqlite3.Error as e:
            return e
        
        finally:
            conn.close()
        

    def delete(item_id):
        
        query=  '''
                DELETE FROM items WHERE id=?
                '''
        try:
            conn = c(Items.DB)
            cursor = conn.cursor()

            cursor.execute(query, (item_id))
            return conn.commit()

        except sqlite3.Error as e:
            return e
        
        finally:
            conn.close()