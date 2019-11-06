#Hacer 10 ejercicios por cda operacion de diccionarios
 # Creación
print("\tCreación")
d = {"dia": "lunes", "mes": "febrero", "año": 2019}
print("1.", d)

e = dict()
print("2.", e)

f = dict(verdura = "lechuga")
print("3.", f)

g = dict({"a": 1, "b": 2})
print("4.", g)

nombre = ["Luis", "Marcos", "Miguel"]
edad = [16, 20, 18]
datos =dict(zip(nombre, edad))
print("5.", datos)

lista1 = [1, 2, 3, 4]
lista2 = ["uno", "dos", "tres", "cuatro"]
dicc1 = dict(zip(lista1, lista2))
print("6.", dicc1)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9.", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedro", 6 : "Iniesta", 7 : "Villa"}
print("10.", futbolistas)


 # Pertenencia de clave
print("\n\tPertenencia de clave")
d = {"dia": "martes", "mes": "noviembre", "año": 2019}
print("1.","dia" in d)

e = dict()
print("2.","mes" not in e)

f = dict(verdura = "lechuga")
print("3.","verdura" not in f)

g = dict({"a": 1, "b": 2})
print("4.",1 in g)

nombre = ["Luis", "Marcos", "Miguel"]
edad = [16, 20, 18]
datos =dict(zip(nombre, edad))
print("5.","Luis" in datos)

lista1 = [1, 2, 3, 4]
lista2 = ["uno", "dos", "tres", "cuatro"]
dicc1 = dict(zip(lista1, lista2))
print("6.",4 in dicc1)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.","Ivanhoe" in obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.","meses" not in dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9.","cereal" in dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedro", 6 : "Iniesta", 7 : "Villa"}
print("10.",7 in futbolistas)


# Comparación
print("\n\tComparación")
print("1.", d == e)
print("2.", e != f)
print("3.", f == g)
print("4.", g != datos)
print("5.", datos == obras_lit)
print("6.", obras_lit != dicc2)
print("7.", dicc1 == dicc2)
print("8.", dicc3 != dicc1)
print("9.", futbolistas == d)
print("10.", dicc2 != e)

# Indexación
print("\n\tIndexación")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1.", d["mes"])

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet"})
print("2.", p["Kill Bill"])

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3.", f["Java"])

g = dict({"a": 1, "b": 2, "c": 3})
print("4.", g["b"])

nombre = ["Luis", "Marcos", "Miguel"]
edad = [16, 20, 18]
datos =dict(zip(nombre, edad))
print("5.", datos["Luis"])

lista1 = [1, 2, 3, 4]
lista2 = ["uno", "dos", "tres", "cuatro"]
dicc1 = dict(zip(lista1, lista2))
print("6.", dicc1[4])

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.", obras_lit["Fausto"])

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.", dicc2["dias"])

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9.", dicc3["verdura"])

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedro", 6 : "Iniesta", 7 : "Villa"}
print("10.", futbolistas[8])


# Longitud
print("\n\tLongitud")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1.", len(d))

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
print("2.", len(p))

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3.", len(f))

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
print("4.", len(g))

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
print("5.", len(datos))

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
print("6.", len(dicc1))

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.", len(obras_lit))

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.", len(dicc2))

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9.", len(dicc3))

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 18 : "Pedro", 6 : "Iniesta", 7 : "Villa"}
print("10.", len(futbolistas))


# Iteración
print("\n\tIteración")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
for a in d:
    print("1.", a)

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
for b in p:
    print("2.", b)

f = {"Python": 1991, "C": 1972, "Java": 1996}
for k,v in f.items():
    print("3.", k, ":", v)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
for e in g:
    print("4.", e)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
for k, v in zip(datos.keys(), datos.values()):
    print("5.", k, ":", v)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
for i in dicc1:
    print("6.", dicc1[i])

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
for k,v in obras_lit.items():
    print("7.", k, ":", v)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
for k in dicc2:
    print("8.", k)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
for k,v in dicc3.items():
    print("9.", k, ":", v)

