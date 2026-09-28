## 1. Introdução

A pontualidade do transporte aéreo interessa aos passageiros, às empresas e à administração pública responsável pelo acompanhamento do setor. A análise de registros de voos pode apoiar o diagnóstico de padrões de atraso e a identificação de limitações dos dados utilizados nesse monitoramento. Neste projeto acadêmico, pretende-se estudar a possibilidade de classificação antecipada do atraso na partida, sem pressupor que uma previsão permita identificar suas causas ou, por si só, orientar uma intervenção regulatória.

A fonte é o conjunto Voo Regular Ativo (VRA), disponibilizado pela Agência Nacional de Aviação Civil (ANAC, s.d.). O recorte adotado compreende 2024 e 2025 e utiliza o arquivo consolidado base_lucimar_nascimento_v2.csv. Esse arquivo é a entrada preservada do estudo e já reúne campos de origem e campos derivados; não deve ser confundido com cada arquivo mensal original da ANAC. A unidade observacional é o registro de uma etapa de voo. A base inclui registros de empresas e aeroportos estrangeiros, de modo que seu conteúdo não se restringe a voos domésticos.

A pergunta orientadora é: “**E****m que medida informações disponíveis antes da partida, como companhia aérea, aeroportos de origem e destino, rota e horário programado, permitem prever a faixa de atraso na partida dos voos realizados no recorte VRA/ANAC de 2024 e 2025?**” Nesta primeira atividade, o trabalho define o problema, examina a base e estabelece os cuidados necessários à etapa preditiva.

O alvo principal é codigo_faixa_atraso, uma variável categórica ordinal com seis classes. Sua descrição textual é faixa_atraso_partida. Ambas derivam de atraso_partida_minutos, calculado como a diferença, em minutos, entre partida real e partida prevista. Valores negativos representam antecipação. As faixas são escolhas analíticas do projeto, definidas da seguinte forma:

- 0 — Pontual ou antecipado: atraso menor ou igual a zero minuto.

- 1 — Atraso inferior a 15 minutos: atraso maior que zero e menor que 15 minutos.

- 2 — Atraso de 15 a 30 minutos: atraso maior ou igual a 15 e menor ou igual a 30 minutos.

- 3 — Atraso superior a 30 até 45 minutos: atraso maior que 30 e menor ou igual a 45 minutos.

- 4 — Atraso superior a 45 até 60 minutos: atraso maior que 45 e menor ou igual a 60 minutos.

- 5 — Atraso superior a 60 minutos: atraso maior que 60 minutos.

O indicador secundário atraso_bi vale 1 quando o atraso é de pelo menos 15 minutos e 0 quando é inferior a 15 minutos, incluindo antecipações. Ele resume as faixas 2 a 5 e permite descrições complementares; o problema principal permanece a classificação em seis faixas. Os limites definidos aqui não são apresentados como categorias regulatórias nem como regra automática de assistência ao passageiro.

A análise do alvo considera voos realizados com datas de partida utilizáveis. Cancelamentos e registros sem elementos necessários ao cálculo são contabilizados na auditoria de exclusões. O CSV de entrada permanece intacto, e as transformações são realizadas em memória pelo notebook. Valores extremos exigem inspeção dos registros e da origem das datas antes de qualquer exclusão adicional. O relatório organiza-se nesta introdução, nos objetivos, no referencial teórico e nas referências; as tabelas, os gráficos e a auditoria constam do notebook.
