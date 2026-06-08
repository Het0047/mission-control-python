# =====================================================================
#  MISSION CONTROL AI  —  Sistema Inteligente de Monitoramento Espacial
#  GS2026.1 — Pensamento Computacional e Automacao com Python (FIAP)
#
#  Sistema em Python puro (sem bibliotecas externas) que simula o
#  monitoramento de uma missao espacial por ciclos, aplicando regras
#  logicas para classificar risco, identificar tendencia e a area mais
#  afetada, e exibir um relatorio final no terminal.
# =====================================================================

# ----- Identificacao da missao e da equipe -----
NOME_MISSAO = "Sentinela Orbital"
NOME_EQUIPE = "Vanguarda Espacial"

# ----- Estrutura principal: matriz dados_missao -----
# Cada LINHA = um ciclo da missao.
# Cada COLUNA, nesta ordem: [temperatura, comunicacao, bateria, oxigenio, estabilidade]
dados_missao = [
    [22, 95, 91, 97, 93],   # Ciclo 1 - inicio da missao
    [26, 78, 68, 93, 82],   # Ciclo 2 - estabilizacao dos sistemas
    [29, 48, 55, 90, 72],   # Ciclo 3 - queda parcial de comunicacao
    [33, 40, 22, 88, 64],   # Ciclo 4 - alerta de energia
    [41, 25, 14, 76, 33],   # Ciclo 5 - risco operacional
    [31, 58, 36, 84, 61],   # Ciclo 6 - tentativa de recuperacao
]

# ----- Lista de areas monitoradas (relacionada as colunas) -----
areas_monitoradas = [
    "Temperatura interna",      # coluna 0
    "Comunicacao com a base",   # coluna 1
    "Sistema de energia",       # coluna 2
    "Suporte de oxigenio",      # coluna 3
    "Estabilidade operacional", # coluna 4
]

# Pontuacao por classificacao
PONTOS = {"NORMAL": 0, "ATENCAO": 1, "CRITICO": 2}


# =====================================================================
#  FUNCOES DE ANALISE POR PARAMETRO
#  Cada funcao recebe um valor e devolve (classificacao, mensagem).
# =====================================================================
def analisar_temperatura(valor):
    if valor > 35:
        return "CRITICO", "Risco de superaquecimento"
    if valor > 30 or valor < 18:
        return "ATENCAO", "Temperatura fora do ideal"
    return "NORMAL", "Temperatura estavel"


def analisar_comunicacao(valor):
    if valor < 30:
        return "CRITICO", "Sinal com a base em nivel critico"
    if valor < 60:
        return "ATENCAO", "Comunicacao instavel"
    return "NORMAL", "Comunicacao estavel"


def analisar_bateria(valor):
    if valor < 20:
        return "CRITICO", "Bateria em nivel critico"
    if valor < 50:
        return "ATENCAO", "Bateria abaixo do recomendado"
    return "NORMAL", "Energia estavel"


def analisar_oxigenio(valor):
    if valor < 80:
        return "CRITICO", "Oxigenio em nivel critico"
    if valor < 90:
        return "ATENCAO", "Oxigenio abaixo do ideal"
    return "NORMAL", "Oxigenio adequado"


def analisar_estabilidade(valor):
    if valor < 40:
        return "CRITICO", "Estabilidade operacional critica"
    if valor < 70:
        return "ATENCAO", "Estabilidade operacional reduzida"
    return "NORMAL", "Estabilidade operacional adequada"


# Ordem das funcoes alinhada as colunas da matriz
ANALISADORES = [
    analisar_temperatura,
    analisar_comunicacao,
    analisar_bateria,
    analisar_oxigenio,
    analisar_estabilidade,
]
ROTULOS = ["Temperatura", "Comunicacao", "Bateria", "Oxigenio", "Estabilidade"]
UNIDADES = ["C", "%", "%", "%", "%"]


# =====================================================================
#  ANALISE DE UM CICLO COMPLETO
# =====================================================================
def analisar_ciclo(ciclo):
    """Recebe uma linha da matriz e devolve a analise completa do ciclo."""
    resultado = {"itens": [], "pontuacao_total": 0, "pontos_por_area": []}
    for i, valor in enumerate(ciclo):
        classificacao, mensagem = ANALISADORES[i](valor)
        pontos = PONTOS[classificacao]
        resultado["itens"].append({
            "rotulo": ROTULOS[i],
            "unidade": UNIDADES[i],
            "valor": valor,
            "classificacao": classificacao,
            "mensagem": mensagem,
            "pontos": pontos,
        })
        resultado["pontuacao_total"] += pontos
        resultado["pontos_por_area"].append(pontos)
    return resultado


def classificar_ciclo(pontuacao_total):
    """Classifica o ciclo de acordo com a pontuacao de risco (0 a 10)."""
    if pontuacao_total <= 2:
        return "MISSAO ESTAVEL"
    if pontuacao_total <= 5:
        return "MISSAO EM ATENCAO"
    return "MISSAO CRITICA"


