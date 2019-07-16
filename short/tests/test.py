from config import config_by_name


def test_test_config(app):
    test_config = config_by_name['test']
    app.config.from_object(test_config)
    assert app.config['DEBUG']
    assert app.config['TESTING']


def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {'ok': 'ok'}


def test_get_emtpy_urls(client):
    response = client.get('/urls')
    assert response.status_code == 200
    assert response.json == {'urls': []}


