from crewai import Task
from agents.level_3_editores import editor_intro, editor_metodo, editor_conclusao
from tasks.pesquisa_tasks import pesquisa_task

# INTRODUÇÃO — breve e contextual
intro_task = Task(
    description="""
        Com base nos dados da pesquisa, escreva a introdução do relatório.

        Foque em contextualizar o problema da empresa, destacando o cenário atual, os desafios enfrentados
        e a relevância do tema proposto para o setor em questão.

        O texto deve ser claro, conciso e servir como porta de entrada para o leitor. Evite repetições e aprofundamentos
        que serão abordados na seção de metodologia.
    """,
    expected_output="Texto introdutório claro e objetivo contextualizando o projeto.",
    agent=editor_intro,
    context=[pesquisa_task]
)

# METODOLOGIA — a seção mais importante
metodo_task = Task(
    description="""
        Redija a seção de metodologia do relatório com o máximo de profundidade e detalhamento possível.

        Instruções:
        - Descreva as etapas do projeto para solucionar o problema apresentado.
        - Apresente os perfis dos profissionais que atuarão (ex: cientista de dados, analista de negócios, engenheiro de machine learning).
        - Liste as ferramentas ou tecnologias previstas (ex: Power BI, Serviços de cloud como os da AWS, utilização de modelos LLM como o GPTs, etc).
        - Se possível, represente o fluxo de etapas em formato descritivo ou em forma de tabela/fluxograma textual.
        - Destaque interdependências entre fases e a lógica por trás da ordem proposta.

        O conteúdo dessa seção deve compor a maior parte do relatório final, com cerca de 4 a 6 páginas (estimadas).
        Seja técnico, organizado e direto.
    """,
    expected_output="Texto detalhado sobre as etapas do projeto, perfis envolvidos e ferramentas utilizadas, com estruturas como listas e tabelas.",
    agent=editor_metodo,
    context=[pesquisa_task]
)

# CONCLUSÃO — encerramento e próximos passos
conclusao_task = Task(
    description="""
        Elabore a conclusão do relatório, retomando os principais pontos do projeto.

        Inclua:
        - Um resumo dos desafios enfrentados pela empresa.
        - A importância da metodologia escolhida.
        - Recomendações para os próximos passos (ex: fases futuras, avaliação de resultados, escalabilidade).
        - Tom de encerramento objetivo, mas com proposta de continuidade.

        Evite repetir frases da introdução. Esta seção deve refletir a maturidade do plano apresentado.
    """,
    expected_output="Texto conclusivo com encerramento estratégico e recomendações.",
    agent=editor_conclusao,
    context=[intro_task, metodo_task]
)