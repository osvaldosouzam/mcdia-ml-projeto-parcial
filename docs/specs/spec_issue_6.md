# Especificação da issue 6 — revisão didática e aprofundamento da Avaliação 1

## 1. Objetivo

Concluir a adequação acadêmica e didática da Avaliação 1 sobre a infraestrutura e as correções já integradas pelos PRs #3 e #5.

Esta issue deve melhorar principalmente o notebook exploratório, tornando cada etapa compreensível, auditável e sustentada por evidências. Também deve manter coerentes o README, o dicionário, o relatório e o pacote final quando as novas análises alterarem terminologia, totais ou conclusões.

O resultado deve continuar sendo uma entrega autocontida, reproduzível e executável sem dependência do repositório de prova de conceito `mcdia-ml-previsao-atraso-voos`.

Não faz parte desta issue refazer a arquitetura de build nem reabrir decisões já consolidadas sem evidência de defeito.

## 2. Contexto atualizado

O projeto entrega, para a Avaliação 1:

1. notebook Python no formato `.ipynb`;
2. dicionário de dados em Excel;
3. base consolidada em CSV, empacotada em ZIP;
4. relatório parcial em Word.

Os PRs #3 e #5, integrados em `main`, estabeleceram uma arquitetura reproduzível e incorporaram as correções sugeridas por Lucimar Oliveira do Nascimento. A issue #6 parte desse estado e não do esboço original do repositório.

A modelagem, a divisão definitiva em treino, validação e teste, o ajuste de hiperparâmetros e a avaliação de modelos pertencem à Avaliação 2. Nesta issue, referências à etapa preditiva devem aparecer apenas como implicações ou encaminhamentos.

## 3. Baseline já implementado

Os itens desta seção são premissas a preservar. Eles só devem ser alterados se a implementação da issue #6 revelar um problema verificável.

### 3.1 Estrutura e build

Já existem:

- fontes versionáveis do relatório em Markdown;
- fontes versionáveis do dicionário em CSV;
- template institucional separado em `templates/relatorio_institucional.docx`;
- biblioteca comum em `scripts/build_common/`;
- build da Avaliação 1 em `scripts/build_avaliacao_01.py`;
- contrato explícito para a Avaliação 2 em `scripts/build_avaliacao_02.py`;
- validação em `scripts/validate_all.py`;
- testes automatizados em `tests/`;
- saídas separadas por avaliação dentro de `target/`;
- `requirements.txt` e instruções de ambiente no README;
- `.gitignore` para ambientes, caches, IDEs, checkpoints e outputs gerados.

O build da Avaliação 1 já pode ser executado fora da raiz do repositório porque resolve caminhos com base na localização dos scripts.

### 3.2 Nomes atuais dos entregáveis

Os nomes padronizados usam o nome completo da representante:

```text
target/avaliacao_01/
├── lucimar_oliveira_do_nascimento.ipynb
├── dicionario_lucimar_oliveira_do_nascimento.xlsx
├── base_lucimar_oliveira_do_nascimento.zip
└── relatorio_parcial_lucimar_oliveira_do_nascimento.docx
```

Não voltar aos nomes abreviados `lucimar_nascimento*`, a nomes com espaços nem ao sufixo de entrega `_v2` nos artefatos finais.

O nome interno legado `base_lucimar_nascimento_v2.csv` pode permanecer dentro do ZIP enquanto corresponder ao arquivo oficial consolidado. O notebook e o empacotamento devem tratar esse nome explicitamente.

### 3.3 Leitura e esquema da base

O notebook atual:

- aceita os nomes oficiais de CSV e ZIP ao lado do notebook;
- aceita a base de desenvolvimento em `data/raw/`;
- dá prioridade ao arquivo colocado ao lado do notebook;
- rejeita mais de uma base no mesmo nível de prioridade;
- lê ZIP diretamente, sem exigir extração permanente;
- valida exatamente as 25 colunas da base consolidada;
- preserva identificadores como texto;
- interrompe a execução quando o esquema é incompatível.

O mapeamento atual já contempla:

