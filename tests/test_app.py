from http import HTTPStatus


def test_read_root_deve_retornar_ok_e_ola_mundo(client):
    # client = TestClient(app)  --- arrange

    response = client.get('/')  # act chama a função que tem o endpoin '/'

    assert response.status_code == HTTPStatus.OK  # deu certo? ou '==200'assert
    assert response.json() == {'message': 'Olá Mundo!'}


def test_read_page_must_return_html(client):
    response = client.get('/ola')

    assert response.status_code == HTTPStatus.OK
    assert (
        response.text
        == """
    <html>
      <head>
        <title> Nosso olá mundo!</title>
      </head>
      <body>
        <h1> Olá Mundo </h1>
      </body>
    </html>
"""
    )
