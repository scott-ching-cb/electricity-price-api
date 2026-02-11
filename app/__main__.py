from app.presentation.__main__ import create_app


def start_server():
    app = create_app()
    app.run(host = "127.0.0.1", port = 5000, debug = False)


if __name__ == "__main__":
    start_server()
