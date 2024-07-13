# Currículo Automático com Python e FPDF

Este projeto cria um currículo profissional em formato PDF utilizando Python e a biblioteca FPDF. A partir de informações fornecidas, o script gera um currículo formatado com seções distintas, cabeçalho e rodapé personalizados, e elementos visuais como separadores e bordas.

## Funcionalidades

- Geração de currículo em PDF com formatação profissional.
- Inclusão de foto de perfil com borda.
- Cabeçalho e rodapé personalizados.
- Seções distintas para contato, objetivo profissional, resumo, experiência profissional, formação acadêmica, certificações, idiomas e projetos.
- Separadores visuais para melhorar a organização.
- Suporte para múltiplos idiomas (exemplo disponível em português e inglês).

## Estrutura do Projeto

O projeto consiste em um script Python principal (`curriculo.py`) que contém toda a lógica para gerar o currículo em PDF. As informações são organizadas em dicionários e listas para fácil manipulação e formatação.

### Arquivos

- `curriculo.py`: Script principal que gera o currículo em PDF.
- `pfp.jfif`: Imagem de perfil utilizada no cabeçalho do currículo.

## Como Usar

1. Clone este repositório em sua máquina local:
    ```sh
    git clone https://github.com/seu-usuario/curriculo-automatico.git
    ```
2. Instale as dependências necessárias:
    ```sh
    pip install fpdf pillow
    ```
3. Execute o script para gerar o PDF:
    ```sh
    python curriculo.py
    ```