- `companhia_icao` → `sg_empresa_icao`;
- `numero_voo` → `nr_voo`;
- `origem_icao` → `sg_icao_origem`;
- `destino_icao` → `sg_icao_destino`;
- `partida_prevista` → `dt_partida_prevista`;
- `partida_real` → `dt_partida_real`;
- `chegada_prevista` → `dt_chegada_prevista`;
- `chegada_real` → `dt_chegada_real`;
- `situacao_voo` → `cd_situacao_voo`;
- `atraso_partida_min` → `atraso_partida_min` na cópia padronizada, usada para auditoria;
- criação de `rota` a partir dos aeroportos de origem e destino.

O problema anterior de gráficos vazios por divergência entre nomes da base e nomes analíticos foi corrigido.

### 3.4 Dicionário

O dicionário atual é gerado a partir de:

```text
sources/dicionario/base_consolidada.csv
sources/dicionario/variaveis_analiticas.csv
```

Ele possui:

- aba `Base consolidada`, com as 25 colunas exatas do CSV;
- aba `Variáveis analíticas`, com 20 variáveis selecionadas ou derivadas;
- documentação de `codigo_faixa_atraso`;
- origem, significado, domínio e restrição de uso futuro;
- autofiltro, congelamento da primeira linha, quebra de texto e formatação legível.

O termo `base consolidada` é intencional. A base entregue já reúne dados de origem e campos produzidos na consolidação e não deve ser chamada de arquivo mensal bruto e intocado da ANAC.

### 3.5 Relatório

O relatório atual:

- é gerado a partir de Markdown e do template institucional;
- contém introdução, objetivos, referencial teórico e referências;
- mantém coerência com o atraso na partida como desfecho;
- diferencia a Avaliação 1 da modelagem futura;
- cita a fonte oficial VRA/ANAC;
- evita atribuições causais não sustentadas;
- usa referências metodológicas e acadêmicas coerentes;
- não contém a atribuição incorreta entre Kalliguddi, Leboulluec e o artigo da PLOS ONE;
- renderiza atualmente em quatro páginas, sem cortes ou sobreposições relevantes;
- usa alinhamento à esquerda nas referências para evitar grandes espaços causados por URLs longas.

Não reintroduzir na bibliografia referências removidas apenas para cumprir uma contagem. Qualquer nova referência deve ter função explícita no texto e metadados conferidos.

### 3.6 Notebook limpo e execução validada

O notebook-fonte e a cópia de entrega estão sem outputs persistidos e com `execution_count` nulo. O build também valida ausência de caminhos locais absolutos.

Na implementação do PR #5, o notebook foi executado integralmente com a base completa, inclusive a partir do pacote final, sem erros. Essa validação deve ser repetida depois das alterações da issue #6.

## 4. Diagnóstico atual após os merges

### 4.1 Organização ainda insuficiente

O notebook atual possui 13 células:

- 5 células de Markdown;
- 8 células de código.

Embora tenha sido reduzido e corrigido, ainda há células de código com 63, 82 e 105 linhas. Algumas combinam responsabilidades distintas, como conversão temporal, seleção da população, criação do alvo, engenharia de variáveis, auditoria de extremos e definição de preditores futuros.

Também permanecem:

- banners com linhas de `=`;
- comentários como `CÉLULA 8` e `CÉLULA 10`;
- explicações concentradas em poucos blocos longos;
- poucas células de interpretação após tabelas e gráficos;
- seções numeradas de forma pouco granular.

### 4.2 Auditoria de qualidade parcial

O notebook já apresenta:

- dimensões e nomes das colunas;
- quantidade e percentual de ausentes na entrada;
- repetição de `arquivo_origem + linha_origem`;
- falhas de conversão das quatro colunas temporais;
- frequências de situação do voo;
- contagem das exclusões e retenções;
- comparação entre atraso fornecido e recalculado;
- amostra rastreável de antecipações superiores a 60 minutos ou atrasos superiores a 24 horas;
- cardinalidade de companhia, origem, destino e rota.

Ainda faltam ou precisam ser explicitados:

- perfil de tipos antes e depois das conversões;
- duplicidades exatas;
- investigação de duplicidades por chave natural documentada;
- validação de domínios das variáveis categóricas e booleanas;
- reconciliação automática das categorias de exclusão;
- auditorias temporais em faixas separadas, em vez de um único indicador amplo;
- quantificação de duração planejada negativa ou implausível;
- tabela específica das divergências entre atraso fornecido e recalculado;
- distinção entre ausência original e falha de conversão em todos os campos relevantes.

### 4.3 Cobertura exploratória parcial

O notebook já contém:

- estatísticas detalhadas do atraso na partida;
- distribuição das seis faixas;
- distribuição do alvo binário;
- histograma e boxplot com recorte exclusivamente visual;
- taxa de atraso por hora prevista;
- comparação das cinco companhias com maior volume;
- discussão preliminar cautelosa.

Ainda faltam, conforme a pertinência e a qualidade dos dados:

- evolução mensal;
- análise por aeroportos de origem e destino;
- análise por rotas de volume suficiente;
- frequências resumidas de variáveis categóricas relevantes;
- estatísticas de outras variáveis numéricas válidas;
- interpretação curta imediatamente após cada conjunto importante de resultados;
- denominadores mínimos ou filtros de volume para comparações entre grupos.

### 4.4 Validação das regras do alvo

As faixas estão implementadas e o alvo binário deriva do atraso contínuo, mas não há testes explícitos de fronteira para todos os limites. A função usa `np.select` e deve ser validada contra valores abaixo, acima e exatamente nos pontos de corte.

### 4.5 Reprodutibilidade operacional ainda não documentada

O README documenta ambiente, build, validação e política de outputs, mas ainda não registra:

- versão de Python efetivamente usada na validação final;
- tempo observado para execução integral do notebook;
- pico aproximado de memória ou estimativa operacional;
- comando automatizado ou procedimento exato usado para a execução integral sem persistir outputs na entrega.

## 5. Escopo da implementação

### RF-01 — Preservar a leitura determinística

A implementação deve manter o mecanismo atual de prioridade:

1. base oficial colocada ao lado do notebook;
2. base de desenvolvimento em `data/raw/`.

Dentro de cada nível, mais de um candidato deve causar erro informativo. A ausência de todos os candidatos também deve causar erro objetivo.

O notebook deve imprimir o caminho escolhido. Quando a entrada for ZIP, deve registrar também o nome do CSV interno validado.

Não escolher arbitrariamente o primeiro CSV de um diretório e não exigir extração manual.

### RF-02 — Dividir o notebook por responsabilidade

Cada célula de código deve ter uma responsabilidade predominante. A estrutura deve separar, no mínimo:

1. imports e estilo visual;
2. configuração dos caminhos aceitos;
3. leitura do CSV ou ZIP;
4. validação do esquema de entrada;
5. perfil inicial da base consolidada;
6. mapeamento para nomes analíticos;
7. conversão de tipos;
8. auditoria de ausências e domínios;
9. auditoria de duplicidades;
10. auditoria temporal;
11. definição e reconciliação da população elegível;
12. construção e testes do alvo;
13. criação das variáveis analíticas;
14. estatísticas descritivas;
15. distribuição dos alvos;
16. visualizações temporais;
17. visualizações por companhia, aeroporto e rota;
18. discussão e conclusão da Avaliação 1.

Funções auxiliares podem concentrar lógica reutilizável, mas uma única célula não deve misturar leitura, limpeza, criação do alvo e visualização.

### RF-03 — Melhorar a narrativa didática

Antes de cada operação relevante, uma célula de Markdown deve explicar:

- o objetivo;
- a motivação;
- a entrada utilizada;
- o resultado esperado;
- o cuidado necessário para interpretar o output.

Após cada tabela ou gráfico importante, incluir uma interpretação curta que diferencie:

- evidência observada;
- hipótese explicativa;
- decisão metodológica;
- limitação ainda não resolvida.

Remover:

