instructions = [
    """CREATE TABLE IF NOT EXISTS clientes(
        id SERIAL NOT NULL PRIMARY KEY,
        nombre varchar(100) NOT NULL, 
        telefono INT NOT NULL,
        empresa VARCHAR(255),
        fecha TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
    )
    """
]