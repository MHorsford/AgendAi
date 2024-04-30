# AgendAi

O **AgendAi** é um sistema de agendamento simples e fácil de usar, desenvolvido em Python. Com ele, você pode criar e gerenciar tarefas, configurar alarmes e verificar suas tarefas agendadas.

## Funcionalidades

- Adicionar uma tarefa com nome, descrição e data/hora específicas.
- Adicionar uma tarefa com alarme diário.
- Verificar as tarefas agendadas.
- Modificar uma tarefa existente.
- Excluir uma tarefa.
- Iniciar o sistema para verificar e acionar os alarmes agendados.

## Requisitos

- Python 3.x
- Bibliotecas: `csv`, `datetime`, `os`, `playsound`

## Como usar

1. Clone o repositório para sua máquina local:

```bash
git clone https://github.com/seu-usuario/AgendAi.git
```

2. Navegue para o diretório do projeto:

```bash
cd AgendAi
```

3. Certifique-se de ter todas as bibliotecas necessárias instaladas:

```bash
pip install playsound==1.2.2
```

4. Execute o menu principal:

```bash
python agendai.py
python menu.py
```

## Como usar o sistema

Ao iniciar o sistema, você terá várias opções disponíveis:

1. **Adicionar uma tarefa:** Digite as informações solicitadas para criar uma nova tarefa. Você pode escolher entre uma tarefa com data/hora específicas ou uma tarefa com alarme diário.

2. **Verificar tarefas:** Veja todas as tarefas agendadas e suas informações.

3. **Modificar uma tarefa:** Escolha a tarefa que deseja modificar e selecione qual informação deseja alterar (nome, descrição, data/hora ou modo de alarme).

4. **Excluir uma tarefa:** Escolha a tarefa que deseja excluir da lista.

5. **Iniciar o sistema:** Verifica as tarefas agendadas e dispara os alarmes para as tarefas que estiverem no momento correto.

0. **Sair:** Encerra o programa.

## Observações

- As tarefas criadas e suas modificações são armazenadas em um arquivo `savetask.csv` para serem recuperadas posteriormente.

## Contribuindo

Se você encontrar algum problema, tiver sugestões ou quiser contribuir com o projeto, sinta-se à vontade para abrir uma **Issue** ou enviar um **Pull Request**. Estamos abertos a melhorias e novas funcionalidades!

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter mais detalhes.