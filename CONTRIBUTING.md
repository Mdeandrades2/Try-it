# Configurando o Ambiente para Contribuição

Este guia o ajudará a configurar rapidamente o ambiente necessário para começar a contribuir com nosso projeto. Siga as etapas abaixo:

Pré-Requisitos

Antes de começar, você precisará:

Python: Certifique-se de ter o Python instalado. Se não, baixe e instale.
IDE: Recomendamos o Visual Studio Code (VS Code)
Versionamento: Uma ferramenta de versionamento é essencial. Recomendamos o Git Bash.

Configuração :

 1.Clone o Repositório:

   
Na sua IDE selecionada abra seu terminal e execute:
   git clone https://github.com/gabrielrroma/Tasty-FDS/tree/main

2.Abra o Projeto:
  
Abra a pasta em que você clonou o repositório.

3.Ambiente Virtual:

  
python -m venv venv
Isso cria uma pasta venv no seu diretório.

4.Ativação do Ambiente Virtual:

  
Ative o ambiente virtual com :
./venv/Scripts/Activate

5.Instalação de Dependências:
  
Instale as dependências necessárias:
pip install -r Tasty-FDS/requirements.txt
