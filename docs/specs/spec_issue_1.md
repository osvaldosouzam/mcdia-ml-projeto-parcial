# Especificação da issue 1 — fontes versionáveis e geração reproduzível dos entregáveis

## 1. Objetivo

Estruturar o projeto para que os conteúdos editáveis dos entregáveis sejam mantidos em formatos textuais adequados para revisão no Git e para que os arquivos finais exigidos pelas Avaliações 1 e 2 sejam produzidos por comandos automatizados, repetíveis e verificáveis.

Esta issue deve estabelecer a infraestrutura de autoria e build antes das revisões de conteúdo da issue 6. O objetivo não é corrigir nesta etapa todo o conteúdo do notebook, do dicionário ou do relatório, mas criar uma fonte única de verdade e um fluxo seguro para que as correções seguintes sejam feitas nos arquivos-fonte certos.

## 2. Decisão arquitetural

O projeto permanecerá unificado. Não serão criados dois projetos independentes nem duas cópias completas da base, do dicionário, das referências ou da lógica de geração.

A organização adotará:

- conteúdo compartilhado entre as avaliações;
- conteúdo específico de cada avaliação;
- notebooks distintos para cada avaliação;
- dois comandos de build explícitos, um para cada avaliação;
- funções comuns reutilizadas pelos dois comandos;
- diretórios de saída separados;
- tags ou releases do Git para preservar a versão efetivamente entregue em cada avaliação.

### 2.1 Justificativa

A Avaliação 2 é uma evolução da Avaliação 1. Ela reutiliza:

- problema de pesquisa;
- descrição e fonte da base;
- introdução;
- objetivos;
- referencial teórico;
- referências bibliográficas;
- dicionário de dados;
- base consolidada.

Separar todo o projeto em `avaliacao1/` e `avaliacao2/` duplicaria esses elementos e criaria risco de divergência. Por outro lado, usar um único script monolítico com muitas condições tornaria o processo menos claro.

A solução recomendada é manter dois pontos de entrada pequenos e explícitos:

```bash
python scripts/build_avaliacao_01.py
python scripts/build_avaliacao_02.py
```

Ambos devem reutilizar funções de uma biblioteca comum. Não deve haver duplicação da implementação de geração de XLSX, DOCX, validação de notebook ou empacotamento.

## 3. Escopo

### 3.1 Incluído

- definir a estrutura de diretórios;
- converter o conteúdo editável do dicionário para fontes CSV;
- converter o conteúdo editável do relatório parcial para Markdown;
- preservar o template institucional como insumo de geração;
- criar o build da Avaliação 1;
- preparar contratos e estrutura para o build da Avaliação 2;
- gerar XLSX e DOCX a partir das fontes;
- preparar o notebook final sem outputs persistidos;
- reunir os arquivos finais em diretório próprio;
- validar estruturalmente os artefatos gerados;
- documentar o fluxo no README;
- ignorar artefatos gerados e temporários no Git.

### 3.2 Não incluído

- corrigir todas as inconsistências de dados descritas na issue 6;
- reescrever integralmente o relatório;
- selecionar os manuscritos acadêmicos definitivos;
- implementar a modelagem da Avaliação 2;
- treinar ou otimizar modelos;
- alterar a base bruta;
- publicar automaticamente na plataforma da disciplina;
- exigir reprodutibilidade byte a byte de arquivos DOCX e XLSX.

## 4. Princípios

### 4.1 Fonte única de verdade

Arquivos em `target/` nunca devem ser editados manualmente. Qualquer correção deve ocorrer no Markdown, nos CSVs, no notebook-fonte, no template ou nos scripts de geração.

### 4.2 Binários gerados não são fonte

DOCX e XLSX finais são produtos do build e não devem ser versionados após a migração e validação do novo fluxo.

### 4.3 Binários-fonte são permitidos

O template institucional em DOCX, imagens e outros recursos necessários à fidelidade visual podem permanecer versionados. Eles são entradas do build, não resultados gerados.

### 4.4 Build explícito por avaliação

Cada avaliação deve ter seu próprio comando e diretório de saída. Um build não pode sobrescrever artefatos da outra avaliação.

### 4.5 Compartilhamento sem duplicação

Introdução, objetivos, referencial, referências, dicionário e base devem ser compartilhados sempre que a semântica for a mesma. Conteúdo específico deve permanecer isolado.

### 4.6 Falha explícita

Ausência de fonte, esquema inválido, template incorreto ou artefato incompleto deve encerrar o build com erro compreensível.

