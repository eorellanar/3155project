def load_routes(app):
    @app.get("/")
    def read_root():
        return {"message": "Welcome to the API"}