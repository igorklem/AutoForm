# -*- coding: ISO-8859-1 -*-
import configparser
import os.path
import subprocess

import pymsgbox
from selenium import webdriver
from selenium.webdriver.common.by import By
from win32api import GetSystemMetrics

cfg = configparser.ConfigParser()
cfg.read('CONFIG.ini', encoding='utf-8')

nome = cfg.get('config', 'nome')
cpf = cfg.get('config', 'cpf')
rg = cfg.get('config', 'rg')
genero = cfg.get('config', 'genero')
orientacao = cfg.get('config', 'orientacao')
estadocivil = cfg.get('config', 'estadocivil')
foto = cfg.get('config', 'foto')
curriculo = cfg.get('config', 'curriculo')
email = cfg.get('config', 'email')
senha = cfg.get('config', 'senha')
nascimento = cfg.get('config', 'nascimento')
tel = cfg.get('config', 'tel')
whats = cfg.get('config', 'whats')
pai = cfg.get('config', 'pai')
profpai = cfg.get('config', 'profpai')
mae = cfg.get('config', 'mae')
profmae = cfg.get(u'config', 'profmae')
cep = cfg.get('config', 'cep')
numero = cfg.get('config', 'numero')
comp = cfg.get('config', 'comp')
estado_natur = cfg.get('config', 'estado_natur')
cidade_natur = cfg.get('config', 'cidade_natur')
raca = cfg.get('config', 'raca')
face = cfg.get('config', 'face')
linkedin = cfg.get('config', 'linkedin')
github = cfg.get('config', 'github')
escola = cfg.get('config', 'escola')
situacao = cfg.get('config', 'situacao')
estudando = cfg.get('config', 'estudando')
turno = cfg.get('config', 'turno')
escolaEnt = cfg.get('config', 'escolaEnt')
idioma = cfg.get('config', 'idioma')
nivel = cfg.get('config', 'nivel')
obsIdioma = cfg.get('config', 'obsIdioma')
exp = cfg.get('config', 'exp')
cursos = cfg.get('config', 'cursos')
js = cfg.get('config', 'js')
jsExp = cfg.get('config', 'jsExp')
java = cfg.get('config', 'java')
javaExp = cfg.get('config', 'javaExp')
python = cfg.get('config', 'python')
pythonExp = cfg.get('config', 'pythonExp')
go = cfg.get('config', 'go')
goExp = cfg.get('config', 'goExp')
delphi = cfg.get('config', 'delphi')
delphiExp = cfg.get('config', 'delphiExp')
c = cfg.get('config', 'c')
cExp = cfg.get('config', 'cExp')
cpp = cfg.get('config', 'cpp')
cppExp = cfg.get('config', 'cppExp')
csharp = cfg.get('config', 'csharp')
csharpExp = cfg.get('config', 'csharpExp')
r = cfg.get('config', 'r')
rExp = cfg.get('config', 'rExp')
php = cfg.get('config', 'php')
phpExp = cfg.get('config', 'phpExp')
rust = cfg.get('config', 'rust')
rustExp = cfg.get('config', 'rustExp')
kotlin = cfg.get('config', 'kotlin')
kotlinExp = cfg.get('config', 'kotlinExp')
swift = cfg.get('config', 'swift')
swiftExp = cfg.get('config', 'swiftExp')
sabendo = cfg.get('config', 'sabendo')
motivo = cfg.get('config', 'motivo')

