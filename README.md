# 🛰️ Mission Control AI — Sentinela Orbital

**FIAP · GS2026.1 · Pensamento Computacional e Automação com Python**

Sistema em **Python puro** que simula o monitoramento inteligente de uma missão
espacial experimental por **ciclos**. Para cada ciclo, o sistema analisa cinco
parâmetros, classifica o risco por regras lógicas, identifica a tendência da
missão e a área mais afetada, e exibe um **relatório final** no terminal.

> A "inteligência" do sistema é baseada em **regras lógicas** (sem machine
> learning e sem bibliotecas externas), conforme proposto na atividade.

## 👥 Integrantes

- Herbert Soares — RM: 571507
- Guilherme Garbelini — RM: 571150
- Gabriel de Almeida Santos — RM: 569395

## 🚀 O que o sistema faz

- Armazena dados simulados em uma **matriz `dados_missao`** (6 ciclos × 5 parâmetros)
- Classifica cada parâmetro em `NORMAL`, `ATENÇÃO` ou `CRÍTICO`
- Calcula a **pontuação de risco** de cada ciclo (0 a 10)
- Classifica o ciclo: `MISSÃO ESTÁVEL` / `EM ATENÇÃO` / `CRÍTICA`
- Gera **recomendações automáticas** por ciclo
- Analisa a **tendência** da missão (comparando o 1º e o último ciclo)
- Identifica a **área mais afetada** ao longo de toda a missão
- Exibe um **relatório final** completo no terminal

## 📊 Estrutura da matriz `dados_missao`

Cada linha é um ciclo; cada coluna, um parâmetro, nesta ordem:

| Posição | Parâmetro | Unidade |
|--------|-----------|---------|
| 0 | Temperatura | °C |
| 1 | Comunicação | % |
| 2 | Bateria | % |
| 3 | Oxigênio | % |
| 4 | Estabilidade | % |

## 🚦 Regras de alerta (limites adotados)

| Parâmetro | NORMAL | ATENÇÃO | CRÍTICO |
|-----------|--------|---------|---------|
| Temperatura | 18 a 30 °C | <18 °C ou 31–35 °C | >35 °C |
| Comunicação | ≥60% | 30–59% | <30% |
| Bateria | ≥50% | 20–49% | <20% |
| Oxigênio | ≥90% | 80–89% | <80% |
| Estabilidade | ≥70% | 40–69% | <40% |

**Pontuação de risco:** `NORMAL = 0`, `ATENÇÃO = 1`, `CRÍTICO = 2`
(máximo de 10 por ciclo).

**Classificação do ciclo:** `0–2 = ESTÁVEL`, `3–5 = EM ATENÇÃO`, `6–10 = CRÍTICA`.

## 🧩 Funções principais

`analisar_temperatura`, `analisar_comunicacao`, `analisar_bateria`,
`analisar_oxigenio`, `analisar_estabilidade`, `analisar_ciclo`,
`classificar_ciclo`, `gerar_recomendacao`, `analisar_tendencia`,
`identificar_area_mais_afetada`, `calcular_medias`, `gerar_relatorio_final`.

## ▶️ Como executar

Não precisa instalar nada (Python puro):

```bash
python mission_control.py
```

## 🎥 Vídeo Pitch

[Assistir ao vídeo](https://youtu.be/M2Q0IYTf3KM)