### 4.7 Validação proporcional

Gerar um arquivo com sucesso não prova que ele está correto. XLSX e DOCX devem passar por verificações estruturais e visuais.

## 5. Estrutura proposta

```text
mcdia-ml-projeto-parcial/
├── data/
│   └── raw/
│       └── base_lucimar_nascimento.zip
├── docs/
│   └── specs/
│       ├── spec_issue_1.md
│       └── spec_issue_6.md
├── notebooks/
│   ├── avaliacao_01/
│   │   └── lucimar_nascimento.ipynb
│   └── avaliacao_02/
│       └── lucimar_nascimento_atividade_2.ipynb
├── sources/
│   ├── shared/
│   │   ├── introducao.md
│   │   ├── objetivos.md
│   │   ├── referencial_teorico.md
│   │   └── referencias.md
│   ├── avaliacao_01/
│   │   ├── relatorio_parcial.md
│   │   └── manifest.json
│   ├── avaliacao_02/
│   │   ├── metodologia.md
│   │   ├── resultados.md
│   │   ├── discussao.md
│   │   ├── conclusao.md
│   │   └── manifest.json
│   └── dicionario/
│       ├── base_bruta.csv
│       └── variaveis_derivadas.csv
├── templates/
│   └── relatorio_institucional.docx
├── scripts/
│   ├── build_avaliacao_01.py
│   ├── build_avaliacao_02.py
│   ├── build_common/
│   │   ├── __init__.py
│   │   ├── paths.py
│   │   ├── xlsx.py
│   │   ├── docx.py
│   │   ├── notebook.py
│   │   ├── package.py
│   │   └── validation.py
│   └── validate_all.py
├── target/
│   ├── avaliacao_01/
│   └── avaliacao_02/
├── tests/
│   ├── test_dictionary_sources.py
│   ├── test_notebook_clean.py
│   ├── test_build_avaliacao_01.py
│   └── test_build_avaliacao_02.py
├── .gitignore
├── README.md
└── requirements.txt
```

Essa árvore pode ser simplificada durante a implementação, mas os limites entre dados, fontes, templates, notebooks, scripts e outputs devem permanecer claros.

## 6. Estratégia para os relatórios das duas avaliações

### 6.1 Conteúdo compartilhado

Os seguintes arquivos devem concentrar conteúdo reutilizável:

- `sources/shared/introducao.md`;
- `sources/shared/objetivos.md`;
- `sources/shared/referencial_teorico.md`;
- `sources/shared/referencias.md`.

### 6.2 Relatório parcial

O relatório da Avaliação 1 será composto por:

1. capa e metadados institucionais;
2. introdução compartilhada;
3. objetivos compartilhados;
4. referencial teórico compartilhado;
5. referências compartilhadas.

O arquivo `sources/avaliacao_01/relatorio_parcial.md` pode funcionar como manifesto textual de composição ou conter o texto integral com diretivas de inclusão, conforme a tecnologia escolhida.

### 6.3 Relatório final

O relatório da Avaliação 2 será composto por:

1. capa e metadados institucionais;
2. introdução compartilhada;
3. objetivos compartilhados;
4. referencial teórico compartilhado;
5. metodologia específica;
6. resultados específicos;
7. discussão específica;
8. conclusão específica;
9. referências compartilhadas e referências adicionais da modelagem.

### 6.4 Evolução após feedback

O conteúdo compartilhado poderá evoluir após a Avaliação 1. A versão efetivamente entregue na primeira avaliação deve ser preservada por tag ou release, por exemplo:

```text
avaliacao-01-entrega
```

Não é necessário duplicar toda a árvore de fontes apenas para congelar a primeira versão.

## 7. Estratégia para os notebooks

### 7.1 Avaliação 1

O notebook da Avaliação 1 deve conter:

- leitura da base;
- auditoria;
- limpeza necessária;
- construção dos alvos;
- análises descritivas;
- gráficos;
- discussão preliminar.

### 7.2 Avaliação 2

O notebook da Avaliação 2 deve conter:

- preparação para modelagem;
- divisão temporal de treino e teste;
- transformação das variáveis;
- treinamento de diferentes algoritmos;
- otimização de hiperparâmetros;
- avaliação final;
- discussão crítica.

### 7.3 Política de versionamento

Os notebooks-fonte permanecem versionados em `.ipynb`, mas devem ser mantidos sem outputs persistidos.

