# Log Analyzer 
Este projeto implementa um analisador de arquivos de log em Python, detecta atividades suspeitas como acessos por pessoas não autorizadas, falhas de login.


## Funcionalidades

- Leitura de arquivos de log (ex.: auth.log, apache.log)
- Procura por padrões suspeitos ("Failed password", "Invalid user, "error", "unauthorized",)
- Conta as ocorrências de cada padrão
- Exporta resultados como 'arquivo CSV' para analisar

## Detalhes Técnicos

Leitura de logs: feita com open() e processamento linha a linha para suportar arquivos grandes.

Detecção de padrões: busca de termos como "Failed password", "error" e "unauthorized" usando comparação de strings

Exportação de resultados: realizada com a biblioteca padrão csv, gerando um relatório estruturado (resultados.csv).


## Referências / Documentação
Bibliotecas utilizadas:

csv → exportação de resultados

re → (opcional) expressões regulares para detecção avançada de padrões
