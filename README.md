# Projeto de previsão de atrasos de voos

Este repositório reúne os entregáveis das Avaliações 1 e 2 da disciplina de Introdução ao Machine Learning. O projeto analisa dados públicos de voos regulares da Agência Nacional de Aviação Civil e prepara uma tarefa de aprendizado supervisionado para classificação de faixas de atraso na partida.

## Integrantes

- Francisco Fonseca
- Lucimar Oliveira do Nascimento
- Osvaldo Souza

Lucimar Oliveira do Nascimento é a representante usada na padronização dos nomes dos entregáveis.

## Organização das avaliações

O projeto é unificado porque a Avaliação 2 evolui diretamente o trabalho iniciado na Avaliação 1. A base, o dicionário, a introdução, os objetivos, o referencial teórico e as referências são compartilhados sempre que mantêm a mesma semântica.

Cada avaliação possui notebook, fontes específicas, comando de build e diretório de saída próprios. A lógica de geração e validação fica em uma biblioteca comum para evitar duplicação.

```text
mcdia-ml-projeto-parcial/
├── data/
│   └── raw/                              # base compartilhada compactada
├── docs/
│   └── specs/                            # especificações das issues
├── notebooks/
│   ├── avaliacao_01/                     # exploração e análise preliminar
│   └── avaliacao_02/                     # modelagem e avaliação final
├── sources/
│   ├── shared/                           # introdução, objetivos, teoria e referências
│   ├── avaliacao_01/                     # capa e montagem do relatório parcial
│   ├── avaliacao_02/                     # metodologia, resultados, discussão e conclusão
│   └── dicionario/                       # fontes CSV do dicionário
├── templates/                            # template institucional do Word
├── scripts/
│   ├── build_avaliacao_01.py             # build completo da Avaliação 1
│   ├── build_avaliacao_02.py             # contrato do build da Avaliação 2
│   ├── validate_all.py                   # validação dos artefatos
│   └── build_common/                     # geração e validação compartilhadas
├── tests/                                # testes das fontes e dos geradores
└── target/                               # outputs locais, ignorados pelo Git
    ├── avaliacao_01/
    └── avaliacao_02/
```

Não edite arquivos dentro de `target/`. Eles são descartáveis e devem ser sempre regenerados a partir das fontes versionadas.

## Avaliação 1

A primeira avaliação entrega:

- notebook de análise exploratória;
- dicionário de dados em Excel;
- base consolidada;
- relatório parcial em Word.

As fontes do relatório são mantidas em Markdown. O dicionário é mantido em dois CSVs:

- `sources/dicionario/base_consolidada.csv` documenta as 25 colunas exatas da base entregue;
- `sources/dicionario/variaveis_analiticas.csv` documenta as 20 variáveis selecionadas ou produzidas pelo notebook.

O termo “base consolidada” é intencional: o arquivo reúne campos provenientes da fonte e campos produzidos na consolidação, portanto não equivale a um arquivo mensal bruto e intocado da ANAC.

O Word é gerado a partir do Markdown e de `templates/relatorio_institucional.docx`. O template preserva cabeçalho, rodapé, imagens, margens e identidade visual institucional.

## Avaliação 2

A segunda avaliação terá notebook e relatório final próprios. Ela acrescentará:

- divisão temporal em treino e teste;
- pré-processamento e transformação;
- construção e comparação de modelos;
- otimização de hiperparâmetros;
- avaliação final;
- metodologia, resultados, discussão e conclusão no relatório.

A infraestrutura já possui um ponto de entrada específico, mas o conteúdo e a modelagem ainda não foram implementados. Enquanto as fontes estiverem ausentes, o comando termina com uma mensagem explícita e código de saída `2`.

## Requisitos

- Python 3.11 ou superior;
- dependências listadas em `requirements.txt`;
- aplicação compatível com DOCX e XLSX para inspeção manual;
- LibreOffice ou Microsoft Word para conferência do relatório final.

Crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

No Windows, a ativação do ambiente normalmente é feita com:

```powershell
.venv\Scripts\Activate.ps1
```

