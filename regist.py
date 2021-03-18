with open('senha.txt', 'w') as senha:
        while True:
                regi = input("Digite a senha a ser usada: ")
                dnv = input("Digite denovo: ")
                if dnv != regi:
                        print("A senha não corresponde com a primeira")
                else:
                        senha.write(str(dnv))
                        print(f"Pronto {dnv} agora e sua senha")
                        break
