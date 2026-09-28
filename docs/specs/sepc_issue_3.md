# Especificação da issue 3 — adequação da entrega parcial da Avaliação 1

## 1. Objetivo

Revisar os quatro componentes da entrega parcial para que atendam integralmente ao enunciado da Avaliação 1, possam ser avaliados de forma reproduzível e apresentem conclusões sustentadas pelos dados.

Esta issue abrange:

- o notebook Jupyter da Avaliação 1;
- a base de dados entregue;
- o dicionário de dados em Excel;
- o relatório parcial em Word;
- a documentação mínima necessária para executar e conferir a entrega.

O resultado deve ser uma entrega autocontida, organizada e executável do início ao fim em um ambiente limpo, sem depender dos scripts externos existentes no projeto de prova de conceito `mcdia-ml-previsao-atraso-voos`.

## 2. Contexto

O projeto `mcdia-ml-projeto-parcial` foi derivado dos três notebooks e dos artefatos da prova de conceito `mcdia-ml-previsao-atraso-voos`. Para a Avaliação 1, todo o processamento necessário deve estar disponível no próprio notebook entregue.

O enunciado da Avaliação 1 exige quatro componentes:

1. notebook Python no formato `.ipynb`, organizado e comentado;
2. dicionário de dados em Excel;
3. uma única base bruta em CSV ou Excel;
4. relatório parcial em Word com introdução, objetivos, referencial teórico e referências bibliográficas.

A modelagem, a divisão de treino e teste, o ajuste de hiperparâmetros e a avaliação de modelos pertencem à Avaliação 2 e não devem ser implementados nesta issue.

## 3. Estado atual e problemas identificados

### 3.1 Execução do notebook

O repositório contém `base_lucimar_nascimento_v2.zip`, mas o notebook procura `base_lucimar_nascimento_v2.csv`. Em um clone limpo, o CSV não existe no diretório de execução e o notebook termina com `FileNotFoundError`.

O notebook também procura candidatos alternativos e, por fim, seleciona o primeiro CSV encontrado no diretório. Esse comportamento não é determinístico e pode carregar silenciosamente uma base incorreta.

Não existem atualmente:

- `requirements.txt` ou `environment.yml`;
- instruções completas de preparação do ambiente;
- descrição de consumo aproximado de memória e tempo de execução;
- validação automatizada de execução completa em ambiente limpo.

### 3.2 Divergência de esquema

A base entregue possui 25 colunas, incluindo:

- `companhia_icao`;
- `origem_icao`;
- `destino_icao`;
- `atraso_partida_min`.

O mapeamento atual do notebook não reconhece alguns desses nomes. A execução armazenada no notebook registra como ausentes:

- `sg_empresa_icao`;
- `sg_icao_origem`;
- `sg_icao_destino`;
- `rota`.

Essa falha impede a criação da rota e compromete a análise por companhia, origem e destino. A célula apresentada como validação de paridade termina com quatro variáveis ausentes, embora o texto do notebook afirme que o esquema foi validado.

### 3.3 Dicionário incompatível com a base entregue

O dicionário atual contém 19 variáveis analíticas, mas a base bruta entregue possui 25 colunas com outros nomes. Exemplos:

- o dicionário registra `sg_empresa_icao`, enquanto a base contém `companhia_icao`;
- `rota`, `faixa_atraso_partida` e `atraso_bi` são derivadas e não existem na base bruta;
- `codigo_faixa_atraso` é criado no notebook, mas não está documentado no dicionário.

O campo `Variável` do dicionário deve respeitar exatamente letras maiúsculas, minúsculas e grafia da base correspondente.

### 3.4 Inconsistências temporais e outliers

A execução atual apresenta:

- atraso mínimo de `-5.760` minutos;
- atraso máximo de `44.635` minutos;
- assimetria de `125,32`;
- curtose de `69.630,84`.

Há exemplos de voos cuja partida prevista ocorre às 23h55 e cuja partida real aparece às 01h29 do mesmo dia, produzindo uma antecipação calculada de `-1.346` minutos. O caso é compatível com uma inconsistência de calendário na virada do dia e não deve ser interpretado automaticamente como antecipação operacional real.

Esses registros podem alterar:

- as medidas descritivas;
- a distribuição das classes;
- a proporção de voos pontuais ou antecipados;
- as conclusões sobre o desbalanceamento do alvo;
- os resultados da modelagem futura.

### 3.5 Organização do notebook

O notebook atual contém 15 células, sendo 10 de código e 5 de Markdown. As células de código possuem em média aproximadamente 39 linhas e chegam a 88 linhas.

Os principais problemas de organização são:

