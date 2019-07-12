from app import create_app

app = create_app()

if __name__ == '__main__':
    from config import SERVER_HOST, SERVER_PORT
    app.run(host=SERVER_HOST, port=SERVER_PORT, debug=True)
