# 🧠 Roadmap: Construção de Agentes e Multi-Agentes com LLMs

Este roadmap orienta a criação de agentes e sistemas multi-agentes que utilizam Modelos de Linguagem Grande (LLMs) como motor de raciocínio, com ou sem uso de memória.

---

## 🔹 1️⃣ Fundamentos

- **Agentes Reativos**: Respondem diretamente às entradas sem memória.
- **Agentes Baseados em Modelo**: Mantêm um estado interno para decisões mais informadas.
- **Agentes com Objetivos**: Planejam ações para alcançar metas específicas.
- **Agentes de Aprendizado**: Aprendem com experiências passadas para melhorar decisões futuras.

---

## 🔹 2️⃣ Escolha de Ferramentas

- **LLMs**:
  - [OpenAI GPT-3.5/4](https://platform.openai.com/)
  - [Mistral](https://mistral.ai/)
  - [LLaMA](https://ai.meta.com/llama/)
- **Frameworks**:
  - [LangChain](https://www.langchain.com/)
  - [LlamaIndex](https://www.llamaindex.ai/)
  - [AgentLite](https://github.com/SalesforceAIResearch/AgentLite)
  - [Atomic Agents](https://github.com/BrainBlend-AI/atomic-agents)

---

## 🔹 3️⃣ Construção de um Agente Simples

1. **Percepção**: Recebe descrições do ambiente em linguagem natural.
2. **Raciocínio com LLM**: Utiliza prompts para interpretar e decidir ações.
3. **Ação**: Executa a ação decidida no ambiente.
4. **Memória (Opcional)**:
   - **Curto Prazo**: Armazena interações recentes.
   - **Longo Prazo**: Utiliza bancos vetoriais como FAISS ou Chroma.

---

## 🔹 4️⃣ Expansão para Multi-Agentes

- **Arquitetura**:
  - **Planejador**: Define estratégias e metas.
  - **Executores**: Realizam tarefas específicas.
- **Comunicação**: Troca de informações entre agentes para coordenação.
- **Orquestração**: Gerencia a interação e colaboração entre agentes.

---

## 🔹 5️⃣ Integração de Memória

- **Sem Memória**: Cada decisão é independente.
- **Memória de Curto Prazo**: Contexto limitado às últimas interações.
- **Memória de Longo Prazo**: Acesso a informações históricas e contextuais amplas.

---

## 🔹 6️⃣ Recursos Recomendados

- **Papers**:
  - [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629)
  - [AgentLite: A Lightweight Library for Building and Advancing Task-Oriented LLM Agent System](https://arxiv.org/abs/2402.15538)
- **Tutoriais**:
  - [LangChain Agents Tutorial](https://python.langchain.com/docs/tutorials/agents/)
  - [Building LangChain Agents to Automate Tasks in Python](https://www.datacamp.com/tutorial/building-langchain-agents-to-automate-tasks-in-python)

---


