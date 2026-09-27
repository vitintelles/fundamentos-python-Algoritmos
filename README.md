# 🐍 Python: Fundamentos e Algoritmos

Repositório dedicado ao estudo, prática e consolidação de conceitos fundamentais de programação, lógica e estruturas de dados utilizando Python.

---

## Projetos e Práticas

### 1. Gerenciador de Tarefas via Terminal (CLI)
Um sistema interativo em linha de comando desenvolvido para organização e controle de tarefas.

#### Funcionalidades:
- **Adicionar Tarefa:** Cadastro de tarefas com nome e categoria (status inicial: *Pendente*).
- **Listar Tarefas:** Exibição enumerada de todas as tarefas cadastradas, mostrando o status atual e a categoria.
- **Concluir Tarefa:** Atualização do status de uma tarefa específica para *Concluída* com validação de índice.
- **Validação de Entradas:** Tratamento de erros para impedir travamento por digitação incorreta do usuário.

#### Conceitos Aplicados:
- **Estruturas de Repetição:** `while True` para manutenção do menu e controle de fluxo.
- **Estruturas Condicionais:** `if / elif / else` para direcionamento das opções do menu.
- **Coleções de Dados:** Listas (`list`) para armazenamento sequencial e Dicionários (`dict`) para representação estruturada de cada tarefa (chave-valor).
- **Funções Nativas:** `enumerate()` para indexação dinâmica e `len()` para verificação de tamanho de listas.
- **Tratamento de Exceções:** Bloco `try / except (ValueError)` para garantir robustez no recebimento de inteiros.

---

## Como Executar o Projeto

1. Certifique-se de ter o **Python 3.14** instalado.
2. Clone o repositório:
````bash
git clone https://github.com/vitintelles/fundamentos-python-Algoritmos.git