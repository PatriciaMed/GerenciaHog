import os
def atualiza():
    #aceita diretório do último extrato convertido para txt
    endereco= input("Nome do extrato em txt: ")
    endereco="C:/Users/Helcio/Pictures/TLMC/RPLetNp/Nova pasta/"+endereco
    extrato = open(endereco, 'r')
    for registro in extrato:
        if "incoming" in registro:
            listaRegistro= registro.replace('"','').split(",")
            nome=""+listaRegistro[6]
            nome="C:/Users/Helcio/Pictures/TLMC/RPLetNp/Nova pasta/Funcionarios/"+nome+".txt"
            try:
                fichaFuncionario=open(nome,"r")
                conteudo = fichaFuncionario.readlines()
                conteudo.append(listaRegistro[4]+"/"+listaRegistro[5]+"/"+listaRegistro[3]+"\n")
                fichaFuncionario = open(nome, 'w')
                fichaFuncionario.writelines(conteudo)
            except FileNotFoundError:
                fichaFuncionario = open(nome, 'w+')
                fichaFuncionario.writelines(listaRegistro[4]+"/"+listaRegistro[5]+"/"+listaRegistro[3]+"\n")
            fichaFuncionario.close()
        else:
            listaRegistro= registro.replace('"','').split(",")
            nome="C:/Users/Helcio/Pictures/TLMC/RPLetNp/Nova pasta/Despesas.txt"
            fichaDespesas=open(nome,"r")
            conteudo = fichaDespesas.readlines()
            conteudo.append(listaRegistro[4]+"/"+listaRegistro[5]+"/"+listaRegistro[6]+"/"+listaRegistro[3]+"\n")
            fichaDespesas = open(nome, 'w')
            fichaDespesas.writelines(conteudo)
            fichaDespesas.close()
def pagamento():
    diretorio="C:/Users/Helcio/Pictures/TLMC/RPLetNp/Nova pasta/Funcionarios/"
    endPagamento="C:/Users/Helcio/Pictures/TLMC/RPLetNp/Nova pasta/Pagamentos.txt"
    fichaPagamentos=open(endPagamento,"w")
    for raiz, pastas, arquivos in os.walk(diretorio,topdown=True):
        for name in arquivos:
            conteudo=[]
            pagamento=0
            caminho=diretorio+name
            fichaFuncionario=open(caminho,"r")
            logFuncionario = fichaFuncionario.readlines()
            for entrada in logFuncionario:
                if "peca" in entrada:
                    pagamento= pagamento+400
            fichaFuncionario= open(caminho,'w')
            fichaFuncionario.close()
            conteudo.append(str(pagamento)+"  "+name.replace(".txt",".")+"\n")
            fichaPagamentos.writelines(conteudo)
    fichaPagamentos.close()

escolha=1
while escolha!='0':
    print("1-Atualizar registro\n2-Gerar folha de pagamento\n 0- sair")
    escolha=input()
    if escolha=='1':
        atualiza()
    if escolha=='2':
        pagamento()