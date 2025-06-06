# from crewai import Task
# from agents.level_4_guardrail import guardrail
# from tasks.edicao_tasks import intro_task, metodo_task, conclusao_task

# revisar_task = Task(
#     description="Revisar todos os textos (introdução, metodologia e conclusão), corrigindo falhas gramaticais e possíveis erros éticos.",
#     expected_output="Texto revisado e validado.",
#     agent=guardrail,
#     context=[intro_task, metodo_task, conclusao_task]
# )

from crewai import Task
from agents.level_4_guardrail import guardrail
from tasks.edicao_tasks import intro_task, metodo_task, conclusao_task
from contexto.context_loader import carregar_contexto
from textwrap import dedent

# Carrega dados do contexto
ctx = carregar_contexto()
publico = ctx['publico_alvo']
tom_global = publico['linguagem']
perfil_alvo = publico['perfil']
foco = publico['foco']

# Task do guard-rail refinada
revisar_task = Task(
    description=dedent(f"""
        Revise criticamente os textos de introdução, metodologia e conclusão do relatório.

        ⚙️ Público-alvo: {perfil_alvo}
        🗣️ Tom desejado: {tom_global}
        🎯 Foco principal: {foco}

        Objetivos da revisão:
        - Corrigir erros gramaticais, concordância e pontuação.
        - Uniformizar o estilo entre as seções, mantendo o mesmo nível de formalidade.
        - Remover repetições, frases vagas e jargões técnicos desnecessários.
        - Garantir que o texto reflita clareza, coerência e objetividade.
        - Verificar e corrigir qualquer desvio ético, como viés, promessas irreais ou linguagem sensível.
        - Melhorar a fluidez sem alterar o sentido técnico do conteúdo.

        Ao final, produza um texto contínuo, pronto para ser formatado como relatório profissional.
    """),
    expected_output="Texto final revisado, coeso, claro e com linguagem apropriada ao público corporativo.",
    agent=guardrail,
    context=[intro_task, metodo_task, conclusao_task]
)