Não será adotado Jupytext nesta issue, salvo se surgir uma necessidade concreta e se o ganho justificar a dependência adicional.

### 7.4 Preparação para entrega

O build deve copiar o notebook correspondente para `target/<avaliacao>/` e garantir:

- JSON válido;
- outputs vazios;
- `execution_count` nulo;
- ausência de caminhos absolutos locais;
- nome final correto.

O build não deve executar o notebook completo por padrão, pois a base é grande. A execução funcional deve ser um comando de validação explícito.

## 8. Fontes do dicionário

### 8.1 CSV da base bruta

`sources/dicionario/base_bruta.csv` deve documentar as colunas exatas da base entregue.

### 8.2 CSV das variáveis derivadas

`sources/dicionario/variaveis_derivadas.csv` deve documentar as variáveis criadas nos notebooks.

### 8.3 Esquema obrigatório

Ambos os arquivos devem conter exatamente estas colunas:

```text
Variável
Nome Descritivo
Tipo de Dado
Unidade de Medida
Domínio / Categoria
Descrição / Significado
Observações
```

O gerador deve rejeitar:

- cabeçalho ausente ou com grafia incorreta;
- variável vazia;
- variável duplicada dentro da mesma fonte;
- linha sem descrição;
- arquivo com codificação inválida;
- quantidade inesperada de colunas.

### 8.4 Excel gerado

O XLSX final deve possuir duas abas:

- `Base bruta`;
- `Variáveis derivadas`.

Ambas devem possuir:

- cabeçalho destacado;
- autofiltro;
- primeira linha congelada;
- quebra automática de texto;
- larguras coerentes;
- alturas ajustadas;
- bordas leves;
- ausência de texto truncado;
- revisão visual.

## 9. Template institucional do Word

### 9.1 Extração do template

O relatório DOCX atual contém conteúdo e elementos institucionais. A implementação deve criar um template limpo contendo apenas os componentes reutilizáveis necessários:

- tamanho e orientação de página;
- margens;
- cabeçalho;
- rodapé;
- logotipos;
- número de página;
- estilos tipográficos;
- estilos de títulos;
- estilo de corpo Times New Roman 12 justificado;
- estilos de listas e referências.

O template não deve conter conteúdo acadêmico obsoleto que possa sobreviver silenciosamente à geração.

### 9.2 Tecnologia de geração

A primeira alternativa a avaliar é Pandoc com `--reference-doc`.

O teste deve verificar se o resultado preserva corretamente:

- cabeçalho e rodapé;
- imagens;
- margens;
- paginação;
- estilos;
- listas;
- itálico;
- símbolos matemáticos;
- quebras de página.

Se a fidelidade for insuficiente, usar `python-docx` ou `docxtpl` com marcadores explícitos no template.

A decisão final deve ser registrada no README ou em comentário de arquitetura no código.

## 10. Interfaces de build

### 10.1 Build da Avaliação 1

```bash
python scripts/build_avaliacao_01.py
```

Saída esperada:

```text
target/avaliacao_01/
├── lucimar_nascimento.ipynb
├── dicionario_lucimar_nascimento.xlsx
├── base_lucimar_nascimento.zip
└── relatorio_parcial_lucimar_nascimento.docx
```

### 10.2 Build da Avaliação 2

```bash
python scripts/build_avaliacao_02.py
```

Saída futura esperada:

```text
target/avaliacao_02/
├── lucimar_nascimento_atividade_2.ipynb
└── relatorio_final_lucimar_nascimento.docx
```

O dicionário e a base poderão ser copiados para o pacote da Avaliação 2 apenas se a plataforma ou a equipe decidir incluí-los novamente. Eles não são exigidos como entregáveis da segunda avaliação segundo o enunciado atual.

### 10.3 Validação

```bash
python scripts/validate_all.py --avaliacao 1
python scripts/validate_all.py --avaliacao 2
```

Na conclusão da issue 1, a validação completa da Avaliação 1 deve existir. Para a Avaliação 2, basta existir a arquitetura e um comportamento claro informando que as fontes ainda não foram produzidas, se esse build for chamado prematuramente.

## 11. Comportamento do build

Cada build deve:

1. resolver a raiz do projeto de maneira independente do diretório de execução;
2. validar fontes e templates;
3. criar um diretório de saída novo ou limpar somente a saída da avaliação correspondente;
4. gerar o dicionário, quando aplicável;
5. gerar o relatório;
6. preparar e copiar o notebook;
7. copiar a base ou pacote de dados, quando aplicável;
8. validar os arquivos produzidos;
9. imprimir um resumo dos outputs e seus tamanhos;
10. terminar com código zero somente quando todas as etapas obrigatórias passarem.