- banners de comentários com linhas de `=`;
- referências a números de células;
- comentários que apenas repetem literalmente o código;
- células vazias;
- código morto e imports não utilizados;
- supressão global de avisos;
- captura genérica de exceções sem reemissão.

### RF-04 — Preservar e nomear os estágios dos dados

Manter objetos distintos e claramente nomeados para:

- base consolidada carregada, sem transformações destrutivas;
- base com nomes padronizados;
- base com tipos convertidos e flags de auditoria;
- população elegível para o alvo;
- base analítica usada nas estatísticas e gráficos.

Evitar cópias completas desnecessárias, mas não sacrificar a capacidade de auditar a entrada.

Cada transição deve informar:

- quantidade anterior;
- quantidade retida;
- quantidade excluída;
- percentual excluído;
- motivo da exclusão.

As categorias devem ser mutuamente exclusivas ou a eventual sobreposição deve ser explicada.

### RF-05 — Completar o perfil inicial

Antes da seleção da população, apresentar:

- dimensões;
- nomes das colunas;
- tipos inferidos;
- ausentes em quantidade e percentual;
- duplicidades exatas;
- repetições de `arquivo_origem + linha_origem`;
- frequências das situações operacionais;
- contagem de cancelados e realizados;
- cobertura temporal bruta, quando interpretável;
- cardinalidade das principais variáveis categóricas;
- valores inesperados em campos booleanos ou de situação.

Tabelas extensas devem ser ordenadas e formatadas para permanecer legíveis.

### RF-06 — Auditar duplicidades por chave natural

Definir e justificar uma chave natural candidata. O ponto de partida recomendado é:

```text
companhia + número do voo + origem + destino + partida prevista
```

A análise deve:

- quantificar grupos repetidos;
- diferenciar repetição legítima em datas distintas de possível duplicação;
- mostrar pequena amostra rastreável;
- não remover registros automaticamente sem justificativa;
- explicar limitações da chave escolhida.

### RF-07 — Aprofundar a auditoria temporal

Usar regra explícita compatível com o formato real `AAAA-MM-DD HH:MM:SS` e quantificar separadamente:

- valores originalmente ausentes;
- valores não ausentes que falharam na conversão;
- partidas previstas ausentes ou inválidas;
- partidas reais ausentes ou inválidas;
- voos realizados sem dados suficientes para o alvo;
- antecipações inferiores a `-1.440` minutos;
- atrasos superiores a `1.440` minutos;
- atrasos superiores a sete dias;
- durações planejadas negativas;
- durações planejadas acima de um limite operacional apenas diagnóstico e justificado;
- divergências entre `atraso_partida_min` e o atraso recalculado.

Casos extremos devem permanecer na base consolidada e aparecer em tabela de auditoria com `arquivo_origem` e `linha_origem`.

Não corrigir automaticamente viradas de dia. Os metadados oficiais indicam que os horários do VRA são publicados no horário de Brasília; isso reduz a ambiguidade de fuso, mas não elimina possíveis inconsistências de data na consolidação.

Qualquer correção futura deve ser conservadora, testável, quantificada e documentada.

### RF-08 — Reconciliar a população analisada

A população do alvo deve conter apenas voos realizados, com partida prevista e real válidas e partida prevista em 2024 ou 2025.

O notebook deve demonstrar automaticamente que:

```text
linhas de entrada = linhas retidas + linhas excluídas por categorias reconciliadas
```

Cancelamentos devem ser apresentados como desfecho operacional separado e não receber classe de atraso.

Registros problemáticos não podem desaparecer silenciosamente. Quando mais de uma condição de exclusão ocorrer na mesma linha, aplicar uma ordem de precedência explícita ou apresentar uma matriz de sobreposição.

### RF-09 — Testar as fronteiras das faixas

As regras permanecem:

- faixa 0: `x <= 0`;
- faixa 1: `0 < x < 15`;
- faixa 2: `15 <= x <= 30`;
- faixa 3: `30 < x <= 45`;
- faixa 4: `45 < x <= 60`;
- faixa 5: `x > 60`.

Adicionar asserções ou testes automatizados para:

