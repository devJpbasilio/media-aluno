# Fluxo do Programa: Cadastro de Aluno com Notas

## 1. Entrada de Dados
- Solicitar o **nome do aluno**.
- Solicitar as **notas dos 3 trimestres**:
  - Nota 1
  - Nota 2
  - Nota 3

## 2. Processamento
- Armazenar os dados em um **dicionário** com as chaves:
  - `nome`: Nome do aluno.
  - `notas`: Lista com as notas dos 3 trimestres.
  - `media`: Média calculada das notas.
    - Fórmula: 
      ```
      media = soma das notas / quantidade de notas
      ```

## 3. Saída de Dados
- Exibir os seguintes dados:
  - Nome do aluno.
  - Lista de notas.
  - Média (formatada com 2 casas decimais).