def gerar_recomendacao(analise):
    """Gera uma recomendacao automatica com base nos itens do ciclo."""
    criticos = [it["rotulo"] for it in analise["itens"] if it["classificacao"] == "CRITICO"]
    atencoes = [it["rotulo"] for it in analise["itens"] if it["classificacao"] == "ATENCAO"]

    mapa_critico = {
        "Temperatura": "verificar o controle termico da missao",
        "Comunicacao": "tentar restabelecer contato com a base",
        "Bateria": "ativar o modo de economia de energia",
        "Oxigenio": "acionar o protocolo de suporte a vida",
        "Estabilidade": "reduzir operacoes nao essenciais",
    }

    if len(criticos) >= 2:
        return "Ativar modo de seguranca e priorizar suporte a vida, energia e comunicacao."
    if len(criticos) == 1:
        return "Acao critica: " + mapa_critico[criticos[0]] + "."
    if atencoes:
        return "Monitorar sistemas em atencao e preparar plano de contingencia."
    return "Manter operacao normal e continuar o monitoramento."


# =====================================================================
#  ANALISES GLOBAIS DA MISSAO
# =====================================================================
def analisar_tendencia(risco_primeiro, risco_ultimo):
    """Compara o risco do primeiro e do ultimo ciclo."""
    if risco_ultimo > risco_primeiro:
        return "A missao apresentou tendencia de PIORA."
    if risco_ultimo < risco_primeiro:
        return "A missao apresentou tendencia de MELHORA."
    return "A missao permaneceu ESTAVEL em relacao ao inicio."


def identificar_area_mais_afetada(analises):
    """Soma a pontuacao de risco de cada area ao longo de todos os ciclos."""
    totais = [0] * len(areas_monitoradas)
    for analise in analises:
        for i, pontos in enumerate(analise["pontos_por_area"]):
            totais[i] += pontos
    indice_max = totais.index(max(totais))
    return areas_monitoradas[indice_max], totais


def calcular_medias():
    """Calcula a media de cada parametro ao longo de todos os ciclos."""
    n = len(dados_missao)
    medias = []
    for coluna in range(5):
        soma = sum(linha[coluna] for linha in dados_missao)
        medias.append(soma / n)
    return medias


# =====================================================================
#  EXIBICAO
# =====================================================================
def exibir_cabecalho():
    print("=" * 60)
    print("MISSION CONTROL AI")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}")
    print("=" * 60)


def exibir_ciclo(numero, analise):
    print(f"\nCICLO {numero}")
    print("-" * 60)
    for it in analise["itens"]:
        print(f"{it['rotulo']}: {it['valor']}{it['unidade']} | "
              f"{it['classificacao']} | {it['mensagem']}")
    print(f"\nPontuacao de risco do ciclo: {analise['pontuacao_total']}")
    print(f"Classificacao do ciclo: {classificar_ciclo(analise['pontuacao_total'])}")
    print(f"Recomendacao: {gerar_recomendacao(analise)}")


def gerar_relatorio_final(analises):
    riscos = [a["pontuacao_total"] for a in analises]
    medias = calcular_medias()
    area_critica, totais_area = identificar_area_mais_afetada(analises)
    ciclo_mais_critico = riscos.index(max(riscos)) + 1
    risco_medio = sum(riscos) / len(riscos)
    qtd_ciclos_criticos = sum(1 for r in riscos if classificar_ciclo(r) == "MISSAO CRITICA")

    print("\n" + "=" * 60)
    print("RELATORIO FINAL DA MISSAO")
    print("=" * 60)
    print(f"Missao: {NOME_MISSAO}")
    print(f"Equipe: {NOME_EQUIPE}")
    print(f"Quantidade de ciclos analisados: {len(dados_missao)}\n")

    print(f"Media de temperatura: {medias[0]:.2f} C")
    print(f"Media de comunicacao: {medias[1]:.2f}%")
    print(f"Media de bateria: {medias[2]:.2f}%")
    print(f"Media de oxigenio: {medias[3]:.2f}%")
    print(f"Media de estabilidade: {medias[4]:.2f}%\n")

    print(f"Ciclo mais critico: Ciclo {ciclo_mais_critico}")
    print(f"Maior pontuacao de risco: {max(riscos)}")
    print(f"Risco medio da missao: {risco_medio:.2f}")
    print(f"Quantidade de ciclos criticos: {qtd_ciclos_criticos}\n")

    print("Tendencia da missao:")
    print(analisar_tendencia(riscos[0], riscos[-1]) + "\n")

    print("Pontuacao acumulada por area:")
    for nome, pontos in zip(areas_monitoradas, totais_area):
        print(f"{nome}: {pontos} pontos")

    print(f"\nArea mais afetada:\n{area_critica}\n")

    print("Classificacao final da missao:")
    print(classificar_ciclo(round(risco_medio)) + "\n")

    print("Conclusao:")
    print("A missao passou por instabilidade relevante, com pico de risco no "
          f"ciclo {ciclo_mais_critico}. A area de '{area_critica}' foi a mais "
          "exigida. A equipe deve manter o plano de contingencia ativo ate a "
          "normalizacao completa dos sistemas.")
    print("=" * 60)


# =====================================================================
#  PROGRAMA PRINCIPAL
# =====================================================================
def main():
    exibir_cabecalho()
    analises = []
    for numero, ciclo in enumerate(dados_missao, start=1):
        analise = analisar_ciclo(ciclo)
        analises.append(analise)
        exibir_ciclo(numero, analise)
    gerar_relatorio_final(analises)


if __name__ == "__main__":
    main()