def Acessar():
    print('Abriu o Chrome...')

    navegador.get('https://t-systems.proway.com.br/inscricao/')
    print('Abriu o site...')
    navegador.set_window_size(width=GetSystemMetrics(0) / 1.3, height=GetSystemMetrics(1) / 1.05)
    print('Alterou o tamanho da janela...')

    print("Preenchendo os dados...")

    Preencher('/html/body/div/div/div/form/div/div[2]/div[1]/div/input', nome, 'Preencheu o nome', 'Falha ao preencher o nome...')
    Preencher('/html/body/div/div/div/form/div/div[2]/div[2]/div[1]/input', cpf, 'Preencheu o CPF', 'Falha ao preencher o CPF...')
    Preencher('/html/body/div/div/div/form/div/div[2]/div[2]/div[2]/input', rg, 'Preencheu o RG', 'Falha ao preencher o RG...')
    Preencher('// *[ @ id = "genero"]', genero, 'Preencheu o g�nero', 'Falha ao preencher o g�nero...')
    Preencher('//*[@id="orientacaoSexual"]', orientacao, 'Preencheu a orienta��o sexual', 'Falha ao preencher a orienta��o sexual...')
    Preencher('//*[@id="estadoCivil"]', estadocivil, 'Preencheu o estado civil', 'Falha ao preencher o estado civil...')
    Preencher('//*[@id="inputFoto"]', foto, 'Selecionou a foto', 'Falha ao selecionar a foto...')
    Preencher('//*[@id="inputCurriculo"]', curriculo, 'Selecionou o curr�culo', 'Falha ao selecionar o curr�culo...')
    Preencher('//*[@id="email"]', email, 'Preencheu o e-mail', 'Falha ao preencher o e-mail...')
    Preencher('// *[ @ id = "email_conf"]', email, 'Preencheu o e-mail de confirma��o', 'Falha ao preencher o e-mail de confirma��o...')
    Preencher('//*[@id="senha"]', senha, 'Preencheu a senha', 'Falha ao preencher a senha...')
    Preencher('//*[@id="senha_conf"]', senha, 'Preencheu a confirma��o da senha', 'Falha ao preencher a confirma��o da senha...')
    Preencher('//*[@id="dataNascimento"]', nascimento, 'Preencheu a data de nascimento', 'Falha ao preencher a data de nascimento...')
    Preencher('//*[@id="telefone"]', tel, 'Preencheu o telefone', 'Falha ao preencher o telefone...')
    Preencher('//*[@id="whatsapp"]', whats, 'Preencheu o WhatsApp', 'Falha ao preencher o WhatsApp...')
    Preencher('//*[@id="nomepai"]', pai, 'Preencheu o nome do pai', 'Falha ao preencher o nome do pai...')
    Preencher('//*[@id="profissaopai"]', profpai, 'Preencheu a profiss�o do pai', 'Falha ao preencher a profiss�o do pai...')
    Preencher('//*[@id="nomemae"]', mae, 'Preencheu o nome da m�e', 'Falha ao preencher o nome da m�e...')
    Preencher('//*[@id="profissaomae"]', profmae, 'Preencheu a profiss�o da m�e', 'Falha ao preencher a profiss�o da m�e...')
    Preencher('//*[@id="cep"]', cep, 'Preencheu o CEP', 'Falha ao preencher o CEP...')
    Preencher('//*[@id="numero"]', numero, 'Preencheu o n�mero', 'Falha ao preencher o n�mero...')
    Preencher('//*[@id="complemento"]', comp, 'Preencheu o complemento', 'Falha ao preencher o complemento...')
    Preencher('/html/body/div/div/div/form/div/div[3]/div[4]/div[1]/select', estado_natur, 'Preencheu o estado de naturalidade', 'Falha ao preencher o estado de naturalidade...')
    navegador.implicitly_wait(10)
    # cidade naturalidade no final propositalmente...
    Preencher('//*[@id="raca"]', raca, 'Preencheu a ra�a', 'Falha ao preencher a ra�a...')
    Preencher('/html/body/div/div/div/form/div/div[4]/div[5]/input', face, 'Preencheu o link do Facebook', 'Falha ao preencher o link do Facebook...')
    Preencher('/html/body/div/div/div/form/div/div[4]/div[6]/div[1]/input', linkedin, 'Preencheu o link do Linkedin', 'Falha ao preencher o link do Linkedin...')
    Preencher('/html/body/div/div/div/form/div/div[4]/div[6]/div[2]/input', github, 'Preencheu o link do GitHub', 'Falha ao preencher o link do GitHub...')
    Preencher('//*[@id="escolaridade"]', escola, 'Preencheu a escolaridade', 'Falha ao preencher a escolaridade...')
    Preencher('//*[@id="situacaoEstudo"]', situacao, 'Preencheu a situa��o de estudo', 'Falha ao preencher a situa��o de estudo...')

    if estudando == 'Sim':
        Clicar('/html/body/div/div/div/form/div/div[5]/div[1]/div[3]/div[2]/button[2]', 'Selecionou "Estudando: Sim"', 'Falha ao Selecionar "Estudando: Sim"...')
        Preencher('//*[@id="turnoEstudo"]', turno, 'Selecionou o turno de estudo', 'Falha ao selecionar o turno de estudo...')
        Preencher('/html/body/div/div/div/form/div/div[5]/div[2]/div[2]/input', escolaEnt, 'Preencheu a institui��o/entidade', 'Falha ao preencher a institui��o/entidade...')

    Preencher('//*[@id="idioma"]', idioma, 'Preencheu o idioma', 'Falha ao preencher o idioma...')
    Preencher('//*[@id="idiomaNivel"]', nivel, 'Preencheu o n�vel do idioma', 'Falha ao preencher o n�vel do idioma...')
    Preencher('/html/body/div/div/div/form/div/div[5]/div[3]/div[3]/input', obsIdioma, 'Preencheu a observa��o do idioma', 'Falha ao preencher a observa��o do idioma...')
    Preencher('/html/body/div/div/div/form/div/div[6]/div[1]/div/textarea', exp, 'Preencheu as experi�ncias profissionais', 'Falha ao preencher as experi�ncias profissionais...')
    Preencher('/html/body/div/div/div/form/div/div[6]/div[2]/div/textarea', cursos, 'Preencheu "Outros cursos"', 'Falha ao preencher "Outros cursos"...')

    if js == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[1]/label/input', 'Selecionou "Javascript: Sim"', 'Falha ao Selecionar "Javascript: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[1]/select', jsExp, 'Preencheu Experi�ncia com Javascript', 'Falha ao preencher Experi�ncia com Javascript...')

    if java == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[2]/label/input', 'Selecionou "Java: Sim"', 'Falha ao Selecionar "Java: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[2]/select', javaExp, 'Preencheu Experi�ncia com Java', 'Falha ao preencher Experi�ncia com Java...')

    if python == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[3]/label/input', 'Selecionou "Python: Sim"', 'Falha ao Selecionar "Python: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[3]/select', pythonExp, 'Preencheu Experi�ncia com Python', 'Falha ao preencher Experi�ncia com Python...')

    if go == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[4]/label/input', 'Selecionou "Go: Sim"', 'Falha ao Selecionar "Go: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[4]/select', goExp, 'Preencheu Experi�ncia com Go', 'Falha ao preencher Experi�ncia com Go...')

    if delphi == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[5]/label/input', 'Selecionou "Delphi: Sim"', 'Falha ao Selecionar "Delphi: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[5]/select', delphiExp, 'Preencheu Experi�ncia com Delphi', 'Falha ao preencher Experi�ncia com Delphi...')

    if c == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[6]/label/input', 'Selecionou "C: Sim"', 'Falha ao Selecionar "C: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[6]/select', cExp, 'Preencheu Experi�ncia com C', 'Falha ao preencher Experi�ncia com C...')

    if cpp == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[7]/label/input', 'Selecionou "C++: Sim"', 'Falha ao Selecionar "C++: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[7]/select', cppExp, 'Preencheu Experi�ncia com C++', 'Falha ao preencher Experi�ncia com C++...')

    if csharp == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[8]/label/input', 'Selecionou "C#: Sim"', 'Falha ao Selecionar "C#: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[8]/select', csharpExp, 'Preencheu Experi�ncia com C#', 'Falha ao preencher Experi�ncia com C#...')

    if r == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[9]/label/input', 'Selecionou "R: Sim"', 'Falha ao Selecionar "R: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[9]/select', rExp, 'Preencheu Experi�ncia com R', 'Falha ao preencher Experi�ncia com R...')

    if php == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[10]/label/input', 'Selecionou "PHP: Sim"', 'Falha ao Selecionar "PHP: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[10]/select', phpExp, 'Preencheu Experi�ncia com PHP', 'Falha ao preencher Experi�ncia com PHP...')

    if rust == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[11]/label/input', 'Selecionou "Rust: Sim"', 'Falha ao Selecionar "Rust: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[11]/select', rustExp, 'Preencheu Experi�ncia com Rust', 'Falha ao preencher Experi�ncia com Rust...')

    if kotlin == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[12]/label/input', 'Selecionou "Kotlin: Sim"', 'Falha ao Selecionar "Kotlin: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[12]/select', kotlinExp, 'Preencheu Experi�ncia com Kotlin', 'Falha ao preencher Experi�ncia com Kotlin...')

    if swift == "Sim":
        Clicar('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[13]/label/input', 'Selecionou "Swift: Sim"', 'Falha ao Selecionar "Swift: Sim"...')
        navegador.implicitly_wait(5)
        Preencher('/html/body/div/div/div/form/div/div[6]/div[3]/div/div/div/div[13]/select', swiftExp, 'Preencheu Experi�ncia com Swift', 'Falha ao preencher Experi�ncia com Swift...')

    Preencher('//*[@id="comoFicouSabendo"]', sabendo, 'Preencheu "Como ficou sabendo do programa"', 'Falha ao preencher "Como ficou sabendo do programa"...')
    Preencher('/html/body/div/div/div/form/div/div[6]/div[5]/div/textarea', motivo, 'Preencheu "Por qual motivo voc� quer ser selecionado?"', 'Falha ao preencher "Por qual motivo voc� quer ser selecionado?"...')

    Preencher('//*[@id="codCidadeNascimento"]', cidade_natur, 'Preencheu a cidade de naturalidade', 'Falha ao preencher a cidade de naturalidade...')

    Clicar('/html/body/div/div/div/form/div/div[7]/label[1]/input', 'Marcou "Declaro que li as condi��es..."', 'Falha ao Selecionar "Declaro que li as condi��es..."...')

    pymsgbox.alert("Processo conclu�do. Verifique se todos os dados foram preenchidos corretamente e se o envio ocorreu normalmente e clique em OK para finalizar o navegador")
    navegador.close()