- `-1`;
- `0`;
- menor valor positivo representável adotado no teste;
- valor imediatamente abaixo de `15`;
- `15`;
- `30`;
- valor imediatamente acima de `30`;
- `45`;
- valor imediatamente acima de `45`;
- `60`;
- valor imediatamente acima de `60`.

Validar também que:

- não há lacunas nem sobreposições;
- o rótulo textual corresponde ao código;
- `atraso_bi == 1` se e somente se `x >= 15`;
- valores ausentes não recebem classe silenciosamente.

Se a função de classificação permanecer dentro do notebook, os testes podem ser executados em uma célula pequena e visível. É preferível manter a lógica autocontida no notebook para a submissão.

### RF-10 — Delimitar preditores futuros e vazamento

Manter explícita a distinção entre variáveis pré-voo e informações pós-evento.

Devem permanecer proibidos em uma futura matriz `X` pré-partida:

- partida real;
- chegada real;
- situação final do voo;
- atrasos fornecidos ou recalculados;
- código e rótulo das faixas;
- alvo binário;
- qualquer justificativa conhecida somente depois do evento.

Variáveis candidatas devem ser apresentadas como hipóteses a validar na Avaliação 2, e não como conjunto definitivo de preditores.

### RF-11 — Completar as análises descritivas

Para o atraso na partida, manter:

- contagem;
- média;
- mediana;
- desvio-padrão;
- mínimo e máximo;
- quartis;
- intervalo interquartil;
- percentis relevantes;
- assimetria;
- curtose.

Incluir outras variáveis numéricas apenas quando sua semântica estiver clara. A duração planejada pode ser descrita depois da auditoria de valores negativos ou implausíveis, deixando explícito que se trata de diferença bruta entre timestamps previstos.

Para categóricas, apresentar frequências e proporções resumidas sem despejar domínios de alta cardinalidade integralmente.

### RF-12 — Completar a exploração gráfica

Manter os gráficos existentes e acrescentar, quando houver dados válidos:

- evolução mensal do atraso ou da proporção de atrasos;
- comparação por aeroportos de origem de maior volume;
- comparação por aeroportos de destino de maior volume, se agregar informação distinta;
- comparação por rotas de maior volume;
- visualização que deixe claro o desbalanceamento das seis classes.

Comparações por grupo devem:

- mostrar ou informar o denominador;
- adotar critério explícito de volume mínimo ou selecionar os grupos de maior volume;
- evitar ranking de grupos com amostras insuficientes;
- permanecer descritivas, sem linguagem causal.

Usar agregações para gráficos. Se uma amostra for necessária, fixar a semente e declarar seu tamanho. Evitar KDE ou operações densas desnecessárias sobre aproximadamente dois milhões de linhas.

Todos os gráficos devem possuir título, eixos, unidade, rótulos legíveis e legenda apenas quando necessária.

### RF-13 — Consolidar discussão e conclusão

A discussão deve cobrir:

- população analisada e exclusões;
- desbalanceamento das classes;
- ausências e falhas de conversão;
- duplicidades;
- inconsistências temporais e extremos;
- alta cardinalidade;
- limitações da base consolidada;
- risco de vazamento;
- possíveis vieses de cobertura;
- consequências para a Avaliação 2.

Cada afirmação quantitativa deve ser rastreável a uma tabela, estatística ou gráfico produzido anteriormente.

Não usar `comprova`, `demonstra causalidade` ou equivalente para associações descritivas.

Adicionar uma conclusão breve da Avaliação 1 antes dos encaminhamentos para a Avaliação 2.

### RF-14 — Manter dicionário e notebook reconciliados

Preservar as abas atuais:

- `Base consolidada`;
- `Variáveis analíticas`.

Depois da reorganização do notebook:

- conferir que as 25 colunas de entrada continuam documentadas;
- conferir que todas as variáveis analíticas efetivamente usadas estão documentadas;
- remover do dicionário variável abandonada;
- incluir variável nova apenas quando ela for materialmente usada;
- manter origem, regra, temporalidade e restrição futura nas observações.

