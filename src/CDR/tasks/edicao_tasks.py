from crewai import Task
from agents.level_3_editores import editor_intro, editor_metodo, editor_conclusao
from tasks.pesquisa_tasks import pesquisa_task
from contexto.context_loader import carregar_contexto
from textwrap import dedent

ctx = carregar_contexto()
projeto = ctx['projeto']
intro_cfg = ctx['agentes']['editor_intro']
metodo_cfg = ctx['agentes']['editor_metodologia']
conclusao_cfg = ctx['agentes']['editor_conclusao']

# INTRODUÇÃO — contextualização estratégica
intro_task = Task(
    description=dedent(f"""
        Com base nas informações pesquisadas, elabore a introdução do relatório para o projeto da empresa {projeto['empresa']}, atuante no setor {projeto['setor']}.

        Objetivo do projeto: {projeto['objetivo']}

        Contexto: {projeto['contexto']}

        Diretrizes:
        - Apresente o cenário atual enfrentado pela empresa e os desafios específicos do setor.
        - Contextualize o problema de forma clara e acessível ao leitor corporativo.
        - Evite aprofundar aspectos técnicos — isso será tratado na seção de metodologia.
        - Mantenha tom {intro_cfg['tom']}.
        - Evitar repetições {intro_cfg['evitar_repeticao']}

        Essa introdução deve preparar o leitor para entender a motivação por trás do projeto e a relevância do tema abordado no restante do relatório.
    """),
    expected_output="Texto introdutório claro e objetivo, contextualizando o problema da empresa.",
    agent=editor_intro,
    context=[pesquisa_task]
)

# METODOLOGIA — núcleo estratégico do relatório
metodo_task = Task(
    description=dedent(f"""
        Elabore a seção de metodologia do relatório para o projeto da empresa {projeto['empresa']} ({projeto['setor']}), com objetivo de {projeto['objetivo']} em até {projeto['prazo_meses']} meses.

        Essa seção é o núcleo central do relatório e deve conter:

        1. Etapas do projeto, ordenadas cronologicamente e com descrição funcional.
        2. Perfis dos profissionais envolvidos (ex: analistas, cientistas de dados, engenheiros de ML, gerente de projeto).
        3. Ferramentas e tecnologias a serem utilizadas (ex: Power BI, AWS, GPTs, APIs de atendimento).
        4. Indicadores de sucesso (como será medido o progresso e o impacto).
        5. Cronograma macro com estimativas por fase.
        6. Riscos e estratégias de mitigação.

        Formato sugerido: {metodo_cfg['formato_sugerido']}
        Tom: {metodo_cfg['tom']}

        Instruções adicionais:
        - Seja direto, técnico e bem estruturado.
        - Utilize listas, tabelas e subtítulos quando necessário.
        - Evite redundância e valorize clareza.

        Essa seção deve ocupar a maior parte do relatório final, com profundidade estratégica.
    """),
    expected_output="Seção robusta de metodologia com etapas, perfis, ferramentas e planejamento.",
    agent=editor_metodo,
    context=[pesquisa_task]
)

pontos_fortes_trecho = ""
if conclusao_cfg.get("incluir_pontos_fortes", False):
    pontos_fortes_trecho = dedent("""
        Além disso, destaque os pontos fortes do projeto:

        - Alinhamento estratégico com objetivos da empresa;
        - Clareza nas etapas e responsabilidade dos envolvidos;
        - Escolha apropriada de tecnologias e ferramentas;
        - Potencial de escalabilidade e impacto operacional.

        Esses pontos devem ser apresentados como fortalezas que reforçam a viabilidade e o diferencial competitivo do projeto.
    """)

# CONCLUSÃO — fechamento estratégico e recomendações
conclusao_task = Task(
    description=dedent(f"""
        Com base nas seções anteriores (introdução e metodologia), redija a conclusão do relatório para o projeto da empresa {projeto['empresa']}.

        Reforce:
        - Os principais desafios enfrentados no cenário atual.
        - A aderência da metodologia proposta às necessidades da empresa.
        - Como as ferramentas e estratégias abordadas podem gerar os resultados esperados.

        Recomende:
        - Ações complementares ou fases futuras do projeto.
        - Possíveis indicadores de sucesso a serem acompanhados.
        - Cuidados estratégicos durante a implementação.

        Evite:
        - Repetir frases da introdução ou metodologia.
        - Linguagem genérica ou promessas não sustentadas.

        Tom: {conclusao_cfg['tom']}

        {pontos_fortes_trecho}

        Essa seção deve encerrar o relatório com firmeza e visão de continuidade.
    """),
    expected_output="Texto conclusivo com visão estratégica e recomendações práticas para próximos passos.",
    agent=editor_conclusao,
    context=[intro_task, metodo_task]
)
