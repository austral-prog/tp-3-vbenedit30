def check_vowels():
	nombre = input("Ingresa tu nombre:").lower()
	a = "a"
	e = "e"
	i = "i"
	o = "o"
	u = "u"

	print(f"Contiene {a}: {"a" in nombre}")
	print(f"Contiene {e}: {"e" in nombre}")
	print(f"Contiene {i}: {"i" in nombre}")
	print(f"Contiene {o}: {"o" in nombre}")
	print(f"Contiene {u}: {"u" in nombre}")

def slice_advanced():
	texto = input("Ingresa un texto:")
	resultado = texto[4: :2]
	print(resultado)