def Preencher(campo, form, msgOK, msgFalha):
    try:
        navegador.find_element(By.XPATH, campo).send_keys(form)
        print(msgOK)
    except:
        print(msgFalha)

def Clicar(campo, msgOK, msgFalha):
    try:
        navegador.find_element(By.XPATH, campo).click()
        print(msgOK)
    except:
        print(msgFalha)

if os.path.exists(r'C:\\Program Files (x86)\\Google\\Chrome\\Application\\'):
    output = subprocess.check_output(
    r'wmic datafile where name="C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" get Version /value',
    shell=True
)
    chrome_version = output.decode('utf-8').split('.')
    chrome_version = chrome_version[0].replace('\n', '')
    chrome_version = chrome_version.replace('Version=', '')
    chrome_version = int(chrome_version)

    if chrome_version == 103:
        s = r'bin\chromedriver_103.exe'
        print('Google Chrome installed in version 103')
        print('Google Chrome instalado na vers�o 103')
        navegador = webdriver.Chrome(s)
        Acessar()
    elif chrome_version == 104:
        s = r'bin\chromedriver_104.exe'
        print('Google Chrome installed in version 104')
        print('Google Chrome instalado na vers�o 104')
        navegador = webdriver.Chrome(s)
        Acessar()
    else:
        print('Please, install the last version of Google Chrome in your system before use this software')
        print('Por favor, instale a �ltima vers�o do Google Chrome antes de usar esse software')

else:
    print('Google chrome n�o instalado na pasta padr�o...')