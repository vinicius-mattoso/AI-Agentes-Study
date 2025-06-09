from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

lider = Agent(
    role="Líder do Projeto",
    goal="Interpretar as entradas do analista e coordenar as etapas do relatório CDR",
    backstory=(
        "Você é o ponto de partida do sistema. Recebe dados como empresa, objetivo e prazos. "
        "Sua função é organizar essa entrada e acionar os agentes subordinados para iniciar o trabalho."
    ),
    llm=llm,
    verbose=True
)
