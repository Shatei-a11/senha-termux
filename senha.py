import time
def senha():
        with open('senha.txt', 'r') as senha:
                       for p in senha:
                        senha = p
                       while True:
                                                if senha == "vazia":
                                                        print("Vc n tem senha")
                                                        k = input("Digite a nova senha:>
                                                        with open('senha.txt', 'w') as >
                                                                nova.write(str(k))
                                                                print("Pronto")
                                                        break
                                                use = input("Digite a senha: ")
                                                if use == senha:
                                                        print("Acesso garantido")
                                                        break
                                                else:
                                                        print("Senha errada tente novam>

while True:
        try:
                senha()
                time.sleep(1)
                break
        except KeyboardInterrupt:
                print("Voce não ira me burlar")
