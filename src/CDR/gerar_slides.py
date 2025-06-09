# gerar_slides.py

import os
from datetime import datetime
from crewai import Task
from agents.level_6_slides import gerador_slides
from contexto.context_loader import carregar_contexto
from textwrap import dedent

# Carregar contexto do .yml
ctx = carregar_contexto()
projeto = ctx['projeto']
publico = ctx['publico_alvo']
# slides_cfg = ctx['slides']

def carregar_md_caminho():
    arquivos_md = [f for f in os.listdir() if f.startswith("relatorio_final_") and f.endswith(".md")]
    if not arquivos_md:
        raise FileNotFoundError("Nenhum relatório final encontrado no diretório atual.")
    arquivos_md.sort(reverse=True)  # pega o mais recente
    return arquivos_md[0]

if __name__ == "__main__":
    caminho_md = carregar_md_caminho()
    print(f"📄 Carregando relatório: {caminho_md}")

    with open(caminho_md, "r", encoding="utf-8") as f:
        relatorio_md = f.read()

    # Criar uma nova task passando o input diretamente
    slide_task = Task(
    description = dedent(f"""
    Você receberá o conteúdo de um relatório técnico abaixo. Sua missão é transformá-lo em **6 blocos de conteúdo** formatados em **Markdown**, prontos para serem usados em **slides executivos**. Cada bloco corresponde a **um slide**, seguindo a estrutura abaixo.

    ### Tópicos esperados (um por slide):
    1. **Escopo Funcional do Projeto**
    - O projeto contempla a disponibilização de times ageis, equipes de sustentação e desenvolvimento e equipes de atendimento, dedicados ao desenvolvimento evolução, sustentação e operações programadas das soluções. 
    - Dizer as incubencias de cada time e os perfis envolvidos no em cada time:
        - O time Agil faz as tarefas de ...... e possui os seguintes perfis .
        - A equipe de sustentação faz as tarefas de ...... e possui os seguintes perfis .
        - A equipe de atendimento faz as tarefas de ...... e possui os seguintes perfis .
    2. **Ciclo de Vida do Projeto**  
    - Liste as **fases principais com duração e entregáveis** em tabela  
    - Em seguida, crie uma **matriz RACI completa**:
        - Atividades nas linhas (ex: Definição de Backlog, Execução de estórias, Validação Funcional, Planejamento do sprint e implantação/homologação)
        - Perfis nos cabeçalhos das colunas (ex: {projeto['empresa']}, Capco (empresa), Agile Master, Product Owner e Lídert Técnico.)
        - Utilize letras R, A, C, I conforme convenção
        - Inclua uma legenda clara abaixo da tabela
    3. **Perfis do Time**  
    - Use uma tabela listando função, responsabilidades e headcounting
    4. **Governança do Time**  
    - Segementação do time em três níveis: Estratégico, Tático e Operacional, inclua uma breve descrição do que é cada nível desse.
    5. **Riscos e Estratégias de Mitigação**  
    - Use uma tabela com colunas: Risco | Estratégia de Mitigação
    6. **Riscos Legais e Penalizações**  
    - Riscos associados á penalização contratual
    - Liste estratégias de Mitigação Correlacionadas

    ### Diretrizes de Estilo:
    - Use Markdown com `### Título do Slide`, bullets (`-`), tabelas (`| coluna |`) e **negrito**
    - **Máximo de 20 linhas** de conteúdo real por tópico/slide
    - Linguagem de **comunicação executiva**: clara, estratégica, concisa
    - Estruture a informação com lógica e hierarquia visual (ex: subtópicos, bullets)
    - **Não resuma excessivamente**; destaque o que é relevante para decisões

    ### Público-alvo:
    - Linguagem: {publico['linguagem']}
    - Foco: {publico['foco']}
    - Perfil: {publico['perfil']}

    --- INÍCIO DO RELATÓRIO ---

    {relatorio_md}

    --- FIM DO RELATÓRIO ---
    """),
    expected_output="Blocos de conteúdo formatados em Markdown para os 6 slides da apresentação.",
    agent=gerador_slides
)


    resultado = gerador_slides.execute_task(slide_task)

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    nome_saida = f"slides_base_{timestamp}.md"

    with open(nome_saida, "w", encoding="utf-8") as f:
        f.write(str(resultado))

    print(f"✅ Slides gerados e salvos em: {nome_saida}")