- grandes blocos que executam várias responsabilidades;
- explicações concentradas por fase, em vez de anteceder cada operação relevante;
- comentários visuais extensos com linhas de `=`;
- referências frágeis a números de células;
- uma célula vazia ao final;
- supressão global de avisos com `warnings.filterwarnings('ignore')`;
- captura genérica de exceções durante a leitura da base;
- interpretações importantes apenas em comentários de código;
- poucas interpretações após tabelas e gráficos.

### 3.6 Cobertura incompleta da Avaliação 1

O notebook cobre bem a definição inicial do problema e da variável-alvo, mas precisa evoluir nos seguintes itens:

- descrição do período e da granularidade da base;
- quantidade de registros e campos;
- data e método da coleta;
- perfil de tipos;
- análise de ausências;
- análise de duplicidades;
- consistência das datas;
- domínio das variáveis categóricas;
- estatísticas de outras variáveis relevantes além do atraso;
- discussão explícita das limitações da base;
- separação entre associação descritiva e causalidade.

### 3.7 Outputs armazenados no notebook

O arquivo `.ipynb` armazena outputs em MIME, incluindo tabelas `text/html`, gráficos `image/png` e textos. Esse HTML é gerado automaticamente pelo Jupyter e não corresponde a código HTML escrito manualmente.

Como o avaliador executará o notebook, a versão final deve ser entregue sem outputs persistidos e sem contagens de execução, depois que uma cópia equivalente tiver sido validada com `Restart Kernel and Run All`.

### 3.8 Relatório parcial

O relatório atende aos requisitos visuais principais:

- fonte Times New Roman;
- tamanho 12;
- texto justificado;
- cinco páginas;
- ausência de cortes e sobreposições relevantes.

Os problemas de conteúdo e edição são:

- subtítulos sem estilos semânticos de título;
- erro em `2.2 Objetivo Específicos`;
- quebras e recuos irregulares na lista das faixas;
- objetivos que misturam esta entrega com a implementação da Avaliação 2;
- ausência de referências formais para a fonte de dados e para normas citadas;
- referências acadêmicas inconsistentes;
- sete referências, enquanto o enunciado solicita entre três e cinco manuscritos acadêmicos.

A referência atribuída a Kalliguddi e Leboulluec mistura autores e título de publicações diferentes. O título `Flight delay prediction: Evaluating machine learning algorithms for enhanced accuracy` pertence a AlBassam e AlShahrani, publicado em 2025 na PLOS ONE. Kalliguddi e Leboulluec publicaram `Predictive Modeling of Aircraft Flight Delay`, em 2017.

A referência de Sternberg também deve ser revisada. A versão original disponível no arXiv e a versão posteriormente publicada possuem título e lista de autores diferentes.

### 3.9 README, nomes e higiene do repositório

O README atual contém apenas uma frase e não permite que o avaliador prepare ou execute o projeto.

Os nomes de arquivos também não seguem literalmente o padrão descrito no enunciado. Existem espaços e o sufixo `v2`, por exemplo em `dicionario_lucimar_nascimento v2.xlsx`.

O diretório local contém artefatos de IDE, como `.idea/` e arquivo `.iml`, que não devem fazer parte da entrega.

## 4. Resultado esperado

Ao concluir esta issue, uma pessoa avaliadora deverá conseguir:

1. clonar ou descompactar o projeto;
2. identificar imediatamente os quatro entregáveis;
3. instalar as dependências descritas;
4. abrir o notebook na raiz do projeto;
5. executar todas as células em ordem, sem intervenção manual;
6. obter resultados consistentes com a base entregue;
7. entender as decisões de limpeza e suas consequências;
8. conferir cada coluna da base no dicionário;
9. relacionar as conclusões do notebook às evidências apresentadas;
10. abrir um relatório Word formatado, coerente e bibliograficamente correto.

## 5. Requisitos funcionais

### RF-01 — Leitura autocontida da base

O notebook deve localizar a base a partir de um caminho relativo à raiz do projeto.

Requisitos:

- suportar diretamente o arquivo ZIP entregue, desde que contenha exatamente um CSV esperado;
- não depender de extração manual;
- não escolher arbitrariamente o primeiro CSV do diretório;
- informar claramente o arquivo utilizado;
- validar que o ZIP possui o membro esperado;
- apresentar mensagem de erro objetiva se o arquivo estiver ausente ou inválido;
- evitar a extração permanente de uma cópia de aproximadamente 685 MB, quando a leitura direta do ZIP for suficiente.

### RF-02 — Validação da estrutura de entrada

Imediatamente após a leitura, o notebook deve:

