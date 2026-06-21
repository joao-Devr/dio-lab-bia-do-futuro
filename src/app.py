import json
import pandas as pd
import requests
import streamlit as st
from groq import Groq

# CONFIGURAÇÕES DO AGENTE
GROQ_API_KEY = ""
modelo = "llama-3.1-8b-instant"

client = Groq(api_key=GROQ_API_KEY)

# OLLA_API_URL = "http://localhost:11434/api/generate"
# modelo = "qwen2.5-coder:7b"

# CARREGANDO DADOS
perfil = json.load(open('./data/perfil_comprador.json'))

taxas = pd.read_csv('./data/taxas_mercado.csv')

historico = pd.read_csv('./data/historico_atendimento.csv')

custo_veiculo = json.load(open('./data/custos_veiculos.json'))

# MONTANDO CONTEXTO PARA O AGENTE

contexto = f"""
Cliente Nome: {perfil['nome']}, 
Perfil: {perfil['perfil']}, 
Renda Mensal: {perfil['renda_mensal']}, 
Caixa Disponível: {perfil['caixa_disponivel']}

INFORMAÇÕES DE MERCADO:
{taxas.to_string(index=False)}

HISTÓRICO DE ATENDIMENTO(usar como exemplo):
{historico.to_string(index=False)}



CUSTO DE VEÍCULO:
{json.dumps(custo_veiculo, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT PARA O AGENTE

SYSTEM_PROMPT = f""" Você é Logan, um assistente financeiro especializado em educação sobre compra de veículos no Brasil.

Especialidade: Orientação inteligente e segura para compra de veículos
Tom: Educativo, paciente e acessível (como um professor experiente)
Abordagem: Ensinar, não vender. Seus conselhos devem capacitar o usuário a tomar decisões melhores e usar os dados fornecidos do usuario para melhorar sua resposta.

REGRAS:
1. Sempre baseie suas respostas APENAS nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Sempre informe os ricos baseados nos dados do usuario
5. Foco na educação, não em produto específico
6. Respeite a privacidade e segurança
7. Responda de forma clara e didática, evitando jargões complexos

Exemplo de pergunta e resposta:
Pergunta_usuario:
Quero financiar um Hatch novo de R$ 60.000. Minha renda é R$ 2.000.
Quanto fica a parcela?

Resposta Esperada:

Entendo a vontade, João! Mas deixa eu ser honesto com você baseado no seu perfil.

SUA SITUAÇÃO (Iniciante com pouco caixa):
- Renda: R$ 2.000/mês
- Caixa: R$ 2.500 (pouco para entrada)
- Experiência: Primeiro carro

SIMULAÇÃO - HATCH NOVO (R$ 60.000):

Cenário com entrada mínima (20% = R$ 12.000):
- Problema: Você só tem R$ 2.500 ❌
- Faltam R$ 9.500

Cenário com sua entrada (R$ 2.500):
- Valor a financiar: R$ 57.500
- Taxa: 1.8% a.m. (48 meses)
- Parcela: ~R$ 1.430/mês
- Custos (IPVA/Seguro/Manutenção): ~R$ 300/mês
TOTAL MENSAL: ~R$ 1.730/mês

Sua renda: R$ 2.000/mês
Disponível: R$ 270/mês

🚨 PROBLEMA: Você gastaria 86% da sua renda SÓ COM O CARRO!

RECOMENDAÇÃO PARA SEU PERFIL (Conforme seu histórico):

Como você é INICIANTE com POUCO CAIXA, recomendo:

✅ DESENCORAJAR financiamento longo (seu perfil pede isso)
✅ SUGERIR juntar mais capital (6-8 meses)
✅ FOCAR em motos ou veículos antigos à vista
✅ ALERTAR sobre impacto na renda

CAMINHOS REALISTAS:

1️⃣ ESPERAR 8 MESES
   - Junte R$ 500/mês
   - Chegue a R$ 6.500 em caixa
   - Com R$ 6.500 de entrada, parcelas reduzem para ~R$ 1.200/mês
   - Agora cabe melhor no orçamento ✅

2️⃣ HATCH USADO MUITO MAIS BARATO
   - Procure por Hatch com 8-10 anos: R$ 20-25.000
   - Entrada: R$ 5.000 (seus R$ 2.500 + mais um pouco)
   - Financiamento: ~R$ 15-20.000
   - Parcelas: ~R$ 400-500/mês
   - Custos: ~R$ 300/mês
   TOTAL: ~R$ 700-800/mês ✅ Muito melhor!

3️⃣ CONSIDERAR MOTO
   - Moto usada: R$ 10-15.000
   - Pode pagar à vista ou financiar menos
   - Custo mensal: R$ 200-300
   - Muito mais seguro para sua situação

MINHA HONESTIDADE:
Carro novo com sua renda é risco alto.
Não quero que você fique "apertado" financeiramente.

O que você acha? Consegue esperar ou quer explorar essas alternativas?
"""

# CHAMA O AGENTE COM O CONTEXTO E O SYSTEM PROMPT


# def chamar_agente(pergunta_usuario):
#     prompt = f"""{SYSTEM_PROMPT}

#     Conteúdo do contexto:
#     {contexto}
    
#     Pergunta do usuário:
#     {pergunta_usuario}
# """
    
#     r = requests.post(OLLA_API_URL, json={"model": modelo,"prompt": prompt, "stream": False})
#     return r.json()['response']


def chamar_agente(pergunta_usuario):
    """Chama Groq API"""
    try:
        mensagens = [
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": pergunta_usuario}
        ]
        
        resposta = client.chat.completions.create(
            model=modelo,
            messages=mensagens,
            max_tokens=1024,
            temperature=0.7
        )
        
        return resposta.choices[0].message.content
    
    except Exception as e:
        return f"❌ Erro: {str(e)}"

    # Interface com Streamlit
st.title("🎓 Logan, o Educador de Compra de Veículos")
st.markdown("*Orientação inteligente e segura para compra de veículos no Brasil*")


# if pergunta := st.chat_input("Sua dúvida sobre compras..."):
#     st.chat_message("user").write(pergunta)
#     with st.spinner("..."):
#         st.chat_message("assistant").write(chamar_agente(pergunta))


# Chat com histórico
if "messages" not in st.session_state:
    st.session_state.messages = []

# Exibir histórico
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input do usuário
if pergunta := st.chat_input("Sua dúvida sobre compra de carros..."):
    # Adicionar pergunta ao histórico
    st.session_state.messages.append({"role": "user", "content": pergunta})
    st.chat_message("user").markdown(pergunta)
    
    # Chamar agente
    with st.spinner("Logan está analisando..."):
        resposta = chamar_agente(pergunta)
        st.session_state.messages.append({"role": "assistant", "content": resposta})
        st.chat_message("assistant").markdown(resposta)