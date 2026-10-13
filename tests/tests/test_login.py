def login(usuario, contrasena): 
	# Simulación mínima del sistema bajo prueba 
	return bool(usuario) and bool(contrasena) 

def test_login_con_contrasena_vacia_muestra_error(): 
	assert login("ana", "") is False