- mostrar quantidade de linhas e colunas;
- listar os nomes recebidos;
- verificar nomes duplicados;
- validar o conjunto mínimo de colunas necessárias;
- interromper a execução com mensagem informativa se uma coluna obrigatória estiver ausente;
- não continuar com gráficos ou conclusões parciais quando o esquema estiver inválido.

### RF-03 — Mapeamento determinístico de colunas

O código de normalização deve contemplar os nomes realmente existentes na base entregue, incluindo pelo menos:

- `companhia_icao` para `sg_empresa_icao`, caso o nome analítico seja mantido;
- `numero_voo` para `nr_voo`;
- `origem_icao` para `sg_icao_origem`;
- `destino_icao` para `sg_icao_destino`;
- `partida_prevista` para `dt_partida_prevista`;
- `partida_real` para `dt_partida_real`;
- `chegada_prevista` para `dt_chegada_prevista`;
- `chegada_real` para `dt_chegada_real`;
- `situacao_voo` para `cd_situacao_voo`;
- `atraso_partida_min` para `atraso_partida_minutos`, quando aplicável.

O mapeamento deve detectar e rejeitar ambiguidades. Duas colunas de entrada não podem ser renomeadas silenciosamente para o mesmo nome final.

### RF-04 — Preservação da base bruta

O DataFrame lido da base deve permanecer sem alterações para auditoria. As transformações devem ocorrer em uma cópia analítica claramente nomeada.

O notebook deve distinguir pelo menos:

- base bruta carregada;
- base elegível para cálculo do alvo;
- base analítica usada nas estatísticas e gráficos.

Cada transição deve apresentar:

- quantidade anterior de linhas;
- quantidade removida;
- percentual removido;
- motivos mutuamente identificáveis para a remoção.

### RF-05 — Auditoria inicial de qualidade

Antes da limpeza, o notebook deve apresentar:

- tipos inferidos;
- quantidade e percentual de ausentes por coluna;
- quantidade de duplicidades exatas;
- análise de possíveis duplicidades por chave natural;
- frequências das situações operacionais;
- quantidade de cancelados e realizados;
- cobertura temporal mínima e máxima;
- cardinalidade das principais variáveis categóricas;
- valores fora dos domínios esperados.

A chave natural adotada para investigar duplicidades deve ser documentada. Uma opção inicial é combinar empresa, número do voo, origem, destino e partida prevista, mas a escolha deve ser confirmada contra a semântica da base.

### RF-06 — Conversão e auditoria temporal

A conversão de datas deve usar uma regra explícita e compatível com o formato real da base.

O notebook deve quantificar separadamente:

- timestamps inválidos;
- partidas reais ausentes;
- partidas previstas ausentes;
- voos realizados sem dados suficientes para calcular o alvo;
- atrasos menores que `-1.440` minutos;
- atrasos maiores que `1.440` minutos;
- atrasos maiores que sete dias;
- durações planejadas negativas ou implausíveis;
- diferenças entre o atraso fornecido pela base e o atraso recalculado.

Casos extremos devem permanecer na base bruta e aparecer em uma pequena tabela de auditoria, com campos suficientes para rastreá-los.

Qualquer regra de correção de virada do dia deve ser explícita, testável e conservadora. Não se deve somar ou subtrair 24 horas de todos os casos negativos sem evidência de que o problema é de calendário.

Para voos internacionais, deve-se confirmar se os timestamps estão em horário local, UTC ou outro padrão antes de interpretar diretamente a diferença entre chegada prevista e partida prevista como duração do voo.

### RF-07 — Definição da população analisada

O notebook deve justificar a população usada na análise do atraso de partida.

No mínimo:

- cancelamento deve ser apresentado como situação operacional separada;
- apenas voos realizados com partida prevista e real válidas podem receber alvo de atraso de partida;
- registros excluídos devem ser contabilizados;
- a regra para inconsistências temporais deve ser definida antes da análise das distribuições finais;
- a base usada na Avaliação 1 não pode apagar silenciosamente casos problemáticos.

### RF-08 — Construção e validação das variáveis-alvo

As faixas devem ter limites não ambíguos e exaustivos:

- faixa 0: atraso menor ou igual a 0 minuto;
- faixa 1: atraso maior que 0 e menor que 15 minutos;
- faixa 2: atraso entre 15 e 30 minutos, inclusive;
- faixa 3: atraso maior que 30 e menor ou igual a 45 minutos;
- faixa 4: atraso maior que 45 e menor ou igual a 60 minutos;
- faixa 5: atraso maior que 60 minutos.

Devem existir testes ou asserções para os valores de fronteira:

- `-1`;
- `0`;
- valor positivo imediatamente acima de `0`;
- valor imediatamente abaixo de `15`;
- `15`;
- `30`;
- valor imediatamente acima de `30`;
- `45`;
- valor imediatamente acima de `45`;
- `60`;
- valor imediatamente acima de `60`.

