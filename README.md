# Challenge 2 - FURIA
# Know Your Fan - Sistema de Perfil de Fã de Esports

Este é um sistema web para gerenciar perfis de fãs de esports, permitindo que os usuários preencham informações pessoais, conectem redes sociais, validem documentos e vinculem perfis em plataformas de esports.

## Pré-requisitos

Antes de iniciar a aplicação, certifique-se de ter os seguintes itens instalados:

- Python 3.9 ou superior
- Pip (gerenciador de pacotes do Python)
- Ambiente virtual (opcional, mas recomendado)

## Instalação

1. Clone este repositório ou baixe os arquivos do projeto.

2. Navegue até o diretório do projeto:

   ```bash
   cd caminho/para/o/projeto
   ```
3. Crie um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   ```
4. Ative o ambiente virtual:

   - No Windows:

	 ```bash
	 venv\Scripts\activate
	 ```

   - No macOS/Linux:

	 ```bash
	 source venv/bin/activate
	 ```
5. Instale as dependências listadas no arquivo requirements.txt:

   ```bash
   pip install -r requirements.txt
   ```
6. Certifique-se de que o arquivo config.py contém as configurações corretas para o ambiente de desenvolvimento. Por padrão, ele já está configurado para uso local.

7. Certifique-se de que a pasta uploads existe no diretório do projeto. Caso contrário, crie-a manualmente:

   ```bash
   mkdir uploads
   ```
## Executando a Aplicação	

1. Inicie o servidor Flask:

   ```bash
   python app.py
   ```
2. Acesse a aplicação no navegador em: http://127.0.0.1:5000 (ou outro endereço que será mostrado no seu terminal)



## Funcionalidades
1. Página Inicial
Acesse a página inicial para começar o cadastro clicando no botão "Começar".
2. Perfil
Preencha suas informações pessoais, como nome, email, CPF, endereço e interesses em esports.
3. Documentos
Envie uma foto do seu documento de identificação para verificação.
4. Redes Sociais
Conecte suas redes sociais (Twitter, Facebook, Instagram, Twitch) para análise de interesses.
5. Esports
Vincule seus perfis em plataformas de esports, como FURIA, FaceIT, Steam, entre outras.
6. Resumo
Visualize um resumo completo do seu perfil, incluindo informações pessoais, redes sociais conectadas e validações realizadas.
Estrutura do Projeto
  - app.py: Arquivo principal que contém as rotas e lógica da aplicação.
  - config.py: Configurações da aplicação, como chaves secretas e limites de upload.
  - templates: Arquivos HTML para renderização das páginas.
  - static: Arquivos estáticos, como CSS, JavaScript e imagens.
  - utils: Funções auxiliares para validação de documentos, redes sociais e perfis de esports.
