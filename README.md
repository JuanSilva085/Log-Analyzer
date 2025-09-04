# Log Analyzer 
Este projeto implementa um analisador de arquivos de log em Python, detecta atividades suspeitas como acessos por pessoas não autorizadas, falhas de login.


## Funcionalidades

- Leitura de arquivos de log (ex.: auth.log, apache.log)
- Procura por padrões suspeitos ("Failed password", "Invalid user, "error", "unauthorized",)
- Conta as ocorrências de cada padrão
- Exporta resultados como 'arquivo CSV' para analisar