O alvo binário deve ser derivado da mesma regra e validado contra as faixas 0 a 5.

O notebook deve documentar separadamente:

- atraso contínuo calculado;
- código ordinal da faixa;
- rótulo textual da faixa;
- alvo binário secundário.

### RF-09 — Engenharia de variáveis compatível com o momento da previsão

As variáveis explicativas apresentadas como candidatas à Avaliação 2 devem usar somente informações disponíveis antes da partida.

O notebook deve identificar explicitamente como pós-evento e proibidas em `X`:

- partida real;
- chegada real;
- atraso calculado;
- situação final do voo;
- qualquer justificativa registrada após o evento;
- as próprias variáveis-alvo.

Variáveis derivadas de horários previstos podem ser produzidas na Avaliação 1 para fins descritivos, desde que a origem e a regra sejam documentadas.

### RF-10 — Análises descritivas

As medidas de posição e dispersão não devem se limitar a uma única variável sem justificativa.

O notebook deve incluir, conforme aplicável:

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

As análises devem cobrir o atraso e outras variáveis numéricas relevantes, como duração planejada, quando sua interpretação for válida.

Para variáveis categóricas, devem ser mostradas frequências e proporções, evitando tabelas excessivamente extensas.

### RF-11 — Exploração gráfica

O notebook deve incluir gráficos que atendam ao escopo exploratório, no mínimo:

- distribuição das seis faixas do alvo;
- histograma e boxplot do atraso com tratamento visual explícito de extremos;
- evolução temporal por mês;
- taxa ou composição das faixas por hora prevista;
- comparação descritiva entre companhias de maior volume;
- comparação descritiva entre aeroportos ou rotas relevantes, após correção do mapeamento.

Os gráficos devem ser produzidos a partir de agregações ou amostras reprodutíveis quando o uso das quase duas milhões de linhas completas for desnecessário.

Não usar `countplot` sobre toda a base quando uma tabela agregada já contiver as contagens. Evitar KDE sobre milhões de registros; quando uma amostra for usada, fixar a semente e declarar seu tamanho.

Todos os gráficos devem possuir:

- título objetivo;
- eixos identificados;
- unidade de medida;
- legenda apenas quando necessária;
- rótulos legíveis;
- interpretação em Markdown após o gráfico.

### RF-12 — Discussão preliminar

A discussão deve responder diretamente aos resultados observados e incluir:

- desbalanceamento das classes;
- ausências;
- inconsistências temporais;
- duplicidades;
- alta cardinalidade;
- limites da fonte de dados;
- risco de vazamento de dados;
- possíveis vieses de cobertura;
- consequências para a Avaliação 2.

As conclusões devem separar claramente:

- evidência observada;
- hipótese explicativa;
- decisão metodológica;
- limitação ainda não resolvida.

Não usar termos como `comprova`, `demonstra causalidade` ou equivalentes quando a evidência for apenas uma associação descritiva.

### RF-13 — Organização didática do notebook

O notebook deve alternar células de Markdown e código em unidades pequenas e coerentes.

Cada célula relevante de código deve executar uma responsabilidade principal. Funções auxiliares podem ser maiores quando isso melhorar a clareza, mas não devem misturar leitura, limpeza, transformação, estatística e visualização em um único bloco.

O Markdown que antecede uma operação deve explicar:

- objetivo;
- motivação;
- entrada utilizada;

- resultado esperado;
- como interpretar o output.

Após tabelas e gráficos importantes, incluir uma interpretação curta e cautelosa.

Remover:

- banners de comentários com linhas de `=`;
- numeração manual de células;
- referências como `Célula 10`;
- célula vazia final;
- avisos globalmente suprimidos;
- código morto e imports não utilizados.

### RF-14 — Estrutura recomendada do notebook

O notebook final deve seguir, em linhas gerais, esta sequência:

1. título, disciplina, integrantes e representante;
2. objetivo e escopo da Avaliação 1;
3. problema de pesquisa, tarefa supervisionada e alvo;
4. fonte, período, granularidade e limitações conhecidas;
5. importação das bibliotecas;
6. localização e leitura da base compactada;
7. inspeção inicial de dimensões e esquema;
8. mapeamento e validação de colunas;
9. tipos e conversões;
10. perfil de ausências;
11. duplicidades e situações operacionais;
12. auditoria temporal e de outliers;
13. critérios de elegibilidade;
14. construção e teste das variáveis derivadas;
15. estatísticas descritivas;
16. frequências categóricas;
17. distribuição das variáveis-alvo;
18. análises por mês, hora, companhia, aeroporto e rota;
19. discussão preliminar;
20. conclusão e encaminhamentos para a Avaliação 2.

