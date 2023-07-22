# Desafio_Promaxima

Este é um projeto desenvolvido para o Desafio_Promaxima, uma aplicação web em Django para consulta de medicamentos através de uma API.

## Pré-requisitos:

Antes de executar o projeto, certifique-se de ter o Python (versão 3.8 ou superior) instalado em seu sistema.

Caso ainda não tenha o Django instalado, você pode instalá-lo usando o pip. Abra um terminal ou prompt de comando e execute o seguinte comando:

```
pip install Django
```

## Como Executar o Projeto Localmente

1. **Clone o Repositório:**

   Clone este repositório para o seu sistema local.

2. **Navegue para o Diretório do Projeto:**

   Acesse o diretório do projeto no terminal ou prompt de comando.

3. **Instale as Dependências:**

   Execute o seguinte comando para instalar as dependências do projeto:

   ```
   pip install -r requirements.txt
   ```

4. **Inicie o Servidor Django:**

   No diretório raiz do projeto (onde o arquivo `manage.py` está localizado), execute o seguinte comando para iniciar o servidor Django:

   ```
   python manage.py runserver
   ```

   O servidor será iniciado e o aplicativo estará disponível localmente.

5. **Acesse o Aplicativo:**

   Após iniciar o servidor, você poderá acessar o aplicativo em seu navegador digitando o seguinte endereço:

   ```
   http://localhost:8000/
   ```

## API de Consulta

A aplicação também oferece uma API de consulta de medicamentos. Você pode acessar a API no seguinte endereço:

```
http://localhost:8000/api/consulta/
```

## Observações

- Este projeto não requer um banco de dados, pois utiliza o banco de dados SQLite embutido do Django para fins de desenvolvimento.

- O Docker não é utilizado neste projeto, o que torna a execução simples e direta no ambiente local.

- Este projeto é apenas para fins educacionais e de demonstração. Se você planeja usá-lo em um ambiente de produção, considere implementar medidas adicionais de segurança e autenticação.

- Se você tiver outras dúvidas ou precisar de mais ajuda, fique à vontade para entrar em contato ou abrir uma issue no repositório. Boa sorte e divirta-se explorando a aplicação!
