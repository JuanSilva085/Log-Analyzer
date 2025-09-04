import re
import csv

#função para ler o arquivo de logs
def leitura_logs(caminho_arquivo):
    with open(caminho_arquivo, 'r', encoding='utf-8') as arquivo:
       linhas = arquivo.readlines()
    return linhas 


#análise de logs para detectar padrões suspeitos
def analisar_logs(linhas):
  padrao_log = ["Failed password", "Invalid user", "error", "unauthorized"]
  resultados = {}

  for linha in linhas:
     for padrao in padrao_log:
        if padrao.lower() in linha.lower():
           if padrao not in resultados:
              resultados[padrao] = 0
           resultados[padrao] += 1
  return resultados

#função para salvar os resultados em um arquivo CSV
def salvar_resultados_csv(resultados, caminho_csv = 'resultados_logs.csv'):
    with open(caminho_csv, 'w', newline='') as csvfile:
       writter = csv.writer(csvfile)
       writter.writerow(['Padrão', 'Ocorrências'])
       for padrao, ocorrencias in resultados.items():
            writter.writerow([padrao, ocorrencias])

#função principal
if __name__ == "__main__":
    caminho_arquivos_logs = "logs/auth.log" 
    linhas_logs = leitura_logs(caminho_arquivos_logs)
    resultados = analisar_logs(linhas_logs)

    print("Resultados da Análise de Logs: ")
    for padrao, ocorrencias in resultados.items():
        print(f"{padrao}: {ocorrencias} ocorrências")

    salvar_resultados_csv(resultados)
    print("Resultados estão no 'resultados_logs.csv'")