import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÕES DO AGENTE
OLLA_API_URL = "http://localhost:11434/api/generate"
modelo = "qwen2.5-coder:7b"

# CARREGANDO DADOS
perfil = json.load(open('./data/perfil_comprador.json'))

taxas = pd.read_csv('./data/taxas_mercado.csv')

historico = pd.read_csv('./data/historico_atendimento.csv')

custo_veiculo = json.load(open('./data/custos_veiculos.json'))

# MONTANDO CONTEXTO PARA O AGENTE

contexto = f"""
Cliente Nome: {perfil['nome']}, 
Perfil: {perfil['perfil']}, 
Faixa de Renda: {perfil['faixa_renda']}, 
Caixa Disponível: {perfil['caixa_disponivel']}

INFORMAÇÕES DE MERCADO:
{taxas.to_string(index=False)}

HISTÓRICO DE ATENDIMENTO:
{historico.to_string(index=False)}

CUSTO DE VEÍCULO:
{json.dumps(custo_veiculo, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT PARA O AGENTE

SYSTEM_PROMPT = f""" Você é Logan, um assistente financeiro especializado em educação sobre compra de veículos no Brasil.

Especialidade: Orientação inteligente e segura para compra de veículos
Tom: Educativo, paciente e acessível (como um professor experiente)
Abordagem: Ensinar, não vender. Seus conselhos devem capacitar o usuário a tomar decisões melhores.

REGRAS:
1. Sempre baseie suas respostas nos dados fornecidos
2. Nunca invente informações financeiras
3. Se não souber algo, admita e ofereça alternativas
4. Sempre informe os ricos
5. Foco na educação, não em produto específico
6. Respeite a privacidade e segurança
7. Responda de forma clara e didática, evitando jargões complexos
"""

# CHAMA O AGENTE COM O CONTEXTO E O SYSTEM PROMPT

def chamar_agente(pergunta_usuario):
    prompt = f"""{SYSTEM_PROMPT}

    Conteúdo do contexto:
    {contexto}
    
    Pergunta do usuário:
    {pergunta_usuario}
"""
    
    r = requests.post(OLLA_API_URL, json={"model": modelo,"prompt": prompt, "stream": False})
    return r.json()['response']

    # Interface com Streamlit
st.title("🎓 Logan, o Educador de Compra de Veículos")

if pergunta := st.chat_input("Sua dúvida sobre compras..."):
    st.chat_message("user").write(pergunta)
    with st.spinner("..."):
        st.chat_message("assistant").write(chamar_agente(pergunta))