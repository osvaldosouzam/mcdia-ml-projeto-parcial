# Projeto de previsão de atrasos de voos

Este repositório reúne os entregáveis das Avaliações 1 e 2 da disciplina de Introdução ao Machine Learning. O projeto analisa dados públicos de voos regulares da Agência Nacional de Aviação Civil e prepara uma tarefa de aprendizado supervisionado para classificação de faixas de atraso na partida.

## Integrantes

- Francisco Alberto Fonseca Neto
- Lucimar Oliveira do Nascimento
- Osvaldo Souza Menezes Júnior

Lucimar Oliveira do Nascimento é a representante usada na padronização dos nomes dos entregáveis.

## Organização das avaliações

O projeto é unificado porque a Avaliação 2 evolui diretamente o trabalho iniciado na Avaliação 1. A base, o dicionário, a introdução, os objetivos, o referencial teórico e as referências são compartilhados sempre que mantêm a mesma semântica.

Cada avaliação possui notebook, fontes específicas, comando de build e diretório de saída próprios. A lógica de geração e validação fica em uma biblioteca comum para evitar duplicação.

```text
mcdia-ml-projeto-parcial/
├── README.md                             # instruções de preparação, execução e entrega
├── requirements.txt                     # dependências Python do projeto
├── avaliacao-01.txt                      # enunciado da primeira avaliação
├── avaliacao-02.txt                      # enunciado da segunda avaliação
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
└── target/                               # snapshots gerados; ZIP e validações locais são ignorados
    ├── avaliacao_01/
    └── avaliacao_02/
```

Não edite arquivos dentro de `target/`. Eles devem ser sempre regenerados a partir das fontes versionadas. O notebook limpo, o dicionário XLSX e o relatório DOCX são versionados como snapshots da entrega; o ZIP copiado para a entrega e os arquivos locais de validação permanecem ignorados.

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

## Preparar o ambiente

- Python 3.11 ou superior;
- dependências listadas em `requirements.txt`;
- aplicação compatível com DOCX e XLSX para inspeção manual;
- LibreOffice ou Microsoft Word para conferência do relatório final.

Execute os comandos a partir da raiz do repositório, isto é, do diretório que contém `requirements.txt`.

### Linux ou macOS com ambiente virtual

Crie e ative um ambiente virtual e instale as dependências:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

### Windows com ambiente virtual

No PowerShell, crie e ative o ambiente com:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Se a política do PowerShell impedir a ativação, libere scripts somente para a sessão atual e tente novamente:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.venv\Scripts\Activate.ps1
```

### Windows com Anaconda

Abra o **Anaconda Prompt**, entre na raiz do repositório e execute:

```powershell
conda create --name mcdia-ml python=3.11 -y
conda activate mcdia-ml
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

O uso de `python -m pip` e `python -m jupyter` ajuda a garantir que os comandos utilizem o mesmo interpretador do ambiente ativo.

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

### Alterar e gerar cada entregável da Avaliação 1

Os quatro arquivos são sempre gerados em conjunto pelo mesmo comando:

```bash
python scripts/build_avaliacao_01.py
```

Esse comando recria `target/avaliacao_01/` desde o início. Portanto, não mantenha alterações manuais nesse diretório: elas serão descartadas no próximo build. Depois de revisar o resultado, inclua no commit os três snapshots versionados — notebook, XLSX e DOCX — quando a alteração fizer parte de uma nova versão da entrega.

#### Notebook de análise exploratória

Edite o notebook-fonte:

```text
notebooks/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb
```

Depois da alteração, gere a cópia limpa destinada à entrega:

```bash
python scripts/build_avaliacao_01.py
```

Arquivo gerado:

```text
target/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb
```

Para abrir exatamente essa cópia no JupyterLab:

```bash
python -m jupyter lab target/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb
```

O build remove outputs e contagens de execução somente da cópia em `target/`; o notebook-fonte não é alterado.

#### Dicionário de dados em Excel

Edite os CSVs que representam as duas abas do arquivo:

