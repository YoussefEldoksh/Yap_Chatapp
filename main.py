from Backend import create_app

app = create_app()

if __name__ == '__main__': #this says that only if we run this file not import it run what's inside
    app.run(host='0.0.0.0', port=5000, debug=True)

# this is the entry point to the website