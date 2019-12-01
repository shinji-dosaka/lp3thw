from app import app

app.testing = True
web = app.test_client()

def test_index():
    rv = web.get('/', follow_redirects=True)
    assert rv.status_code == 404

    rv = web.get('/hello', follow_redirects=True)
    assert rv.status_code == 200
    assert "フォームに記入する" in rv.get_data(as_text=True)

    data = {'name': 'Zed', 'greet': 'こんにちは'}
    rv = web.post('/hello', follow_redirects=True, data=data)
    assert "Zed" in rv.get_data(as_text=True)
    assert "こんにちは" in rv.get_data(as_text=True)
