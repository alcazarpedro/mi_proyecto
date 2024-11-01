def ine(age):
    if age >= 18:
        return "ya puedes tramitar la INE"
    else:
        return "ere menor de edad"

age = int(input("escribe tu edad :"))
tramite = ine(age)
print(tramite)    