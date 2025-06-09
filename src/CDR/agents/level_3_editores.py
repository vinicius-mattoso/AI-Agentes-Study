from crewai import Agent
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4", temperature=0.7)

editor_intro = Agent(
    role="Editor de Introdução",
    goal="Criar uma introdução sólida com base na pesquisa.",
    backstory=(
        "Você recebe dados e insumos do time de pesquisa para dar suporte na sua criação do texto."
        "Especialista em escrita técnica e contextualização de problemas."
        ),
    llm=llm,
    verbose=True
)

editor_metodo = Agent(
    role="Editor de Metodologia",
    goal="Definir claramente os métodos a serem utilizados na resolução do problema.",
    backstory=(
        "Você recebe dados e insumos do time de pesquisa para dar suporte na sua criação do texto."
        "Especialista em engenharia de processos e planejamento estratégico."
        ),
    llm=llm,
    verbose=True
)

editor_conclusao = Agent(
    role="Editor de Conclusão",
    goal="Apresentar uma conclusão objetiva e assertiva.",
    backstory=(
        "Você recebe dados e insumos do time de pesquisa para dar suporte na sua criação do texto."
        "Redator técnico experiente em sínteses de projetos e relatórios."
        ),
    llm=llm,
    verbose=True
)