O build não pode:

- apagar `target/` inteiro quando apenas uma avaliação está sendo gerada;
- modificar os arquivos-fonte;
- editar o notebook original para limpar outputs;
- baixar dependências ou dados silenciosamente;
- depender de caminhos absolutos do computador de um integrante;
- exigir edição manual dos outputs após sua conclusão.

## 12. Tratamento da base

A base é fonte de dados compartilhada e não deve ser regenerada a partir do dicionário ou do notebook.

A estrutura recomendada é:

```text
data/raw/base_lucimar_nascimento.zip
```

O build da Avaliação 1 deve:

- confirmar que o ZIP existe;
- verificar que ele contém exatamente o CSV esperado ou uma estrutura documentada;
- validar que o arquivo não está vazio;
- copiar o ZIP para a saída com o nome aprovado para submissão;
- não extrair permanentemente o CSV no repositório.

Deve-se confirmar com a plataforma da disciplina se um ZIP é aceito. Se não for, a estratégia de submissão da base deverá ser ajustada sem versionar uma segunda cópia desnecessária no repositório.

## 13. Dependências

O projeto deve declarar apenas as dependências necessárias.

Dependências candidatas:

- pandas;
- NumPy;
- Matplotlib;
- seaborn;
- openpyxl;
- python-docx ou docxtpl, se utilizados;
- Jupyter ou ipykernel;
- ferramenta de teste escolhida;
- Pandoc como dependência externa, se essa for a solução aprovada.

O README deve distinguir:

- pacotes Python instaláveis pelo gerenciador escolhido;
- ferramentas de sistema, como Pandoc;
- dependências necessárias apenas para desenvolvimento e validação.

## 14. Git e artefatos

### 14.1 Arquivos versionados

Devem ser versionados:

- fontes Markdown;
- fontes CSV do dicionário;
- notebooks limpos;
- scripts;
- testes;
- specs;
- README;
- template institucional;
- imagens e recursos necessários;
- base compactada, enquanto essa for a decisão de armazenamento do projeto.

### 14.2 Arquivos não versionados

Devem ser ignorados:

- `target/`;
- `.idea/`;
- `*.iml`;
- `.ipynb_checkpoints/`;
- `__pycache__/`;
- `.pytest_cache/`;
- ambientes virtuais;
- arquivos temporários;
- CSV extraído localmente da base;
- renders de validação;
- perfis temporários de ferramentas de escritório.

### 14.3 Preservação das entregas

A entrega efetiva pode ser preservada por:

- tag Git;
- GitHub Release;
- artefato de CI;
- pacote enviado à plataforma da disciplina.

Não é necessário commitar novamente os arquivos gerados na branch principal apenas para registrar a versão entregue.

## 15. Migração dos arquivos existentes

### 15.1 Dicionário

1. Extrair o conteúdo atual do XLSX.
2. Separar o que representa base bruta e o que representa variável derivada.
3. Salvar as fontes CSV em UTF-8 sem BOM.
4. Gerar um novo XLSX.
5. Comparar conteúdo e aparência.
6. Manter o XLSX antigo até a validação ser concluída.
7. Remover o binário antigo somente após aprovação do novo fluxo.

### 15.2 Relatório

1. Extrair o conteúdo atual para Markdown.
2. Preservar títulos, listas, ênfases, símbolos e referências.
3. Extrair ou criar o template institucional.
4. Gerar um novo DOCX.
5. Renderizar o antigo e o novo.
6. Comparar todas as páginas.
7. Corrigir perdas de fidelidade.
8. Manter o DOCX antigo até a validação ser concluída.
9. Remover o binário final antigo somente após aprovação.

### 15.3 Notebook

1. Mover para o diretório específico da Avaliação 1.
2. Preservar todo o conteúdo.
3. Limpar outputs somente na cópia gerada para `target` durante a primeira fase.
4. Definir posteriormente se o notebook-fonte também será permanentemente mantido limpo.

### 15.4 Base

1. Mover o ZIP para o diretório de dados.
2. Atualizar caminhos relativos.
3. Validar a leitura pelo notebook e pelo build.
4. Evitar nova compactação que altere desnecessariamente o arquivo antes da conferência.

## 16. Validações automatizadas

### 16.1 Fontes CSV

Validar:

