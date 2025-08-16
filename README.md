# PDF Translator - PDF em Inglês para TXT em Português

Esse projeto é um aplicativo simples feito em Python com interface que permite ao usuário:

1. Selecionar um arquivo **PDF em inglês**.
2. **Extrair o texto** do arquivo.
3. Traduzir automaticamente para o **português do Brasil**.
4. **Salvar o resultado em um arquivo `.txt`**.


## Funcionalidades

- Interface gráfica (Tkinter)
- Leitura de texto de arquivos PDF (`pdfplumber`)
- Tradução automática com **Google Translate** via `deep-translator`
- Exportação para `.txt`


## Interface do usuário

A interface é simples e intuitiva:

- Botão para selecionar o arquivo PDF
- Botão para iniciar a tradução
- Mensagens de erro e sucesso


## Instalação

Precisa ter o Python instalado (versão 3.7 ou superior).

```bash
pip install pdfplumber deep-translator