Essa estrutura é uma referência. Pode ser ajustada se a nova organização preservar todos os requisitos e permanecer fácil de acompanhar.

### RF-15 — Notebook final sem outputs persistidos

Antes da entrega:

1. executar o notebook completo em ambiente limpo;
2. preservar uma evidência interna da execução bem-sucedida;
3. limpar todos os outputs do notebook que será entregue;
4. remover todos os `execution_count`;
5. validar que nenhuma célula de código ou Markdown foi removida durante a limpeza.

Não inserir HTML manual para simular resultados.

### RF-16 — Desempenho e consumo de memória

O notebook deve ser compatível com a base de aproximadamente 1,99 milhão de registros sem multiplicar desnecessariamente cópias completas em memória.

Medidas recomendadas:

- ler somente colunas necessárias quando isso não impedir a auditoria exigida;
- declarar `dtype` para identificadores e categorias quando seguro;
- evitar múltiplas chamadas encadeadas de `copy()` sobre toda a base;
- usar tabelas agregadas para gráficos;
- usar amostra com semente para visualizações densas;
- liberar objetos temporários grandes quando deixarem de ser necessários;
- documentar o consumo aproximado observado na validação final.

Não sacrificar a rastreabilidade da base bruta apenas para reduzir memória.

### RF-17 — Dicionário da base bruta

O Excel deve conter uma aba `Base bruta` com todas as colunas do CSV entregue, usando exatamente os nomes presentes no arquivo.

Para cada variável, preencher:

- Variável;
- Nome Descritivo;
- Tipo de Dado;
- Unidade de Medida;
- Domínio / Categoria;
- Descrição / Significado;
- Observações.

O dicionário deve documentar as 25 colunas da base bruta, salvo se a base entregue for deliberadamente substituída por outra estrutura aprovada.

### RF-18 — Dicionário de variáveis derivadas

O Excel deve conter uma aba separada `Variáveis derivadas` para documentar as variáveis criadas no notebook, incluindo, quando mantidas:

- `sg_empresa_icao`;
- `nr_voo`;
- `sg_icao_origem`;
- `sg_icao_destino`;
- `rota`;
- `dt_partida_prevista`;
- `dt_partida_real`;
- `dt_chegada_prevista`;
- `dt_chegada_real`;
- `ano`;
- `mes`;
- `dia_semana`;
- `hora_partida_prevista`;
- `minuto_partida_previsto`;
- `tempo_voo_planejado_minutos`;
- `cd_situacao_voo`;
- `atraso_partida_minutos`;
- `codigo_faixa_atraso`;
- `faixa_atraso_partida`;
- `atraso_bi`.

Cada linha derivada deve informar na coluna `Observações`:

- variável ou variáveis de origem;
- regra resumida de transformação;
- se a variável é pré-voo, pós-voo ou target;
- eventuais restrições de uso futuro.

### RF-19 — Usabilidade do dicionário

O Excel deve possuir:

- cabeçalho legível e destacado;
- autofiltro;
- primeira linha congelada;
- quebra automática de texto;
- larguras coerentes;
- altura ajustada ao conteúdo;
- tipos e domínios descritos de maneira padronizada;
- ausência de textos truncados;
- revisão visual de todas as abas.

### RF-20 — Relatório parcial

O relatório deve manter o template institucional e atender aos requisitos de fonte Times New Roman, tamanho 12 e alinhamento justificado.

Conteúdo obrigatório:

- introdução;
- objetivo geral;
- objetivos específicos;
- referencial teórico;
- referências bibliográficas.

Também deve:

- distinguir o objetivo desta entrega parcial do objetivo futuro do projeto completo;
- não apresentar como concluídas etapas reservadas à Avaliação 2;
- manter coerência entre problema, alvo, base e notebook;
- citar a fonte oficial dos dados;
- citar normas regulatórias somente quando sustentarem uma afirmação específica;
- usar de três a cinco manuscritos acadêmicos centrais, conforme o enunciado;
- separar, quando necessário, referências acadêmicas, livros metodológicos e documentos institucionais;
- corrigir autoria, título, periódico, ano, volume, páginas e DOI de cada referência;
- manter padrão bibliográfico uniforme.

### RF-21 — Referências que exigem correção

Revisar especificamente:

1. Kalliguddi e Leboulluec:
   - título correto: `Predictive Modeling of Aircraft Flight Delay`;
   - ano: 2017;
   - periódico: `Universal Journal of Management`;
   - volume 5, número 10, páginas 485–491;
   - DOI: `10.13189/ujm.2017.051003`.

