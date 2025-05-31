from app import app

def test_home():
    with app.test_client() as client:
        response = client.get('/')
        assert response.data.decode() == 'Selamat Datang di Kafe DevOps!'
        assert response.status_code == 200