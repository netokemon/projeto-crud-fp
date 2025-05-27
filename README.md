# 🍽️ Restauranty - Sistema de Gerenciamento de Restaurante

**Restauranty** é um sistema de gerenciamento de restaurante em Python que permite o controle de **cardápio**, **mesas** e **pedidos** de forma simples e eficiente via terminal.

---

## 📁 Estrutura do Projeto

```bash
restauranty/
├── app.py
├── CRUD_cardapio.py
├── CRUD_pedidos.py
├── CRUD_mesas.py
├── cardapio.json
├── pedidos.json
└── mesas.json

```

## ▶️ Como Usar

1. Certifique-se de ter o **Python 3** instalado.
2. Instale a biblioteca necessária (caso ainda não tenha):

   ```bash
   pip install pandas

## 📋 Funcionalidades

### `app.py` - Menu Principal
- Exibe o menu principal com opções:
  - Gerenciar **cardápio**
  - Gerenciar **mesas**
  - Gerenciar **pedidos**

---

### `CRUD_cardapio.py` - Gerenciamento de Cardápio
- `criar_prato()` — Adiciona um novo prato ao cardápio.
- `listar_pratos()` — Lista todos os pratos disponíveis.
- `atualizar_prato()` — Altera informações de um prato existente.
- `deletar_prato()` — Remove um prato do cardápio.

---

### `CRUD_mesas.py` - Gerenciamento de Mesas
- `adicionar_mesas()` — Adiciona uma nova mesa.
- `ler_mapa_mesas()` — Lista todas as mesas e seus estados (Livre, Ocupada, Reservada).
- `atualizar_mesas()` — Atualiza o número ou o estado de uma mesa.
- `remover_mesas()` — Remove uma mesa existente.

---

### `CRUD_pedidos.py` - Gerenciamento de Pedidos
- `criar_pedido()` — Registra um novo pedido com pratos selecionados.
- `listar_pedidos()` — Lista todos os pedidos registrados.
- `atualizar_pedido()` — Atualiza pratos, observações ou status de um pedido.
- `deletar_pedido()` — Exclui um pedido específico.