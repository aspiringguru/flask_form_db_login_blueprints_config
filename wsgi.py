from application import create_app

app = create_app()
#launches def create_app in application/__init__.py

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