- UTF-8;
- cabeçalho exato;
- sete colunas;
- variáveis únicas;
- campos obrigatórios preenchidos;
- ausência de linhas completamente vazias.

### 16.2 XLSX

Validar:

- arquivo abre sem erro;
- nomes e ordem das abas;
- cabeçalhos;
- quantidade de linhas;
- correspondência de valores com os CSVs;
- autofiltro;
- congelamento de linha;
- estilos básicos esperados;
- ausência de fórmulas ou erros inesperados.

### 16.3 Markdown

Validar:

- arquivos referenciados existem;
- seções obrigatórias existem;
- não há diretivas de inclusão não resolvidas;
- links internos e imagens locais existem;
- não há marcadores de template pendentes.

### 16.4 DOCX

Validar:

- arquivo abre sem erro;
- título e seções obrigatórias estão presentes;
- cabeçalho e rodapé existem, quando exigidos;
- estilos fundamentais existem;
- não há placeholders não substituídos;
- fontes e alinhamentos mínimos estão corretos;
- número de páginas é plausível.

### 16.5 Notebook

Validar na cópia final:

- JSON válido;
- células presentes;
- outputs vazios;
- `execution_count` nulo;
- ausência de caminho absoluto do workspace;
- ausência de dependência de scripts do projeto de POC;
- nome final correto.

### 16.6 Pacote

Validar:

- conjunto exato de arquivos obrigatórios;
- nomes corretos;
- arquivos não vazios;
- ausência de arquivos temporários;
- ausência de diretórios internos indevidos;
- resumo final legível.

## 17. Validação visual

### 17.1 Excel

Renderizar ou abrir todas as abas e conferir:

- conteúdo visível;
- ausência de `####`;
- cabeçalhos legíveis;
- quebras de texto adequadas;
- alturas e larguras coerentes;
- ausência de truncamento.

### 17.2 Word

Renderizar o DOCX em páginas e conferir todas elas:

- cabeçalho e rodapé;
- logotipos;
- margens;
- paginação;
- fonte;
- alinhamento;
- listas;
- símbolos;
- quebras de página;
- referências;
- ausência de cortes e sobreposições.

A inspeção visual pode permanecer manual nesta issue, mas o comando e o local dos renders devem ser documentados.

## 18. README

O README deve explicar:

- objetivo do repositório;
- relação entre Avaliação 1 e Avaliação 2;
- estrutura das fontes;
- arquivos compartilhados;
- arquivos específicos de cada avaliação;
- dependências;
- preparação do ambiente;
- build da Avaliação 1;
- build da Avaliação 2;
- validação;
- localização dos outputs;
- política de não editar `target/`;
- política de notebooks sem outputs;
- política de tags/releases;
- tratamento da base grande;
- limitações conhecidas.

## 19. Critérios de aceitação

### CA-01 — Fontes textuais criadas

O conteúdo editável do dicionário deve estar em CSVs versionados e o conteúdo editável do relatório parcial deve estar em Markdown versionado.

### CA-02 — Template separado

O template institucional deve existir separadamente do relatório final e não conter conteúdo acadêmico residual que possa aparecer no output.

### CA-03 — Build único da Avaliação 1

`python scripts/build_avaliacao_01.py` deve gerar todos os entregáveis da Avaliação 1 em `target/avaliacao_01/` a partir de um clone preparado conforme o README.

### CA-04 — Preparação para Avaliação 2

A arquitetura deve conter ponto de entrada e contratos claros para a Avaliação 2, sem exigir que o conteúdo final dessa avaliação seja implementado nesta issue.

### CA-05 — Lógica compartilhada

Os dois pontos de entrada não podem duplicar a implementação de geração de Word, validação de notebook, caminhos ou empacotamento.

### CA-06 — Outputs isolados

O build de uma avaliação não pode apagar ou sobrescrever outputs da outra.

### CA-07 — Excel gerado

O XLSX deve refletir integralmente os CSVs, possuir as abas esperadas, formatação legível, autofiltros e congelamento da primeira linha.

### CA-08 — Word gerado

O DOCX deve refletir integralmente o Markdown, preservar o template institucional e passar pela revisão visual de todas as páginas.

### CA-09 — Notebook preparado

O notebook em `target` deve estar sem outputs e sem contagens de execução, sem alterar destrutivamente o notebook-fonte durante o build.

### CA-10 — Base incluída

O pacote da Avaliação 1 deve conter ou referenciar corretamente a base exigida, conforme a decisão confirmada para a plataforma.