2. Artigo PLOS ONE de 2025:
   - título: `Flight delay prediction: Evaluating machine learning algorithms for enhanced accuracy`;
   - autores: Sarah Ahmed A. AlBassam e Samira Dhafir N. AlShahrani;
   - PLOS ONE 20(12), e0335141;
   - DOI: `10.1371/journal.pone.0335141`.

3. Revisão sobre predição de atrasos:
   - decidir se será citada a versão original do arXiv de 2017 ou a versão publicada em `Transport Reviews`;
   - usar o título e a lista de autores correspondentes à versão escolhida;
   - não combinar metadados das duas versões.

Fontes para conferência:

- <https://www.hrpub.org/journals/article_info.php?aid=6569>
- <https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0335141>
- <https://arxiv.org/abs/1703.06118>
- <https://doi.org/10.1080/01441647.2020.1861123>

### RF-22 — Formatação e estrutura do relatório

Corrigir pelo menos:

- `2.2 Objetivo Específicos` para `2.2 Objetivos Específicos`;
- estilos semânticos para títulos e subtítulos;
- recuos e quebras da lista das seis faixas;
- quebras de página inadequadas;
- espaçamento entre títulos e parágrafos;
- consistência de itálico em termos estrangeiros;
- consistência dos símbolos matemáticos e intervalos.

Após qualquer alteração, renderizar novamente o Word e revisar visualmente todas as páginas.

### RF-23 — README de execução

O README deve conter:

- título e objetivo da entrega;
- integrantes e representante do grupo;
- descrição resumida do problema;
- lista dos quatro entregáveis;
- estrutura do repositório;
- fonte, período e data de coleta da base;
- instruções de instalação;
- instruções para abrir e executar o notebook;
- informação de que a base é lida diretamente do ZIP;
- versões de Python e bibliotecas validadas;
- tempo e memória aproximados da execução completa;
- política de entrega sem outputs;
- separação entre escopo da Avaliação 1 e da Avaliação 2;
- limitações relevantes conhecidas.

### RF-24 — Dependências reproduzíveis

Criar um arquivo de dependências mínimo contendo apenas o necessário para o notebook, por exemplo:

- NumPy;
- pandas;
- Matplotlib;
- seaborn;
- Jupyter ou ipykernel, conforme o fluxo adotado.

As versões devem ser compatíveis com a versão de Python indicada no README. Evitar fixar versões excessivamente novas ou incomuns sem necessidade.

### RF-25 — Padronização dos nomes de entrega

Adotar nomes compatíveis com o padrão do enunciado, preferencialmente:

- `lucimar_nascimento.ipynb`;
- `dicionario_lucimar_nascimento.xlsx`;
- `base_lucimar_nascimento.csv`, dentro de ZIP apenas se a plataforma aceitar compactação;
- `relatorio_parcial_lucimar_nascimento.docx`.

Antes de renomear, confirmar se o sufixo `_v2` ou outro identificador foi solicitado pela docente ou exigido pela plataforma. Na ausência de exigência externa, remover espaços e sufixos de versão dos nomes finais.

### RF-26 — Higiene do repositório

Adicionar `.gitignore` apropriado para excluir:

- `.idea/`;
- `*.iml`;
- `.ipynb_checkpoints/`;
- ambientes virtuais;
- caches do Python;
- arquivos temporários;
- cópias locais extraídas da base, quando não forem o artefato oficial da entrega.

Não remover nem sobrescrever trabalho local não relacionado sem revisão prévia.

## 6. Requisitos não funcionais

### RNF-01 — Reprodutibilidade

A execução deve produzir os mesmos totais e agregações relevantes em execuções sucessivas sobre o mesmo arquivo.

Toda amostragem deve usar semente fixa.

### RNF-02 — Clareza didática

O notebook deve poder ser lido por alguém que conheça fundamentos de Python e estatística, mas não conheça previamente a prova de conceito.

### RNF-03 — Rastreabilidade

Toda transformação relevante deve indicar:

- coluna de origem;
- regra aplicada;
- quantidade de registros afetados;
- justificativa metodológica.

### RNF-04 — Integridade

Nenhuma falha de esquema, conversão ou domínio pode ser ocultada por:

- `except Exception` sem reemissão do erro;
- `warnings.filterwarnings('ignore')` global;
- preenchimento silencioso com zero;
- seleção arbitrária de arquivo;
- continuação após asserção de integridade malsucedida.

### RNF-05 — Escopo

As referências à Avaliação 2 devem aparecer apenas como encaminhamentos. Esta issue não deve implementar treinamento, otimização ou avaliação de modelos.

## 7. Critérios de aceitação

### CA-01 — Execução limpa

