## 1. Introdução

A infraestrutura de transporte aéreo desempenha um papel fulcral no desenvolvimento socioeconômico e na integração territorial do Brasil. No entanto, a pontualidade operacional dos voos comerciais regulares representa um dos principais desafios regulatórios e logísticos enfrentados pela administração pública setorial. Atrasos sistemáticos e não programados impõem severos custos de transação à economia nacional, geram ineficiências na alocação de slots em aeroportos saturados e acarretam prejuízos econômicos e desassistência aos usuários dos serviços de transporte público aéreo. Nesse cenário, o monitoramento preventivo e a capacidade preditiva estatal configuram instrumentos indispensáveis para aprimorar a fiscalização contratual e a formulação de intervenções regulatórias informadas por evidências.

Com a finalidade de mitigar essas falhas de coordenação e estruturar subsídios empíricos para a atuação regulatória, este projeto utiliza o microdado público de voos disponibilizado pela **Agência Nacional de Aviação Civil (ANAC)**, especificamente a base do sistema de **Voo Regular Ativo (VRA)**. O objetivo precípuo da utilização dessa base é desenvolver um modelo preditivo capaz de estimar antecipadamente — no momento do planejamento e autorização operacional do voo — a probabilidade de ocorrência e a magnitude de atrasos na partida dos voos que integram a malha aérea nacional. A pergunta central que orienta esta pesquisa é: *quais fatores operacionais, temporais, geográficos e concorrenciais (como rota, aeroporto de origem/destino, empresa aérea, horário programado e dia da semana) exercem maior influência sobre a degradação da pontualidade dos voos comerciais no Brasil?*

O problema de aprendizado supervisionado configura-se essencialmente como uma tarefa de classificação multiclasse/ordinal, admitindo como *benchmark* comparativo a formulação de classificação binária. A variável alvo principal (*target*) modelada é a faixa de atraso na partida (faixa_atraso_partida), uma variável categórica ordinal estruturada a partir do atraso líquido em minutos (atraso_partida_minutos), dividida em seis classes operacionais e regulatórias progressivas (FAIXAS de 0 a 5):

- **Faixa 0 — Pontual ou antecipado:** voos com partida no horário exato programado ou adiantada (≤ 0 min);

- **Faixa 1 — Atraso inferior a 15 min:** voos com partida após o horário previsto, porém dentro da margem internacional de tolerância operacional da aviação civil (0 < atraso < 15 min);

- **Faixa 2 — Atraso de 15 a 30 min:** atrasos iniciais acima do limiar de tolerância (15 ≤ atraso ≤ 30 min);

- **Faixa 3 — Atraso superior a 30 até 45 min:** atrasos moderados com potencial de impacto em conexões curtas (30 < atraso ≤ 45 min);

- **Faixa 4 — Atraso superior a 45 até 60 min:** atrasos intermediários próximos a uma hora (45 < atraso ≤ 60 min);

- **Faixa 5 — Atraso superior a 60 min:** atrasos severos e críticos (> 60 min), patamar a partir do qual se intensificam a degradação de *slots* na malha aérea e o escalonamento das obrigações regulatórias de assistência material previstas na Resolução ANAC nº 400.

Secundariamente, avalia-se a variável binária atraso_bi (1 para atrasos comerciais ≥ 15 minutos, englobando as faixas 2 a 5, e 0 para operações pontuais < 15 minutos, correspondentes às faixas 0 e 1).

A presente entrega preliminar está estruturada em quatro seções: esta introdução, a formulação dos objetivos gerais e específicos da pesquisa, a fundamentação teórica que contextualiza a regulação setorial e as técnicas de aprendizado supervisionado adotadas, e as respectivas referências bibliográficas formatadas sob as normas da ABNT.