Não renomear as abas para `Base bruta` e `Variáveis derivadas`, pois isso faria o projeto regredir em relação à terminologia consolidada nos PRs anteriores.

### RF-15 — Manter o relatório coerente

O relatório não precisa ser reescrito integralmente. Atualizá-lo somente quando as novas auditorias ou análises exigirem correção de:

- totais citados;
- percentuais das classes;
- limitações;
- terminologia;
- conclusões;
- encaminhamentos para a Avaliação 2.

Preservar:

- template institucional;
- Times New Roman 12 no corpo;
- títulos semânticos;
- introdução, objetivos, referencial e referências;
- distinção entre atraso na partida e atraso na chegada;
- linguagem cautelosa;
- conjunto bibliográfico atual, salvo necessidade justificada.

Depois de qualquer alteração, gerar novamente o DOCX e revisar visualmente todas as páginas.

### RF-16 — Completar o README operacional

Adicionar ao README, após validação final:

- versão de Python efetivamente usada;
- versões principais efetivamente testadas ou referência inequívoca ao `requirements.txt`;
- comando ou procedimento de execução integral do notebook;
- tempo observado de execução;
- memória máxima aproximada ou orientação prática de memória;
- ambiente em que as medições foram obtidas;
- ressalva de que tempo e memória variam por máquina.

Manter as instruções atuais de build, validação, pacote e separação entre avaliações.

### RF-17 — Notebook de entrega sem outputs

O fluxo final deve ser:

1. gerar ou preparar uma cópia de validação;
2. executar todas as células com kernel reiniciado;
3. confirmar ausência de erros;
4. registrar tempo e memória;
5. preservar evidência interna da execução;
6. executar o build novamente;
7. confirmar que o notebook de `target/` possui outputs vazios e `execution_count` nulo.

Não versionar o notebook executado nem inserir HTML manual para simular resultados.

### RF-18 — Ampliar testes e validações

Adicionar testes automatizados, quando viável, para:

- limites das seis faixas;
- consistência entre faixa ordinal e alvo binário;
- esquema exato de 25 colunas;
- correspondência entre variáveis criadas e dicionário;
- ausência de outputs e contagens;
- ausência de caminhos absolutos;
- ausência dos banners e referências a números de células removidos pela issue;
- nomes e conjunto exato dos quatro artefatos.

O build documental não precisa executar os dois milhões de registros em toda chamada. A execução completa deve existir como validação separada e documentada.

## 6. Requisitos não funcionais

### RNF-01 — Reprodutibilidade

Execuções sucessivas sobre a mesma base devem produzir os mesmos totais, classes e agregações. Toda amostragem deve usar semente fixa.

### RNF-02 — Clareza didática

O notebook deve ser compreensível para alguém que conheça fundamentos de Python e estatística, mas não conheça a POC nem os scripts que lhe deram origem.

### RNF-03 — Rastreabilidade

Toda transformação relevante deve indicar:

- coluna de origem;
- regra aplicada;
- quantidade de registros afetados;
- justificativa metodológica.

### RNF-04 — Integridade

Nenhuma falha de esquema, conversão ou domínio pode ser ocultada por:

- `except Exception` sem reemissão;
- supressão global de avisos;
- preenchimento silencioso com zero;
- seleção arbitrária de arquivo;
- continuação após validação obrigatória malsucedida.

### RNF-05 — Desempenho

O notebook deve operar sobre aproximadamente 1,99 milhão de registros sem multiplicar cópias completas sem necessidade.

Preferir:

- tipos explícitos para identificadores;
- agregações para gráficos;
- operações vetorizadas;
- amostras reprodutíveis apenas quando necessárias;
- liberação de objetos temporários grandes quando deixarem de ser usados.

### RNF-06 — Escopo

Não implementar treinamento, otimização ou avaliação de modelos nesta issue.

## 7. Critérios de aceitação

### CA-01 — Build preservado

`python scripts/build_avaliacao_01.py` deve continuar produzindo e validando os quatro entregáveis com os nomes atuais.

