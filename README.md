# 🎓 Logan - Orientação em Compra de Veículos

Um assistente educativo inteligente que ajuda brasileiros a comprar veículos de forma segura e inteligente, sem gerar grandes dívidas.

---

## 📋 Sobre o Projeto

**Logan** é um agente de IA que ensina como comprar veículos no Brasil de forma consciente. Ele:

✅ Analisa sua renda e capacidade financeira  
✅ Compara opções (financiamento, consórcio, à vista)  
✅ Alerta sobre riscos financeiros  
✅ Usa dados reais de taxas e custos do mercado  
✅ Oferece alternativas seguras e realistas  

**Não é um vendedor** - é um educador financeiro que quer capacitar você a tomar melhores decisões.

---

## 🚀 Como Instalar

### 1️⃣ Clonar o repositório
```bash
git clone https://github.com/joao-Devr/dio-lab-bia-do-futuro.git
cd dio-lab-bia-do-futuro
```

### 2️⃣ Criar ambiente virtual
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

### 3️⃣ Instalar dependências
```bash
pip install -r requirements.txt
```

### 4️⃣ Configurar API Key do Groq

#### Opção A: Adicionar direto no código (não recomendado)
```python
GROQ_API_KEY = "gsk_sua_chave_aqui"
```

#### Opção B: Usar arquivo de secrets (recomendado)
Criar arquivo `.streamlit/secrets.toml`:
```toml
GROQ_API_KEY = "gsk_sua_chave_aqui"
```

**Como pegar a chave:**
1. Acesse https://console.groq.com/keys
2. Crie uma conta (grátis)
3. Copie sua API Key

---

## ▶️ Como Rodar

### Rodar a aplicação
```bash
streamlit run app.py
```

A aplicação vai abrir em `http://localhost:8501`

### Exemplos de Perguntas para Testar

```
❓ "Ganho R$ 2.500/mês e tenho R$ 3.000 guardado. Consigo comprar um carro?"

❓ "Qual é melhor: financiamento ou consórcio?"

❓ "Quanto custa manter um carro novo por mês?"

❓ "Encontrei um carro por R$ 50.000. Faz sentido para mim?"
```

---

## 📁 Estrutura de Pastas

```
projeto/
├── src/
|   └── app.py                      # Aplicação principal (Streamlit)
|   └── requirements.txt            # Dependências Python
│
├── data/                           # Dados Mokados
│   └── perfil_comprador.json       # Perfil do usuário
│   └── taxas_mercado.csv           # Taxas de financiamento/consórcio
│   └── custos_veiculos.json        # Custos de manutenção por tipo
│   └── historico_atendimento.csv   # Histórico de conversas
|
├── docs/
|   └── 01-documentacao-agente.md   # Descricao do Agente
|   └── 02-base-conhecimento.md     # Descricao dos dados utilizados
|   └── 03-prompts.md               # System Prompt 
|   └── 04-metricas.md              # Avaliação e Métrica
|
└── README.md                       # Este arquivo
```

---

## 🛠️ Tecnologias Usadas

- **Python 3.9+** - Linguagem principal
- **Streamlit** - Interface web interativa
- **Groq API** - LLM para respostas inteligentes
- **Pandas** - Processamento de dados (CSV)
- **JSON** - Armazenamento de configurações

---

## 📊 Dados Utilizados

### Taxas de Mercado
```
Financiamento CDC:    1.8% a.m.  (entrada mínima 20%)
Consórcio:            0.15% adm  (sem juros)
Empréstimo Pessoal:   4.5% a.m.  (NUNCA recomendar)
```

### Custos de Veículos
```
Hatch Compacto (Onix, HB20, Gol):
  - Valor: ~R$ 45.000
  - Custos anuais: R$ 5.000

SUV Compacto (Renegade, Kicks):
  - Valor: ~R$ 85.000
  - Custos anuais: R$ 9.400
```

---

## 📝 Exemplo de Resposta do Logan

**Entrada:**
```
Ganho R$ 2.000/mês e quero financiar um Hatch novo de R$ 60.000.
Quanto fica a parcela?
```

**Saída (Logan):**
```
SUA SITUAÇÃO:
- Renda: R$ 2.000/mês
- Máximo seguro (30%): R$ 600/mês

SIMULAÇÃO - HATCH NOVO:
- Parcela: ~R$ 1.430/mês
- Custos (IPVA/Seguro): ~R$ 300/mês
TOTAL: ~R$ 1.730/mês

🚨 Você gastaria 86% da sua renda!

ALTERNATIVAS:
1. Esperar 6-8 meses e juntar mais capital
2. Considerar hatch usado (R$ 25-30k)
3. Explorar consórcio
```

---

## 👨‍💻 Autor

**João Pedro** ([@joao-Devr](https://github.com/joao-Devr))

Desenvolvido como projeto educativo de IA e Finanças.

---
