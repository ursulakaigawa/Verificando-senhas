senha = "Senha@123"
caracteres_especiais = "!@#$%^&*()-_=+"

tem_8_ou_mais_caracteres = len(senha) >=8
tem_letra_maiuscula = False
tem_letra_minuscula = False
tem_numero = False
tem_caractere_especial = False

for c in senha:
    if c.isupper():
        tem_letra_maiuscula = True

    elif c.islower():
        tem_letra_minuscula = True
    elif c.isdigit():
        tem_numero = True
                
    elif c in caracteres_especiais:
        tem_caractere_especial = True


if (tem_8_ou_mais_caracteres and tem_letra_maiuscula and tem_letra_minuscula and tem_numero and tem_caractere_especial):
    print ("Senha válida")
else:
    print ("Senha inválida")