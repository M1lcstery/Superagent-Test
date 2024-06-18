import threading
import server

def main():
    app = server.create_app()
    threading.Thread(target=server.run_ngrok).start() 
    app.run(port=5000)

if __name__ == '__main__':
    main()