Dado um clone limpo contendo os arquivos versionados, quando o ambiente descrito no README for preparado e o notebook for executado com kernel reiniciado, então todas as células devem terminar sem erro e sem necessidade de copiar, extrair ou renomear a base manualmente.

### CA-02 — Arquivo de entrada determinístico

O notebook deve registrar no output de validação o caminho do ZIP e o nome exato do CSV interno. A execução deve falhar se o ZIP não contiver o arquivo esperado ou contiver estrutura ambígua.

### CA-03 — Paridade do esquema

A validação final não pode apresentar como ausentes `sg_empresa_icao`, `sg_icao_origem`, `sg_icao_destino` ou `rota`.

Todas as variáveis que o notebook declara construir devem existir e possuir tipo e domínio compatíveis.

### CA-04 — Dicionário completo

A aba `Base bruta` deve documentar exatamente todas as colunas do CSV entregue. A aba `Variáveis derivadas` deve documentar todas as colunas criadas pelo notebook e utilizadas na análise.

Não deve haver variável usada no notebook sem documentação correspondente.

### CA-05 — Qualidade quantificada

O notebook deve apresentar valores verificáveis para ausências, duplicidades, situações operacionais, timestamps inválidos e outliers temporais antes de aplicar exclusões.

### CA-06 — População final reconciliada

Deve ser possível reconciliar:

`linhas brutas = linhas elegíveis + linhas excluídas`, considerando categorias de exclusão claramente apresentadas e sem dupla contagem não explicada.

### CA-07 — Limites das classes validados

Os testes de fronteira das seis faixas e do alvo binário devem passar. Não pode haver lacuna ou sobreposição entre faixas.

### CA-08 — Gráficos completos

Todos os gráficos condicionais esperados devem ser produzidos. Não pode haver eixo vazio por ausência de coluna ou falha de mapeamento.

### CA-09 — Conclusões sustentadas

Cada afirmação quantitativa da discussão deve poder ser ligada a uma tabela, estatística ou gráfico produzido anteriormente no notebook.

Associações descritivas não devem ser apresentadas como prova causal.

### CA-10 — Notebook organizado

O notebook deve alternar explicação e execução, não possuir célula vazia final, comentários decorativos extensos, referências por número de célula ou blocos que combinem várias etapas independentes.

### CA-11 — Notebook de submissão limpo

O `.ipynb` final deve ter todos os outputs removidos e `execution_count` nulo em todas as células de código.

### CA-12 — Relatório validado

O Word final deve:

- manter Times New Roman 12 e alinhamento justificado no corpo;
- renderizar sem cortes ou sobreposições;
- conter as quatro seções exigidas;
- conter de três a cinco manuscritos acadêmicos selecionados;
- possuir referências bibliograficamente verificadas;
- estar coerente com a terminologia e as faixas do notebook.

### CA-13 — README suficiente

Uma pessoa sem conhecimento prévio da POC deve conseguir preparar o ambiente e executar a entrega usando apenas o README e os arquivos do projeto.

### CA-14 — Repositório limpo

Arquivos de IDE, caches, checkpoints e cópias temporárias não devem aparecer entre os arquivos versionados da entrega.

## 8. Plano de validação

### 8.1 Validação do notebook

1. Criar ambiente limpo com a versão documentada do Python.
2. Instalar somente as dependências declaradas.
3. Confirmar que o CSV não está previamente extraído.
4. Executar o notebook do início ao fim com kernel reiniciado.
5. Registrar tempo total e pico aproximado de memória.
6. Confirmar ausência de exceções e avisos inesperados.
7. Conferir os totais principais contra a base por cálculo independente.
8. Conferir as fronteiras das classes.
9. Conferir que todos os gráficos possuem dados.
10. Executar novamente para verificar determinismo.
11. Limpar outputs apenas depois da validação.

### 8.2 Validação da base e do dicionário

1. Ler o cabeçalho do CSV interno ao ZIP.
2. Comparar os nomes com a aba `Base bruta`.
3. Confirmar igualdade exata de quantidade e grafia.
4. Comparar todas as variáveis criadas pelo notebook com a aba `Variáveis derivadas`.
5. Conferir tipos, unidades, domínios e observações.
6. Revisar visualmente todas as abas do Excel.

### 8.3 Validação do relatório

1. Conferir conteúdo das quatro seções obrigatórias.
2. Conferir fonte, tamanho e alinhamento.
3. Conferir cada citação no texto contra a lista de referências.
4. Abrir DOI ou página oficial de cada manuscrito.
5. Confirmar autores, título, ano, periódico e páginas.
6. Renderizar o DOCX em PDF ou imagens.
7. Inspecionar todas as páginas em tamanho normal.
8. Conferir recuos, quebras, cabeçalho, rodapé e numeração.