futbolistas = {"Arthur": 4, "Puyol": 2, "Busquets": 5, "Xavi Hernandez": 8, "Pedro": 11, "Iniesta": 6, "Villa": 9}
for m in futbolistas:
    print("10.", m)

# Búsqueda
print("\n\tBúsqueda")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1.", d.get("año"))

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
print("2.", p.get("Titanic"))

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3.", f.get("Python"))

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
print("4.", g.get("f"))

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
print("5.", datos.get("Sebastian"))

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
print("6.", dicc1.get(1))

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.", obras_lit.get("Tartufo"))

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.", dicc2.get("meses"))

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9.", dicc3.get("fruta"))

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
print("10.", futbolistas.get(5))


# Eliminación
print("\n\tEliminación")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
del d["dia"]
print("1.", d)

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
del p["Love Actually"]
print("2.", p)

f = {"Python": 1991, "C": 1972, "Java": 1996}
del f["C"]
print("3.", f)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
del g["b"]
print("4.", g)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
del datos["Marcos"]
print("5.", datos)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
del dicc1[3]
print("6.", dicc1)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
del obras_lit["Guerra y paz"]
print("7.", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
del dicc2["dias"]
print("8.", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
del dicc3["tuberculo"]
print("9.", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
del futbolistas[4]
print("10.", futbolistas)

# Reemplazo
print("\n\tReemplazo")

d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1. Antes del reemplazo:", d)
d["dia"] = "Lunes"
print("1. Despúes del reemplazo:", d)

p = dict({"Richard Curtis": "Love Actually", "Tarantino": "Kill Bill", "Titanic": "James Cameron"})
print("2. Antes del reemplazo:", p)
p["Richard Curtis"] = "Yesterday"
print("2. Despúes del reemplazo:", p)

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3. Antes del reemplazo:", f)
f["Java"] = 2000
print("3. Despúes del reemplazo:", f)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4})
print("4. Antes del reemplazo:", g)
g["b"] = "Hola"
print("4. Despúes del reemplazo:", g)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
print("5. Antes del reemplazo:", datos)
datos["Marcos"] = "Bienvenido"
print("5. Despúes del reemplazo:", datos)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
print("6. Antes del reemplazo:", dicc1)
dicc1[2] = 2
print("6. Despúes del reemplazo:", dicc1)

obras_lit = dict({"Goethe": "Fausto", "Moliere": "Tartufo", "Walter Scott": "Ivanhoe", "Tolstoi": "Guerra y paz"})
print("7. Antes del reemplazo:", obras_lit)
obras_lit["Moliere"] = "El avaro"
print("7. Despúes del reemplazo:", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8. Antes del reemplazo:", dicc2)
dicc2["dias"] = ["sab", "dom"]
print("8. Despúes del reemplazo:", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9. Antes del reemplazo:", dicc3)
dicc3["fruta"] = "pera"
dicc3["verdura"] = "espinaca"
print("9. Despúes del reemplazo:", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
print("10. Antes del reemplazo:", futbolistas)
futbolistas[11] = "Dembelé"
futbolistas[9] = "Suárez"
futbolistas[2] = "Piqué"
print("10. Despúes del reemplazo:", futbolistas)

# Agregado
print("\n\tAgregado")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1. Antes del agregado:", d)
d.setdefault("siglo", "XXI")
print("1. Despúes del agregado:", d)

p = dict({"Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
print("2. Antes del agregado:", p)
p.setdefault("Joker", "Todd Phillips")
print("2. Despúes del agregado:", p)

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3. Antes del agregado:", f)
f.setdefault("Ruby", 1995)
print("3. Despúes del agregado:", f)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5})
print("4. Antes del agregado:", g)
g.setdefault("f", 6)
print("4. Despúes del agregado:", g)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
print("5. Antes del agregado:", datos)
datos.setdefault("Gian", 20)
print("5. Despúes del agregado:", datos)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
print("6. Antes del agregado:", dicc1)
dicc1.setdefault(6, "seis")
print("6. Despúes del agregado:", dicc1)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott"})
print("7. Antes del agregado:", obras_lit)
obras_lit.setdefault("Maria", "Jorge Isaacs")
print("7. Despúes del agregado:", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8. Antes del agregado:", dicc2)
dicc2.setdefault("años", [2017, 2018, 2019])
print("8. Despúes del agregado:", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("9. Antes del agregado:", dicc3)
dicc3.setdefault("flor", "rosa")
print("9. Despúes del agregado:", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
print("10. Antes del agregado:", futbolistas)
futbolistas.setdefault(10, "Messi")
print("10. Despúes del agregado:", futbolistas)

# Anulación
print("\n\tAnulación")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
d.clear()
print("1.", d)

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
p.clear()
print("2.", p)

f = {"Python": 1991, "C": 1972, "Java": 1996}
f.clear()
print("3.", f)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
g.clear()
print("4.", g)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
datos.clear()
print("5.", datos)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
dicc1.clear()
print("6.", dicc1)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
obras_lit.clear()
print("7.", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
dicc2.clear()
print("8.", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
dicc3.clear()
print("9.", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
futbolistas.clear()
print("10.", futbolistas)

# Clonado
print("\n\tClonado")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
a = d.copy()
print("1.", a)

p = dict({"Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
b = p.copy()
print("2.", b)

f = {"Python": 1991, "C": 1972, "Java": 1996}
c = f.copy()
print("3.", c)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
e = g.copy()
print("4.", e)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
h = datos.copy()
print("5.", h)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
i = dicc1.copy()
print("6.", i)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
j = obras_lit.copy()
print("7.", j)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
k = dicc2.copy()
print("8.", k)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
l = dicc3.copy()
print("9.", l)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
m = futbolistas.copy()
print("10.", m)

# Inserción
print("\n\tInserción")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
d["dia"] = "Lunes"
print("1.", d)

p = dict({"Richard Curtis": "Love Actually", "Tarantino": "Kill Bill", "Titanic": "James Cameron"})
p["Richard Curtis"] = "Yesterday"
print("2.", p)

f = {"Python": 1991, "C": 1972, "Java": 1996}
f["Java"] = 2000
print("3.", f)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4})
g["b"] = "Hola"
print("4.", g)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
datos["Marcos"] = "Bienvenido"
print("5.", datos)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
dicc1[2] = 2
print("6.", dicc1)

obras_lit = dict({"Goethe": "Fausto", "Moliere": "Tartufo", "Walter Scott": "Ivanhoe", "Tolstoi": "Guerra y paz"})
obras_lit["Moliere"] = "El avaro"
print("7.", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
dicc2["dias"] = ["sab", "dom"]
print("8.", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
dicc3["fruta"] = "pera"
print("9.", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
futbolistas[11] = "Dembelé"
print("10.", futbolistas)

# Extracción
print("\n\tExtracción")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
a = d.pop("mes")
print("1.", a)
print("1.", d)

p = dict({"Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
b = p.pop("Kill Bill")
print("2.", b)
print("2.", p)

f = {"Python": 1991, "C": 1972, "Java": 1996}
c = f.pop("C")
print("3.", c)
print("3.", f)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
e = g.pop("e")
print("4.", e)
print("4.", g)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
h = datos.pop("Marcos")
print("5.", h)
print("5.", datos)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
i = dicc1.pop(4)
print("6.", i)
print("6.", dicc1)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
j = obras_lit.pop("Fausto")
print("7.", j)
print("7.", obras_lit)

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
k = dicc2.pop("numeros")
print("8.", k)
print("8.", dicc2)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
l = dicc3.pop("verdura")
print("9.", l)
print("9.", dicc3)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
m = futbolistas.pop(4)
print("10.", m)
print("10.", futbolistas)

# Ver Claves
print("\n\tVer Claves")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1.", d.keys())

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
print("2.", p.keys())

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3.", f.keys())

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
print("4.", g.keys())

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
print("5.", datos.keys())

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
print("6.", dicc1.keys())

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.", obras_lit.keys())

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.", dicc2.keys())

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("8.", dicc3.keys())

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
print("10.", futbolistas.keys())

# Ver Valores
print("\n\tVer Valores")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
print("1.", d.values())

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
print("2.", p.values())

f = {"Python": 1991, "C": 1972, "Java": 1996}
print("3.", f.values())

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
print("4.", g.values())

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
print("5.", datos.values())

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
print("6.", dicc1.values())

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
print("7.", obras_lit.values())

dicc2 = {"dias": ["lun", "mar", "miér", "jue", "vie"], "numeros": [1, 2, 3, 4, 5], "meses": ["Ene", "Feb", "Mar", "Abr", "May"]}
print("8.", dicc2.values())

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
print("8.", dicc3.values())

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
print("10.", futbolistas.values())

# Conversión
print("\n\tConversión")
d = {"dia": "Martes", "mes": "Noviembre", "año": 2019}
l = list(d)
t = tuple(d)
s = set(d)
print("1. KEYS en lista:", l, "\n1. KEYS en tupla:",  t, "\n1. KEYS en set:", s)

p = dict({"Love Actually": "Richard Curtis", "Kill Bill": "Tarantino", "Amélie": "Jean-Pierre Jeunet", "Titanic": "James Cameron"})
l = list(p.values())
t = tuple(p.values())
s = set(p.values())
print("2. VALUES en lista:", l, "\n2. VALUES en tupla:",  t, "\n2. VALUES en set:", s)

f = {"Python": 1991, "C": 1972, "Java": 1996}
l = list(f)
t = tuple(f)
s = set(f)
print("3. KEYS en lista:", l, "\n3. KEYS en tupla:",  t, "\n3. KEYS en set:", s)

g = dict({"a": 1, "b": 2, "c": 3, "d": 4, "e": 5, "f": 6})
l = list(g.values())
t = tuple(g.values())
s = set(g.values())
print("4. VALUES en lista:", l, "\n4. VALUES en tupla:",  t, "\n4. VALUES en set:", s)

nombre = ["Luis", "Marcos", "Miguel", "Sebastian"]
edad = [16, 20, 18, 12]
datos =dict(zip(nombre, edad))
l = list(datos)
t = tuple(datos)
s = set(datos)
print("5. KEYS en lista:", l, "\n5. KEYS en tupla:",  t, "\n5. KEYS en set:", s)

lista1 = [1, 2, 3, 4, 5]
lista2 = ["uno", "dos", "tres", "cuatro", "cinco"]
dicc1 = dict(zip(lista1, lista2))
l = list(dicc1.values())
t = tuple(dicc1.values())
s = set(dicc1.values())
print("6. VALUES en lista:", l, "\n6. VALUES en tupla:",  t, "\n6. VALUES en set:", s)

obras_lit = dict({"Fausto": "Goethe", "Tartufo": "Moliere", "Ivanhoe": "Walter Scott", "Guerra y paz":"Tolstoi"})
l = list(obras_lit)
t = tuple(obras_lit)
s = set(obras_lit)
print("7. KEYS en lista:", l, "\n7. KEYS en tupla:",  t, "\n7. KEYS en set:", s)

dicc2 = {"dia": "mar", "numero": 3, "mes": "Mar"}
l = list(dicc2.values())
t = tuple(dicc2.values())
s = set(dicc2.values())
print("8. VALUES en lista:", l, "\n8. VALUES en tupla:",  t, "\n8. VALUES en set:", s)

dicc3 = {"fruta": "manzana", "verdura": "lechuga", "cereal": "arroz", "tuberculo": "camote"}
l = list(dicc3)
t = tuple(dicc3)
s = set(dicc3)
print("9. KEYS en lista:", l, "\n9. KEYS en tupla:",  t, "\n9. KEYS en set:", s)

futbolistas = {4 : "Arthur", 2 : "Puyol", 5 : "Busquets", 8 : "Xavi Hernandez", 11 : "Pedro", 6 : "Iniesta", 9 : "Villa"}
l = list(futbolistas.values())
t = tuple(futbolistas.values())
s = set(futbolistas.values())
print("10. VALUES en lista:", l, "\n10. VALUES en tupla:",  t, "\n10. VALUES en set:", s)