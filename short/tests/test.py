

def test_ping(client):
    response = client.get('/ping')
    assert response.status_code == 200
    assert response.json == {'ok': 'ok'}


def test_get_urls(client):
    response = client.get('/urls')
    assert response.status_code == 200
    assert list(response.json.keys()) == ['urls']


def test_create_short_urls(client):
    response = client.post('/urls', data=dict())
    assert response.status_code == 200
