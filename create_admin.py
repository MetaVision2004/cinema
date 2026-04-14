#!/usr/bin/env python
# Script para crear usuario admin

from db import create_admin_user

# Credenciales de admin
admin_email = "admin@cinevox.com"
admin_password = "Admin123456!"
admin_nombre = "Admin"

print("Creando usuario administrador...")
print(f"Email: {admin_email}")
print(f"Contraseña: {admin_password}")
print(f"Nombre: {admin_nombre}")
print()

user_id = create_admin_user(admin_email, admin_password, admin_nombre)

if user_id:
    print(f"✅ Usuario admin creado exitosamente!")
    print(f"ID: {user_id}")
    print(f"\n📧 Email: {admin_email}")
    print(f"🔐 Contraseña: {admin_password}")
    print(f"\nAccede a: http://127.0.0.1:5000/admin/login")
else:
    print("❌ Error al crear el usuario admin")