## Gerar a Avaliação 1

Na raiz do repositório, execute:

```bash
python scripts/build_avaliacao_01.py
```

O comando pode ser chamado a partir de outro diretório porque os caminhos são resolvidos com base na localização dos scripts.

Arquivos produzidos:

```text
target/avaliacao_01/
├── lucimar_oliveira_do_nascimento.ipynb
├── dicionario_lucimar_oliveira_do_nascimento.xlsx
├── base_lucimar_oliveira_do_nascimento.zip
└── relatorio_parcial_lucimar_oliveira_do_nascimento.docx
```

O build:

1. valida as fontes CSV do dicionário;
2. gera e formata as duas abas do Excel;
3. resolve as inclusões Markdown do relatório;
4. gera o Word com o template institucional;
5. cria uma cópia limpa do notebook, sem outputs ou contagens de execução;
6. valida e copia a base compactada;
7. valida a estrutura dos quatro entregáveis.

O processo não executa o notebook completo automaticamente, pois essa etapa carrega aproximadamente dois milhões de registros e possui custo de memória e tempo distinto do build documental.

O notebook aceita deterministicamente a base oficial em CSV ou ZIP. Ele valida as 25 colunas esperadas, preserva identificadores como texto, audita ausências e duplicidades, contabiliza exclusões, compara o atraso recalculado com o campo existente e interrompe a execução se o esquema não for compatível. O alvo principal permanece a faixa de atraso na partida; atraso na chegada é tratado como outro problema de pesquisa.

## Gerar a Avaliação 2

Quando as fontes da modelagem estiverem disponíveis, o ponto de entrada será:

```bash
python scripts/build_avaliacao_02.py
```

No estado atual, o comando lista as fontes ainda pendentes e termina sem criar um pacote incompleto.

## Validar os entregáveis

Depois do build da primeira avaliação:

```bash
python scripts/validate_all.py --avaliacao 1
```

Para executar os testes unitários sem dependência adicional:

```bash
python -m unittest discover -s tests -v
```

As validações automatizadas não substituem a revisão visual. Antes da submissão:

1. abra as duas abas do Excel e verifique textos, larguras e quebras;
2. renderize ou abra o Word e confira todas as páginas;
3. execute o notebook com kernel reiniciado em um ambiente limpo;
4. confirme que o pacote contém somente os quatro arquivos esperados.

## Política para notebooks

Os notebooks-fonte são versionados em `.ipynb`. A cópia produzida para entrega contém:

- `outputs` vazios;
- `execution_count` nulo;
- nenhuma alteração destrutiva no notebook-fonte.

Antes da submissão, execute `Restart Kernel and Run All` em uma cópia de validação. Depois de confirmar a execução, gere novamente o pacote para obter o notebook final limpo.

## Base de dados

A base compartilhada está em:

```text
data/raw/base_lucimar_nascimento_v2.zip
```

O ZIP contém um único CSV consolidado. O build valida essa estrutura sem extrair permanentemente o arquivo de aproximadamente 685 MB.

É necessário confirmar se a plataforma da disciplina aceita a base compactada. Caso exija CSV não compactado, a estratégia de submissão deverá ser ajustada sem versionar uma segunda cópia no Git.

## Preservação das entregas

O diretório `target/` não é versionado. A versão efetivamente submetida deve ser preservada por um dos seguintes meios:

- tag Git, por exemplo `avaliacao-01-entrega`;
- GitHub Release;
- artefato de integração contínua;
- pacote enviado à plataforma da disciplina.

O conteúdo compartilhado pode evoluir após o feedback da primeira avaliação. A tag ou release permite recuperar exatamente a versão submetida sem duplicar a árvore do projeto.

## Especificações

- `docs/specs/spec_issue_1.md`: fontes versionáveis e geração dos entregáveis;
- `docs/specs/spec_issue_2.md`: incorporação das correções propostas pelo Lucimar;
- `docs/specs/sepc_issue_3.md`: revisão de conteúdo, qualidade dos dados e adequação completa da Avaliação 1.