### 8.4 Validação do pacote final

1. Comparar nomes dos arquivos com o enunciado.
2. Confirmar que existem exatamente os entregáveis esperados.
3. Confirmar se a plataforma aceita ZIP para a base.
4. Testar o fluxo documentado no README a partir de uma nova pasta.
5. Verificar que não há caminhos absolutos locais no notebook.
6. Verificar que não há dependência do repositório da POC.

## 9. Sequência recomendada de implementação

### Etapa 1 — Corrigir bloqueadores de execução

- implementar leitura direta do ZIP;
- corrigir o mapeamento de colunas;
- adicionar validações obrigatórias;
- remover seleção arbitrária de CSV;
- criar dependências mínimas e README inicial.

### Etapa 2 — Auditar a qualidade dos dados

- preservar a base bruta;
- produzir perfil de ausências e duplicidades;
- auditar datas e extremos;
- comparar atraso fornecido e recalculado;
- definir população elegível e regras conservadoras.

### Etapa 3 — Reestruturar o notebook

- dividir células por responsabilidade;
- adicionar Markdown antes e depois das análises;
- executar estatísticas e gráficos faltantes;
- corrigir interpretações causais ou não sustentadas;
- separar claramente o escopo da Avaliação 2.

### Etapa 4 — Alinhar o dicionário

- criar abas de base bruta e variáveis derivadas;
- documentar todas as colunas;
- adicionar origem, transformação e restrição de uso;
- aplicar formatação legível e revisar visualmente.

### Etapa 5 — Revisar o relatório

- corrigir objetivos e terminologia;
- selecionar de três a cinco manuscritos;
- corrigir referências misturadas;
- incluir fontes institucionais necessárias;
- corrigir estilos, recuos e quebras;
- renderizar e inspecionar todas as páginas.

### Etapa 6 — Preparar a entrega

- validar tudo em ambiente limpo;
- padronizar nomes;
- confirmar política da plataforma para ZIP;
- remover outputs do notebook;
- remover artefatos de IDE e temporários;
- conferir o pacote final contra o enunciado.

## 10. Fora do escopo

Não fazem parte desta issue:

- divisão definitiva em treino, validação e teste;
- treinamento de regressão logística, Random Forest, HistGradientBoosting, CatBoost ou outro modelo;
- otimização por Grid Search ou Random Search;
- avaliação final de desempenho preditivo;
- matriz de confusão de modelos;
- seleção final de hiperparâmetros;
- publicação de API ou aplicação;
- automação de coleta futura de dados da ANAC;
- alterações no repositório original da prova de conceito.

O notebook pode explicar como as decisões desta etapa afetam a Avaliação 2, mas não deve implementar esses itens.

## 11. Riscos e decisões pendentes

### 11.1 Aceitação do ZIP

O enunciado pede base em CSV ou Excel. Deve-se confirmar se a plataforma aceita o CSV dentro de um ZIP. Se não aceitar, será necessário definir um meio de submissão compatível com o limite de tamanho.

### 11.2 Regra para inconsistências de calendário

Não há evidência suficiente para corrigir automaticamente todos os atrasos extremos. A equipe deve decidir, com base na documentação da fonte e em amostra auditada, se cada classe de problema será:

- corrigida por regra verificável;
- excluída da base analítica;
- mantida e sinalizada;
- tratada como dado de qualidade desconhecida.

### 11.3 Significado dos horários em voos internacionais

É necessário confirmar a referência temporal dos timestamps antes de usar diferenças entre aeroportos como duração de voo.

### 11.4 Nome final dos arquivos

Confirmar se `_v2` foi solicitado externamente. Caso contrário, seguir literalmente os padrões do enunciado.

### 11.5 Seleção bibliográfica

Definir quais três a cinco manuscritos serão centrais. Livros e documentos institucionais podem ser mantidos em categoria adicional apenas se isso não contrariar a orientação da docente.

## 12. Definição de pronto

Esta issue estará concluída somente quando:

- todos os critérios de aceitação estiverem atendidos;
- o notebook tiver sido executado duas vezes em ambiente limpo sem erro;
- a base e o dicionário estiverem integralmente reconciliados;
- as decisões sobre outliers e inconsistências estiverem documentadas e quantificadas;
- o relatório tiver sido conferido visualmente e bibliograficamente;
- o README permitir a reprodução por terceiro;
- os quatro entregáveis finais estiverem nomeados e organizados conforme o enunciado;
- a versão do notebook destinada à submissão estiver sem outputs persistidos;
- não houver implementação indevida de itens da Avaliação 2.
