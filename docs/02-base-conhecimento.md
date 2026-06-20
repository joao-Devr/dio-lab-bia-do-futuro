# Base de Conhecimento

## Dados Utilizados

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `perfil_comprador.json` | JSON | Identificar a capacidade de pagamento e o momento financeiro do usuário. |
| `custos_veiculos.json` | JSON | Fornecer médias de custos ocultos (IPVA, seguro, manutenção) por categoria de veículo. |
| `taxas_mercado.csv` | CSV | Base de cálculo para comparar financiamento, consórcio e compra à vista. |
| `checklist_seguranca.json` | JSON | Guiar o usuário nos passos práticos (Consulta Detran, vistoria cautelar, tabela FIPE). |
| `historico_atendimento.csv` | CSV | Contextualizar interações anteriores |

---

## Adaptações nos Dados

Os dados mockados foram construídos para refletir a realidade atual do mercado automotivo brasileiro. Foram incluídas taxas médias de juros praticadas pelos bancos (variando de 1.5% a 2.5% ao mês) e categorias genéricas de veículos (Hatch, Sedan, SUV) com estimativas de custos anuais. O objetivo não é dar o preço exato do carro, mas ensinar o impacto financeiro da compra.

---

## Estratégia de Integração

### Como os dados são carregados?
Os arquivos JSON e CSV são carregados via Python no back-end (Streamlit). Quando o usuário inicia a conversa e fornece sua renda e valor em caixa, o sistema filtra o `perfil_comprador.json` e busca as taxas no `taxas_mercado.csv`.

### Como os dados são usados no prompt?
Os dados filtrados são injetados dinamicamente no **System Prompt** do Ollama. O modelo não tem acesso direto aos arquivos, mas recebe um resumo em texto puro do perfil do cliente e das métricas de mercado relevantes para aquela interação, garantindo respostas embasadas e reduzindo alucinações.

---

## Exemplo de Contexto Montado

```text
Você é o Logan. Use os dados abaixo para aconselhar o usuário:

Dados do Cliente:
- Renda Mensal: R$ 4.000
- Valor guardado: R$ 15.000
- Objetivo: Primeiro carro (usado)

Dados de Mercado Injetados:
- Categoria Recomendada: Hatch Compacto (ex: Ônix, HB20, Gol).
- Custo Anual Médio (IPVA + Seguro + Manutenção): R$ 4.500
- Taxa média de financiamento atual: 1.8% a.m.

Diretriz: Explique ao usuário que o custo do carro não é apenas a parcela. Calcule por cima quanto ele gastaria por mês mantendo um Hatch Compacto.