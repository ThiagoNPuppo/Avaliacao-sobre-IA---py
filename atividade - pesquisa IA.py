estados = ['AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO',
'RR', 'SC', 'SP', 'SE', 'TO']

pesquisa = {}

class Relevancia:
    def __init__(self):
        while True:
            try:
                self.__desemprego = int(input("Desemprego e desigualdade: "))
                if 1 <= self.__desemprego <= 5:
                    break
                else:
                    print("Digite um valor entre 1 e 5")
                    continue
            except ValueError:
                print("valor inválido! ")
        while True:
            try:
                self.__etica = int(input("Questões éticas e morais: "))
                if 1 <= self.__etica <= 5:
                    break
                else:
                    print("Digite um valor entre 1 e 5")
                    continue
            except ValueError:
                print("valor inválido! ")
        while True:
            try:
                self.__seguranca = int(input("Segurança cibernética: "))
                if 1 <= self.__seguranca <= 5:
                    break
                else:
                    print("Digite um valor entre 1 e 5")
                    continue
            except ValueError:
                print("valor inválido! ")
        while True:
            try:
                self.__regulamentacao = int(input("Regulamentação: "))
                if 1 <= self.__regulamentacao <= 5:
                    break
                else:
                    print("Digite um valor entre 1 e 5")
                    continue
            except ValueError:
                print("valor inválido! ")
        while True:
            try:
                self.__potencial = int(input("Potencial desenvolvimento: "))
                if 1 <= self.__potencial <= 5:
                    break
                else:
                    print("Digite um valor entre 1 e 5")
                    continue
            except ValueError:
                print("valor inválido! ")

    def get_desemprego(self):
        return self.__desemprego

    def get_etica(self):
        return self.__etica

    def get_seguranca(self):
        return self.__seguranca

    def get_regulamentacao(self):
        return self.__regulamentacao

    def get_potencial(self):
        return self.__potencial


    def __str__(self):
        return f"""As notas dadas foram:
        #DESEMPREGO E DESIGUALDADE: {self.__desemprego}
        #ÈTICA E MORAL: {self.__etica}
        #SEGURANÇA CIBERNÉTICA: {self.__seguranca}
        #REGULAMENTAÇÃO: {self.__regulamentacao}
        #POTENCIAL DESENVOLVIMENTO: {self.__potencial}"""


def relatorio():
    estado_mora = input("Informe seu Estado: ").upper()
    if estado_mora in estados:
        print("Relatório:")
        qtd = 0
        soma1 = 0
        soma2 = 0
        soma3 = 0
        soma4 = 0
        soma5 = 0
        for estado, items in pesquisa.items():
            if estado == estado_mora:
                print(f"Estado: {estado}")
                for pes in items:
                    qtd += 1
                    soma1 += pes.get_desemprego()
                    soma2 += pes.get_etica()
                    soma3 += pes.get_seguranca()
                    soma4 += pes.get_regulamentacao()
                    soma5 += pes.get_potencial()
                media1 = (soma1 / qtd) * 100 / 5
                media2 = (soma2 / qtd) * 100 / 5
                media3 = (soma3 / qtd) * 100 / 5
                media4 = (soma4 / qtd) * 100 / 5
                media5 = (soma5 / qtd) * 100 / 5

                soma1 = media1; soma2 = media2; soma3 = media3; soma4 = media4; soma5 = media5

                print(f"O estado de {estado} teve {qtd} avaliações")
                print()
                print(f"+ Desemprego e Desigualdade tivemos \33[31m{soma1:.2f}%\33[m de relevância")
                print(f"+ Questões éticas e morais tivemos \33[31m{soma2:.2f}%\33[m de relevância")
                print(f"+ Segurança cibernética tivemos \33[31m{soma3:.2f}%\33[m de relevância")
                print(f"+ Regulamentação tivemos \33[31m{soma4:.2f}%\33[m de relevância")
                print(f"+ Potencial desenvolvimento tivemos \33[31m{soma5:.2f}%\33[m de relevância")

    else:
        print("estado não existente!")

def menu():
    while True:
        try:
            print("""
            MENU PRINCIPAL
    +++++++++++++++++++++++++++""")
            op = int(input("""Escolha uma opção:
        [1] Realizar avaliação
        [2] Relatório
        [3] Finalizar programa 
          ==> """))
            if op == 1:
                while True:
                    es = input("Qual seu estado? Sigla => ").upper()
                    if es in estados:
                        print()
                        print("Digite suas notas de [1] a [5] para cada assunto.")
                        print()
                        res = Relevancia()
                        if es in pesquisa:
                            pesquisa[es].append(res)
                            break
                        else:
                            pesquisa[es] = [res]
                            break
                    else:
                        print("Estado não encontrado!")
            elif op == 2:
                relatorio()
            elif op == 3:
                print("Até logo...")
                break
            else:
                print("opção inválida!\n Escolha uma opção do menu!")
                continue
        except ValueError:
            print("valor inválido")


print("PESQUISA SOBRE INTELIGÊNCIA ARTIFICIAL\n"
      "De 1 a 5 de uma nota para o que vc considera mais preocupante sobre a IA")
print("++" * 35)
menu()