### CA-02 — Execução limpa

Em ambiente preparado pelo README, o notebook deve executar integralmente com a base compactada, sem extração manual, renomeação ou edição de caminhos.

### CA-03 — Entrada determinística

O output deve identificar o arquivo escolhido e, para ZIP, o membro CSV. Entradas ausentes ou ambíguas devem falhar claramente.

### CA-04 — Notebook reorganizado

O notebook deve alternar explicação, operação e interpretação. Não deve conter banners com `=`, referências como `CÉLULA 8`, célula vazia final nem blocos que combinem fases independentes.

### CA-05 — Qualidade quantificada

Devem existir resultados verificáveis para ausências, tipos, domínios, duplicidades, situações operacionais, timestamps inválidos, extremos e divergências de atraso.

### CA-06 — População reconciliada

A relação entre entrada, exclusões e população final deve fechar numericamente, com precedência ou sobreposição documentada.

### CA-07 — Fronteiras validadas

Todos os testes de limite das seis faixas e do alvo binário devem passar, inclusive para ausentes.

### CA-08 — Gráficos completos

Nenhum gráfico pode ficar vazio por erro de mapeamento. Análises por grupo devem declarar denominadores e critério de volume.

### CA-09 — Conclusões sustentadas

Afirmações quantitativas devem ser rastreáveis aos resultados do notebook. Associações não podem ser apresentadas como causalidade.

### CA-10 — Dicionário reconciliado

As abas `Base consolidada` e `Variáveis analíticas` devem corresponder ao CSV e às variáveis efetivamente usadas pelo notebook.

### CA-11 — Relatório validado

Se alterado, o DOCX deve manter as quatro seções obrigatórias, coerência terminológica e renderização sem cortes ou sobreposições.

### CA-12 — README suficiente

O README deve informar ambiente testado, execução integral, tempo e memória observados, além dos comandos já existentes.

### CA-13 — Notebook final limpo

O notebook produzido em `target/` deve ter todos os outputs vazios e `execution_count` nulo.

### CA-14 — Repositório limpo

Não versionar ambiente virtual, caches, checkpoints, outputs de `target/`, notebook executado ou cópia extraída da base.

### CA-15 — Avaliação 2 preservada

O comando da Avaliação 2 deve continuar encerrando com código `2` e mensagem explícita enquanto seus entregáveis não forem implementados.

## 8. Plano de validação

### 8.1 Testes rápidos

Executar:

```bash
python -m unittest discover -s tests -v
python -m compileall -q scripts tests
python scripts/build_avaliacao_01.py
python scripts/validate_all.py --avaliacao 1
```

Confirmar também:

```bash
git diff --check
```

### 8.2 Execução integral do notebook

1. Criar ambiente limpo com a versão de Python documentada.
2. Instalar apenas `requirements.txt`.
3. Confirmar que o CSV não está previamente extraído.
4. Executar o notebook com kernel reiniciado.
5. Medir tempo total e pico aproximado de memória.
6. Confirmar ausência de erros.
7. Verificar as asserções das faixas.
8. Conferir que os gráficos possuem dados.
9. Executar novamente ou repetir agregações críticas para verificar determinismo.
10. Não copiar o notebook executado para a entrega.

### 8.3 Validação independente de dados

Conferir por cálculo independente:

- quantidade de linhas e colunas;
- cobertura 2024–2025;
- categorias de exclusão;
- população retida;
- distribuição das seis faixas;
- distribuição binária;
- quantidade de extremos;
- divergências entre atraso fornecido e recalculado.

### 8.4 Validação do dicionário

1. Comparar o cabeçalho do CSV interno com `Base consolidada`.
2. Comparar as variáveis usadas no notebook com `Variáveis analíticas`.
3. Conferir tipos, unidades, domínios, origem e restrições.
4. Renderizar e revisar visualmente as duas abas.

### 8.5 Validação do relatório

Se houver alteração de conteúdo ou gerador:

1. conferir as quatro seções;
2. conferir citações e referências;
3. renderizar todas as páginas;
4. inspecionar cabeçalho, rodapé, paginação, recuos e quebras;
5. confirmar que percentuais e conclusões correspondem ao notebook final.