### CA-11 — Falha segura

O build deve terminar com erro quando faltar fonte, template, notebook ou base, ou quando uma validação estrutural obrigatória falhar.

### CA-12 — Sem edição manual

Nenhum entregável gerado deve exigir edição manual posterior para atingir o estado previsto pelo build.

### CA-13 — Git limpo

`target/`, arquivos de IDE, caches, checkpoints e temporários não devem ser versionados.

### CA-14 — Documentação suficiente

Uma pessoa sem conhecimento prévio do projeto deve conseguir instalar dependências e gerar a Avaliação 1 usando apenas o README.

### CA-15 — Migração segura

Os binários finais atuais só podem ser removidos depois que o conteúdo gerado tiver sido comparado e aprovado.

### CA-16 — Build repetível

Duas execuções sobre as mesmas fontes devem produzir conteúdo e estrutura equivalentes, ainda que metadados internos de DOCX ou XLSX impeçam igualdade byte a byte.

## 20. Testes mínimos

### 20.1 Testes positivos

- gerar a Avaliação 1 com todas as fontes válidas;
- abrir o XLSX gerado e comparar seus valores com os CSVs;
- abrir o DOCX gerado e localizar todas as seções;
- verificar o notebook limpo;
- executar o build duas vezes;
- executar o build a partir de diretório diferente da raiz.

### 20.2 Testes negativos

- remover temporariamente um CSV do dicionário;
- alterar um cabeçalho obrigatório;
- duplicar uma variável;
- remover o template;
- usar Markdown com inclusão inexistente;
- usar notebook inválido;
- remover a base;
- deixar placeholder não substituído.

Cada cenário deve produzir erro claro e não deixar um pacote final aparentemente válido.

## 21. Sequência de implementação

1. Criar a estrutura de diretórios e `.gitignore`.
2. Extrair o template institucional do DOCX atual.
3. Migrar o dicionário para CSVs.
4. Implementar geração e validação do XLSX.
5. Migrar o relatório para Markdown.
6. Fazer uma prova de conceito de geração do DOCX.
7. Escolher e consolidar a tecnologia de geração do Word.
8. Implementar preparação do notebook.
9. Implementar empacotamento da base.
10. Implementar `build_avaliacao_01.py`.
11. Criar a interface inicial de `build_avaliacao_02.py`.
12. Adicionar testes positivos e negativos.
13. Atualizar o README.
14. Executar comparação visual e estrutural.
15. Remover os binários finais antigos somente após aprovação.

## 22. Riscos e decisões pendentes

### 22.1 Fidelidade do Word

Pandoc pode não preservar todos os elementos do template. A tecnologia só será confirmada depois da renderização de um documento completo.

### 22.2 Conteúdo compartilhado e montagem

É necessário escolher entre:

- Markdown com diretivas de inclusão;
- manifesto JSON que ordena arquivos Markdown;
- script Python que concatena seções antes da conversão.

A montagem deve ser simples, explícita e fácil de depurar. Diretivas próprias complexas devem ser evitadas.

### 22.3 ZIP da base

Ainda é necessário confirmar se a plataforma aceita o CSV compactado.

### 22.4 Dependência do Pandoc

Se Pandoc for adotado, sua instalação e versão devem ser documentadas. Se isso dificultar a execução pela equipe, preferir solução inteiramente Python.

### 22.5 Nomes finais

Os nomes definitivos devem ser confirmados contra o enunciado e eventuais orientações da professora antes de codificá-los em testes rígidos.

### 22.6 Preservação do histórico

A remoção dos binários gerados do Git não elimina seu histórico. Deve-se evitar qualquer reescrita destrutiva de histórico nesta issue.

## 23. Definição de pronto

A issue estará concluída quando:

- a arquitetura unificada estiver implementada;
- as fontes CSV e Markdown forem a origem efetiva dos artefatos;
- o template institucional estiver separado;
- o build da Avaliação 1 produzir os quatro entregáveis;
- a estrutura para a Avaliação 2 estiver pronta sem duplicação de lógica;
- XLSX, DOCX e notebook passarem pelas validações definidas;
- todas as páginas do Word e todas as abas do Excel tiverem sido inspecionadas;
- o README documentar o processo completo;
- `target/` e temporários estiverem ignorados;
- os binários antigos tiverem sido preservados até a aprovação e removidos somente depois dela;
- a issue 6 puder ser executada alterando fontes versionáveis em vez de editar outputs binários.
