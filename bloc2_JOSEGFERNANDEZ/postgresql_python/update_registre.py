import connect

def update_reg():
    conn = connect.connection_db()
    cursor = conn.cursor()

    sql_update = '''
    UPDATE clientes
    SET nombre_cliente = "Juan Manuel"
    SET telefóno_cliente=000000000
    WHERE nombre_cliente = "Roger"
    '''

    cursor.execute(sql_update)
    conn.commit()

    cursor.close()
    conn.close()

    return {"Update successfully"}