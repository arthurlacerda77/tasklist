def adicionar_tarefa():
  listar_filtro('todos')
  id = int(input('ID da nova tarefa: '))
  desc = input('Descrição: ')
  prioridade = input('Prioridade: ')
  categoria = input('Categoria: ')
  dic = {
    'ID': id,
    'Descrição': desc,
    'Prioridade': prioridade,
    'Categoria': categoria
  }
  dados.append(dic)

def excluir_tarefa():
  listar_filtro('todos')
  id = int(input('ID da tarefa: '))
  for tarefa in dados:
    if tarefa['ID'] == id:
      dados.remove(tarefa)

def listar_filtro(tipo):
  print('ID Descrição                 Prio  Categoria')
  print("-- ------------------------- ----- ----------")
  if tipo == 'Categoria':
    filtro = input('Categoria?')
    for tarefa in dados:
      if tarefa['Categoria'] == filtro:
        print(f"{tarefa['ID']:2} {tarefa['Descrição']:25} {tarefa['Prioridade']:5} {tarefa['Categoria']:10}")
  elif tipo == 'Prioridade':
    filtro = input('Prioridade?')
    for tarefa in dados:
      if tarefa['Prioridade'] == filtro:
          print(f"{tarefa['ID']:2} {tarefa['Descrição']:25} {tarefa['Prioridade']:5} {tarefa['Categoria']:10}")
  else:
    for tarefa in dados:
      print(f"{tarefa['ID']:2} {tarefa['Descrição']:25} {tarefa['Prioridade']:5} {tarefa['Categoria']:10}")
  print('-- ------------------------- ----- -----')

dados = []

while True:
  print('''
          ---------------------
          Tarefas
          ---------------------
          1. Cadastrar nova tarefa
          2. Excluir uma tarefa
          3. Listar todas as tarefas
          4. Listar uma categoria de tarefa          
          5. Listar uma prioridade de tarefa          
          0. Sair
          ---------------------
          ''')
  op = int(input('Informe a opção desejada: '))

  if op == 1:
    print('>>>> Cadastrando nova tarefa')
    adicionar_tarefa()
    print('Cadastramento concluído <<<<\n')
  elif op == 2:
    print('>>>> Excluindo tarefa')
    excluir_tarefa()
    print('Exclusão concluída <<<<\n')
  elif op == 3:
    print('>>>> listando tarefas')
    listar_filtro('todos')
  elif op == 4:
    print('>>>> listando tarefas (Categoria)')
    listar_filtro('Categoria')
  elif op == 5:
    print('>>>> listando tarefas (Prioridade)')
    listar_filtro('Prioridade')
  elif op == 0:
        print('>>>> Saindo da aplicação')
        break
  else:
    print('[ERRO] Opção inválida\n')

  
    
  



  

        


