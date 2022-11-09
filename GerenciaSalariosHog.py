import os


def ehConceto(entrada):
  palavrasChave = [
    "peca", "pecas", "peça", "peças", "pçs", "pç", "concerto", "conserto", "!"
  ]
  for palavra in palavrasChave:
    if palavra in entrada.lower():
      return True
  return False


def idFuncionario(id):
  #Id e nome dos funcionarios como aparece no arquivo txt
  switcher = {
    30224: "Kyrie Young",
    6290: "Igor Marques",
    31797: "Mimo Lopes",
    33794: "Rafael Soarez",
    33977: "Edgar Lobo",
    33967: "Dominc Willians"
  }
  return switcher.get(id, "nothing")


def espaco(comprimento):
  nEspacos = (30 - comprimento)
  sEspc = " "
  for i in range(nEspacos):
    sEspc = sEspc + " "
  return sEspc


def resumoPrivado(endereco):
  extrato = open(endereco, 'r')
  for registro in extrato:
    listaRegistro = registro.replace('"',
                                     '').replace("Business Services Payment:",
                                                 '').split(",")
    nome = "" + listaRegistro[6]
    if "incoming" in registro:
      sinal = "+"
    else:
      sinal = "-"
    lim = 5 - len(listaRegistro[4])
    for i in range(lim):
      sinal = sinal + " "

    fichaResumoPrvt = open("ResumoPrivado.txt", 'r')
    conteudo = fichaResumoPrvt.readlines()
    conteudo.append(sinal + listaRegistro[4] + "|" + listaRegistro[5] +
                    espaco(len(listaRegistro[5])) + nome + "\n")
    fichaResumoPrvt = open("ResumoPrivado.txt", 'w')
    fichaResumoPrvt.writelines(conteudo)
    fichaResumoPrvt.close()


def resumoPublico(endereco):
  extrato = open(endereco, 'r')
  for registro in extrato:
    listaRegistro = registro.replace('"',
                                     '').replace("Business Services Payment:",
                                                 '').split(",")
    nome = "" + listaRegistro[6]
    if "incoming" in registro:
      sinal = "+"
      lim = 5 - len(listaRegistro[4])
      for i in range(lim):
        sinal = sinal + " "
      fichaResumoPbc = open("ResumoPublico.txt", 'r')
      conteudo = fichaResumoPbc.readlines()
      conteudo.append(sinal + listaRegistro[4] + "|" + listaRegistro[5] +
                      espaco(len(listaRegistro[5])) + nome + "\n")
      fichaResumoPbc = open("ResumoPublico.txt", 'w')
      fichaResumoPbc.writelines(conteudo)
      fichaResumoPbc.close()

def ehConceto(entrada):
  palavrasChave = ["peca", "pecas", "peça", "peças", "pçs", "pç", "concerto", "conserto"
    ]
  for palavra in palavrasChave:
    if palavra in entrada.lower():
      return True
  return False


def atualiza(endereco):
  extrato = open(endereco, 'r')
  for registro in extrato:
    if "incoming" in registro:
      listaRegistro = registro.replace('"', '').split(",")
      nome = "" + listaRegistro[6]
      if '@' in registro:
        print(registro)
        id = int(input("Id do funcionário a ser transferido:"))
        nome = idFuncionario(id)
      nome = "Funcionarios/" + nome + ".txt"
      try:
        fichaFuncionario = open(nome, "r")
        conteudo = fichaFuncionario.readlines()
        conteudo.append(listaRegistro[4] + "/" + listaRegistro[5] + "/" +
                        listaRegistro[3] + "\n")
        fichaFuncionario = open(nome, 'w')
        fichaFuncionario.writelines(conteudo)
      except FileNotFoundError:
        fichaFuncionario = open(nome, 'w+')
        fichaFuncionario.writelines(listaRegistro[4] + "/" + listaRegistro[5] +
                                    "/" + listaRegistro[3] + "\n")
      fichaFuncionario.close()
    else:
      listaRegistro = registro.replace('"', '').split(",")
      nome = "Despesas.txt"
      fichaDespesas = open(nome, "r")
      conteudo = fichaDespesas.readlines()
      conteudo.append(listaRegistro[4] + "/" + listaRegistro[5] + "/" +
                      listaRegistro[6] + "/" + listaRegistro[3] + "\n")
      fichaDespesas = open(nome, 'w')
      fichaDespesas.writelines(conteudo)
      fichaDespesas.close()


def pagamento():
  diretorio = "Funcionarios/"
  endPagamento = "Pagamentos.txt"
  fichaPagamentos = open(endPagamento, "w")
  for raiz, pastas, arquivos in os.walk(diretorio, topdown=True):
    for name in arquivos:
      conteudo = []
      pagamento = 0
      caminho = diretorio + name
      fichaFuncionario = open(caminho, "r")
      logFuncionario = fichaFuncionario.readlines()
      for entrada in logFuncionario:
        if ehConceto(entrada) == True:
          pagamento = pagamento + 400
          if "cera" in entrada.lower():
            pagamento= pagamento+100
        else:
          print("\n" + entrada)
          pagamento = pagamento + int(input("Valor a adicionar no salário:"))
      fichaFuncionario = open(caminho, 'w')
      fichaFuncionario.close()
      conteudo.append(str(pagamento) + "  " + name.replace(".txt", ".") + "\n")
      fichaPagamentos.writelines(conteudo)

  fichaPagamentos.close()


escolha = 1
endereco = input("Nome do extrato em txt: ")
while escolha != '0':
  print(
    "\n1-Atualizar registro\n2-Gerar folha de pagamento\n3-Resumo Privado\n4-Resumo Publico\n 0- sair"
  )
  escolha = input()
  if escolha == '1':
    atualiza(endereco)
  if escolha == '2':
    pagamento()
  if escolha == '3':
    resumoPrivado(endereco)
  if escolha == '4':
    resumoPublico(endereco)
