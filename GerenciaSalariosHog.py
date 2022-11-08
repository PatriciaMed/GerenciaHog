import os

def ehConceto(entrada):
  palavrasChave = [
    "peca", "pecas", "peça", "peças", "pçs", "pç", "concerto", "conserto"
  ]
  for palavra in palavrasChave:
    if palavra in entrada.lower():
      return True
  return False
def resumoPrivado():
  endereco = input("Nome do extrato em txt: ")
  extrato = open(endereco, 'r')
  for registro in extrato:
    listaRegistro = registro.replace('"', '').split(",")
    nome = "" + listaRegistro[6]
    if '@' in registro:
      print(registro)
      id = int(input("Id do funcionário a ser transferido:"))
      nome = idFuncionario(id)
      if "incoming" in registro:
        sinal = "+"
      else:
        sinal = "-"
      fichaResumoPrvt = open("ResumoPrivado.txt", 'w')
      fichaResumoPrvt.writelines(sinal + listaRegistro[4] + "|" +listaRegistro[5] + "              " +nome + "\n")
      fichaResumoPrvt.close()

def resumoPublico():
  endereco = input("Nome do extrato em txt: ")
  extrato = open(endereco, 'r')
  for registro in extrato:
    listaRegistro = registro.replace('"', '').split(",")
    nome = "" + listaRegistro[6]
    if '@' in registro:
      print(registro)
      id = int(input("Id do funcionário a ser transferido:"))
      nome = idFuncionario(id)
    nomeArquivo = "Funcionarios/" + nome + ".txt"
    for registro in extrato:
      if "incoming" in registro:
        fichaResumoPblc = open("ResumoPublico.txt", 'w')
        fichaResumoPblc.writelines(sinal + listaRegistro[4] + "|" +listaRegistro[5] + "              " +nome + "\n")
        fichaResumoPblc.close()

  def ehConceto(entrada):
    palavrasChave = [
      "peca", "pecas", "peça", "peças", "pçs", "pç", "concerto", "conserto"
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

def atualiza():
  endereco = input("Nome do extrato em txt: ")
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
      outros = []
      pagamento = 0
      caminho = diretorio + name
      fichaFuncionario = open(caminho, "r")
      logFuncionario = fichaFuncionario.readlines()
      for entrada in logFuncionario:
        if ehConceto(entrada) == True:
          pagamento = pagamento + 400
        else:
          print("\n" + entrada)
          pagamento = pagamento + int(input("Valor a adicionar no salário:"))
      fichaFuncionario = open(caminho, 'w')
      fichaFuncionario.close()
      conteudo.append(str(pagamento) + "  " + name.replace(".txt", ".") + "\n")
      fichaPagamentos.writelines(conteudo)

  fichaPagamentos.close()


escolha = 1
while escolha != '0':
  print("1-Atualizar registro\n2-Gerar folha de pagamento\n 0- sair")
  escolha = input()
  if escolha == '1':
    atualiza()
  if escolha == '2':
    pagamento()
  if escolha == '3':
    resumoPrivado()
  if escolha == '4':
    resumoPublico()