```text
sources/dicionario/base_consolidada.csv
sources/dicionario/variaveis_analiticas.csv
```

O primeiro documenta as colunas do CSV consolidado. O segundo documenta o conjunto de variáveis usado ou produzido pela análise. Depois da alteração, execute:

```bash
python scripts/build_avaliacao_01.py
```

Arquivo gerado:

```text
target/avaliacao_01/dicionario_lucimar_oliveira_do_nascimento.xlsx
```

Abra o arquivo gerado no Microsoft Excel ou LibreOffice Calc e confira as duas abas. Em Linux, se o LibreOffice estiver instalado, ele pode ser aberto pela linha de comando:

```bash
libreoffice target/avaliacao_01/dicionario_lucimar_oliveira_do_nascimento.xlsx
```

No Windows, o arquivo pode ser aberto no aplicativo associado com:

```powershell
Start-Process target\avaliacao_01\dicionario_lucimar_oliveira_do_nascimento.xlsx
```

#### Base consolidada compactada

A base versionada que deve ser substituída quando houver uma nova consolidação é:

```text
data/raw/base_lucimar_nascimento_v2.zip
```

O ZIP deve conter exatamente um CSV não vazio. Alterações nas colunas desse CSV também devem ser refletidas em `sources/dicionario/base_consolidada.csv` e, quando aplicável, no notebook e no dicionário analítico. Depois de substituir a base, execute:

```bash
python scripts/build_avaliacao_01.py
```

Arquivo validado, copiado e renomeado para a entrega:

```text
target/avaliacao_01/base_lucimar_oliveira_do_nascimento.zip
```

Para conferir o conteúdo do ZIP sem extraí-lo:

```bash
python -m zipfile -l target/avaliacao_01/base_lucimar_oliveira_do_nascimento.zip
```

#### Relatório parcial em Word

O arquivo que define a ordem e a composição do relatório é:

```text
sources/avaliacao_01/relatorio_parcial.md
```

Normalmente, o conteúdo deve ser alterado nos arquivos incluídos por ele:

```text
sources/avaliacao_01/capa.md
sources/shared/introducao.md
sources/shared/objetivos.md
sources/shared/referencial_teorico.md
sources/shared/referencias.md
```

O arquivo `templates/relatorio_institucional.docx` deve ser alterado somente quando for necessário mudar estilos, margens, cabeçalho, rodapé ou elementos visuais do documento. Depois da alteração, execute:

```bash
python scripts/build_avaliacao_01.py
```

Arquivo gerado:

```text
target/avaliacao_01/relatorio_parcial_lucimar_oliveira_do_nascimento.docx
```

Abra o documento no Microsoft Word ou LibreOffice Writer e confira todas as páginas. Em Linux, se o LibreOffice estiver instalado, use:

```bash
libreoffice target/avaliacao_01/relatorio_parcial_lucimar_oliveira_do_nascimento.docx
```

No Windows, use o aplicativo associado ao formato DOCX:

```powershell
Start-Process target\avaliacao_01\relatorio_parcial_lucimar_oliveira_do_nascimento.docx
```

O processo não executa o notebook completo automaticamente, pois essa etapa carrega aproximadamente dois milhões de registros e possui custo de memória e tempo distinto do build documental.

O notebook aceita deterministicamente a base oficial em CSV ou ZIP. Ele valida as 25 colunas esperadas, preserva identificadores como texto, audita ausências e duplicidades, contabiliza exclusões, compara o atraso recalculado com o campo existente e interrompe a execução se o esquema não for compatível. O alvo principal permanece a faixa de atraso na partida; atraso na chegada é tratado como outro problema de pesquisa.

Além da distribuição do alvo, o notebook apresenta auditorias de tipos, domínios, duplicidades por proveniência e chave natural, conversões temporais, extremos e reconciliação da população. A exploração inclui mês, hora prevista, companhia, aeroportos e rotas, sempre com denominadores e linguagem descritiva.

## Executar o notebook com Jupyter

Com o ambiente ativado e a partir da raiz do repositório, inicie o JupyterLab:

```bash
python -m jupyter lab
```

Se preferir a interface clássica, execute:

```bash
python -m jupyter notebook
```

No navegador:

1. para desenvolver ou revisar a análise, abra `notebooks/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb`;
2. confirme que o kernel selecionado pertence ao ambiente no qual `requirements.txt` foi instalado;
3. escolha **Restart Kernel and Run All Cells** — ou a opção equivalente da interface;
4. confira se todas as células terminam sem erro e se tabelas e gráficos são exibidos.

Para validar exatamente a cópia destinada à entrega, primeiro execute `python scripts/build_avaliacao_01.py` e depois abra `target/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb`. Essa cópia fica ao lado do ZIP esperado pelo notebook.

No Windows com Anaconda, o fluxo completo no **Anaconda Prompt** é:

```powershell
conda activate mcdia-ml
python scripts\build_avaliacao_01.py
python -m jupyter lab
```

Depois, abra no JupyterLab o notebook em `target/avaliacao_01` e execute todas as células. Os caminhos internos do projeto são resolvidos de forma independente do separador usado pelo sistema operacional.

### Execução automatizada para validação

Depois de gerar a Avaliação 1, crie uma área de validação ignorada pelo Git e execute a cópia do pacote ao lado do ZIP:

```bash
mkdir -p target/validation
python -m jupyter nbconvert \
  --to notebook \
  --execute target/avaliacao_01/lucimar_oliveira_do_nascimento.ipynb \
  --output-dir target/validation \
  --output lucimar_oliveira_do_nascimento_executado.ipynb \
  --ExecutePreprocessor.timeout=1200
```

No PowerShell — inclusive no **Anaconda PowerShell Prompt** — o comando equivalente é:

```powershell
New-Item -ItemType Directory -Force target\validation | Out-Null
python -m jupyter nbconvert `
  --to notebook `
  --execute target\avaliacao_01\lucimar_oliveira_do_nascimento.ipynb `
  --output-dir target\validation `
  --output lucimar_oliveira_do_nascimento_executado.ipynb `
  --ExecutePreprocessor.timeout=1200
```

O arquivo executado serve apenas como evidência local. Não o copie para o pacote nem o versione. Após a conferência, execute novamente `python scripts/build_avaliacao_01.py` para garantir que o notebook destinado à submissão permaneça sem outputs.

### Ambiente e consumo observados

A validação integral mais recente usou:

- Python 3.14.3;
- NumPy 2.5.3;
- pandas 3.0.6;
- Matplotlib 3.11.2;
- seaborn 0.13.2;
- base com 1.992.832 registros e 25 colunas.

Nesse ambiente, a execução completa levou aproximadamente 21 segundos e atingiu cerca de 2,5 GB de memória residente. Recomenda-se manter ao menos 4 GB de memória disponível para o processo. Esses valores são referências observadas e podem variar conforme sistema operacional, armazenamento e versões compatíveis instaladas por `requirements.txt`.

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

Em `target/`, o notebook limpo, o dicionário XLSX e o relatório DOCX são versionados. A cópia renomeada da base em ZIP não é versionada porque duplica a base de `data/raw/`, e `target/validation/` permanece reservado a evidências locais de execução.

A versão efetivamente submetida deve ser identificada por um dos seguintes meios:

- tag Git, por exemplo `avaliacao-01-entrega`;
- GitHub Release;
- artefato de integração contínua;
- pacote enviado à plataforma da disciplina.

O conteúdo compartilhado pode evoluir após o feedback da primeira avaliação. A tag ou release permite recuperar exatamente os três snapshots versionados da entrega; a base correspondente continua disponível pelo arquivo versionado em `data/raw/`.

## Especificações

- `docs/specs/spec_issue_1.md`: fontes versionáveis e geração dos entregáveis;
- `docs/specs/spec_issue_2.md`: incorporação das correções propostas pelo Lucimar;
- `docs/specs/spec_issue_6.md`: revisão de conteúdo, qualidade dos dados e adequação completa da Avaliação 1.
