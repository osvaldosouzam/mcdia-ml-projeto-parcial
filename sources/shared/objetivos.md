## 2. Objetivos

### 2.1 Objetivo Geral

Desenvolver, validar e comparar modelos preditivos baseados em algoritmos de aprendizado de máquina supervisionado para a classificação de faixas de atraso de voos comerciais regulares no Brasil, a partir dos microdados públicos da ANAC, gerando insumos analíticos para a governança regulatória e a mitigação de ineficiências na malha aeroviária nacional.

### 2.2 Objetivo Específicos

Para alcançar o objetivo geral proposto, definem-se as seguintes metas específicas:

- **Executar a análise exploratória e descritiva dos microdados do VRA/ANAC:** mensurar medidas de posição, dispersão e assimetria do tempo de atraso, bem como mapear a distribuição de frequência entre as classes e investigar o desbalanceamento intrínseco aos atrasos aéreos graves;

- **Estruturar um pipeline robusto de auditoria, limpeza e pré-processamento de dados:** tratar inconsistências de calendário, isolar voos cancelados/desviados e aplicar técnicas de codificação categórica de alta cardinalidade (*Target **Encoding* com regularização para aeroportos e rotas) evitando vazamento de dados (*data **leakage*);

- **Implementar e comparar modelos supervisionados de classificação ****multiclasse****:** treinar modelos baselines (regressão logística e classificadores dummy) e algoritmos avançados baseados em árvores e *gradient** **boosting* (HistGradientBoosting, Random Forest), avaliando-os por meio de métricas resilientes ao desbalanceamento, tais como Balanced Accuracy, F1-Score Macro e Matriz de Confusão;

- **Avaliar a capacidade de generalização temporal:** submeter a arquitetura analítica à validação temporal progressiva (treinamento na série histórica e teste em períodos subsequentes), assegurando aderência à realidade estocástica e operacional da malha aérea brasileira.
