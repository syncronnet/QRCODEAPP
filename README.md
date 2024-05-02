# QRCodeApp 📱

## Descrição
Este é um projeto de aplicativo para geração de códigos QR, desenvolvido utilizando Django.

## Tecnologias Utilizadas 🛠️
- Django 5.0.4
- Gunicorn 22.0.0
- QRCode 7.4.2
- wfastcgi 3.0.0
- Outras dependências podem ser encontradas no arquivo requirements.txt

## Funcionalidades ✨
- Geração de códigos QR a partir de texto inserido pelo usuário.
- Visualização dos códigos QR gerados.
- Download dos códigos QR em formato de imagem.

## Requisitos do Sistema 💻
- Python 3.x
- Django 5.0.4
- Outras dependências estão listadas no arquivo requirements.txt

## Configuração do Ambiente ⚙️
1. Clone o repositório para o seu ambiente local.
2. Instale as dependências utilizando o comando:
pip install -r requirements.txt
3. Execute as migrações do banco de dados:
python manage.py makemigrations
python manage.py migrate
4. Inicie o servidor local:
python manage.py runserver 0.0.0.0:8000
5. Acesse o aplicativo em seu navegador: http://localhost:8000

## Deploy 🚀
Este projeto pode ser facilmente implantado em um servidor web. Recomenda-se o uso do IIS com wfastcgi para hospedar a aplicação.

## Contribuindo 🤝
Contribuições são bem-vindas! Por favor, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Autores ✍️
- Moisés Sousa


## Licença 📝
Este projeto é licenciado sob a Licença GPL-3.0. Consulte o arquivo LICENSE.md para obter mais detalhes.


