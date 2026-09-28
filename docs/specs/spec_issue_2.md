# Especificação da issue 2 — incorporação das correções propostas pelo Lucimar

## 1. Objetivo

Incorporar às fontes versionáveis do projeto as correções apresentadas por Lucimar Oliveira do Nascimento em 27 de setembro de 2026, preservando a arquitetura de geração criada na issue 1.

Os anexos da issue são referências de conteúdo. Os arquivos finais continuam sendo produzidos pelo build a partir do notebook-fonte, CSVs, Markdown e template institucional.

## 2. Decisões

### 2.1 Variável alvo

O alvo principal permanece o atraso na partida, representado por `codigo_faixa_atraso` e `faixa_atraso_partida`.

O atraso na chegada é uma pergunta de pesquisa distinta e poderá ser avaliado posteriormente. Ele não será misturado ao alvo principal da Avaliação 1.

### 2.2 Momento da previsão

A etapa futura de modelagem deverá considerar apenas informações disponíveis antes da partida prevista. Horários reais, situação final, atrasos observados e representações do alvo não podem integrar a matriz de preditores.

### 2.3 Base consolidada

O arquivo entregue contém 25 colunas e reúne campos provenientes da fonte com campos adicionados na consolidação. Por isso, será descrito como base consolidada, e não como arquivo bruto mensal da ANAC.

### 2.4 Nomes finais

Os entregáveis usarão o nome completo da representante:

- `lucimar_oliveira_do_nascimento.ipynb`;
- `dicionario_lucimar_oliveira_do_nascimento.xlsx`;
- `base_lucimar_oliveira_do_nascimento.zip`;
- `relatorio_parcial_lucimar_oliveira_do_nascimento.docx`.

## 3. Notebook

O notebook deve:

- aceitar deterministicamente a base oficial em CSV ou ZIP;
- rejeitar ausência, ambiguidade ou esquema inesperado;
- validar as 25 colunas da base consolidada;
- preservar identificadores como texto;
- mapear explicitamente `companhia_icao`, `origem_icao` e `destino_icao`;
- criar `sg_empresa_icao`, `sg_icao_origem`, `sg_icao_destino` e `rota`;
- contabilizar ausências, duplicidades e cada motivo de exclusão;
- restringir o recorte analítico a partidas previstas em 2024 e 2025;
- comparar o atraso recalculado com `atraso_partida_min`;
- sinalizar antecipações superiores a 60 minutos e atrasos superiores a 24 horas;
- manter extremos até existir justificativa documentada para tratamento;
- apresentar denominadores nas análises por hora e companhia;
- falhar explicitamente quando não houver dados necessários a um gráfico;
- evitar afirmações causais com base em associações descritivas;
- permanecer versionado sem outputs e sem contagens de execução.

## 4. Dicionário

As fontes CSV devem gerar duas abas:

- `Base consolidada`, com as 25 colunas exatas da entrada;
- `Variáveis analíticas`, com 20 variáveis, incluindo `codigo_faixa_atraso`.

Cada linha deve documentar, quando aplicável:

- origem ou regra de derivação;
- tratamento de ausentes;
- disponibilidade pré ou pós-voo;
- risco de vazamento de dados;
- uso como alvo, preditor candidato ou campo de auditoria;
- natureza analítica dos limites das faixas.

## 5. Relatório

O relatório deve:

- formular uma pergunta de pesquisa objetiva;
- identificar a unidade observacional;
- explicar que a entrada é consolidada;
- registrar a presença de ligações internacionais;
- distinguir atraso na partida de atraso na chegada;
- afirmar que as faixas são escolhas analíticas do estudo;
- separar análise exploratória de avaliação preditiva;
- evitar inferências causais e regulatórias não demonstradas;
- documentar limitações e extremos;
- usar cinco trabalhos acadêmicos, além da fonte institucional da ANAC;
- remover ou corrigir referências com autoria incorreta.

Segundo os metadados oficiais do VRA, horários previstos e realizados são publicados em horário de Brasília. A consolidação ainda deve ser auditada, mas o relatório não deve afirmar que a fonte oficial usa horários locais desconhecidos.

## 6. Build e validação

O comando permanece:

```bash
python scripts/build_avaliacao_01.py
```

O build deve produzir os quatro entregáveis com o nome completo da representante, limpar o notebook e validar:

- contagem de 25 e 20 variáveis no dicionário;
- presença das duas abas e tabelas estruturadas;
- seções obrigatórias do relatório;
- ausência de outputs no notebook;
- estrutura do ZIP;
- presença e tamanho dos quatro arquivos finais.

## 7. Critérios de aceitação

1. O notebook contém o mapeamento exato das colunas que causavam os gráficos vazios.
2. O notebook-fonte e o notebook gerado estão sem outputs.
3. O dicionário contém 25 variáveis da base e 20 variáveis analíticas.
4. `codigo_faixa_atraso` está documentado.
5. O relatório mantém o atraso na partida como desfecho e usa linguagem metodologicamente cautelosa.
6. Os nomes dos quatro entregáveis contêm `lucimar_oliveira_do_nascimento`.
7. O build pode ser executado fora da raiz do repositório.
8. Testes automatizados e validações estruturais passam.
9. Todas as páginas do DOCX e as duas abas do XLSX são revisadas visualmente.

## 8. Fora do escopo

- trocar o alvo principal para atraso na chegada;
- treinar modelos da Avaliação 2;
- decidir tratamento definitivo dos extremos antes da auditoria;
- atribuir causas meteorológicas, operacionais ou regulatórias aos padrões observados;
- aceitar automaticamente qualquer CSV encontrado no diretório de execução.
