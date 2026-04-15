"""Script temporal para crear/reparar el usuario admin."""
from db import get_db_connection
from werkzeug.security import generate_password_hash

conn = get_db_connection()
cursor = conn.cursor()

# Crear tabla usuarios si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS `usuarios` (
  `id` int NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `rol` enum('admin','usuario') DEFAULT 'usuario',
  `activo` tinyint(1) DEFAULT 1,
  `fecha_creacion` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;
""")
conn.commit()
print("Tabla usuarios OK")

# Crear/actualizar admin
email = "admin@cinevox.com"
password = "Admin123456!"
pw_hash = generate_password_hash(password)

cursor.execute("""
    INSERT INTO usuarios (email, password, nombre, rol, activo)
    VALUES (%s, %s, %s, %s, 1)
    ON DUPLICATE KEY UPDATE
        password = VALUES(password),
        rol = 'admin',
        activo = 1
""", (email, pw_hash, "Administrador", "admin"))
conn.commit()

cursor.close()
conn.close()

print(f"\nAdmin listo!")
print(f"  Email:      {email}")
print(f"  Contrasena: {password}")
print(f"\nInicia sesion en: http://127.0.0.1:5000/login")