### 8.6 Validação do pacote

1. Gerar o pacote a partir de outro diretório.
2. Confirmar os quatro nomes esperados.
3. Executar o notebook de `target/` ao lado do ZIP gerado.
4. Confirmar que a precedência escolhe o ZIP do pacote.
5. Confirmar ausência de caminhos absolutos e dependência da POC.
6. Gerar novamente o pacote e confirmar equivalência de conteúdo e estrutura.

## 9. Sequência recomendada

### Etapa 1 — Reestruturar o notebook

- dividir células grandes;
- remover banners e numeração manual;
- inserir Markdown antes das operações;
- inserir interpretações após resultados.

### Etapa 2 — Completar auditorias

- tipos e domínios;
- duplicidades exatas e chave natural;
- auditoria temporal detalhada;
- reconciliação de exclusões;
- divergências entre atrasos.

### Etapa 3 — Validar alvos

- extrair uma função pequena e legível no notebook;
- adicionar casos de fronteira;
- validar faixa, rótulo e alvo binário;
- tratar ausentes explicitamente.

### Etapa 4 — Completar exploração

- mês;
- aeroportos;
- rotas;
- filtros de volume;
- interpretações e conclusão.

### Etapa 5 — Reconciliar artefatos

- dicionário;
- relatório, somente quando necessário;
- README com ambiente, tempo e memória;
- testes automatizados.

### Etapa 6 — Validar a entrega

- testes rápidos;
- execução integral;
- inspeção visual do Excel e do Word;
- build fora da raiz;
- execução do pacote final;
- notebook final sem outputs.

## 10. Fora do escopo

Não fazem parte desta issue:

- substituir a arquitetura unificada das duas avaliações;
- voltar a versionar DOCX e XLSX gerados como fontes;
- alterar o alvo principal para atraso na chegada;
- divisão definitiva em treino, validação e teste;
- treinamento de modelos;
- otimização de hiperparâmetros;
- avaliação de desempenho preditivo;
- matriz de confusão de modelos;
- publicação de API ou aplicação;
- automação de coleta futura da ANAC;
- alteração do repositório original da POC.

## 11. Riscos e decisões pendentes

### 11.1 Aceitação do ZIP pela plataforma

O projeto suporta e gera ZIP, mas a equipe ainda deve confirmar se a plataforma da disciplina aceita o CSV compactado. Se não aceitar, definir estratégia de submissão sem versionar uma segunda cópia de aproximadamente 685 MB.

### 11.2 Tratamento dos extremos

Ainda não há justificativa suficiente para corrigir ou excluir automaticamente todos os atrasos extremos. A implementação deve priorizar auditoria e sinalização. Qualquer regra de tratamento depende de evidência documentada.

### 11.3 Chave natural

A chave de duplicidade deve ser validada contra a granularidade de etapa de voo e a semântica dos registros. `arquivo_origem + linha_origem` é referência de proveniência, não necessariamente chave de negócio.

### 11.4 Limite de duração planejada

Qualquer limite usado para sinalizar duração implausível deve ser diagnóstico, justificado e separado de uma regra de exclusão.

## 12. Definição de pronto

A issue estará concluída quando:

- todos os critérios de aceitação aplicáveis estiverem atendidos;
- o notebook estiver organizado em unidades didáticas menores;
- as auditorias de qualidade e temporalidade estiverem completas e reconciliadas;
- os limites das classes estiverem testados;
- as análises temporais, por aeroporto e por rota estiverem concluídas ou justificadamente omitidas;
- as conclusões forem rastreáveis aos resultados;
- dicionário, notebook, relatório e README estiverem coerentes;
- tempo e memória da execução final estiverem registrados;
- o notebook executar integralmente a partir do pacote final;
- o notebook destinado à submissão estiver sem outputs;
- as duas abas do dicionário e todas as páginas do relatório alterado tiverem sido inspecionadas;
- não houver implementação indevida da Avaliação 2.
