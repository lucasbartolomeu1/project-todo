from flask import Flask, jsonify
from app.database import db

def create_app(): 
    app = Flask(__name__) 
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tasks.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)


    @app.errorhandler(404)
    def not_found(e): 
        return jsonify({"message": "Recurso nao encontrado."}), 404

    with app.app_context(): 
        from app import models 
        db.create_all()

        from app.routes import bp as routes_bp 
        app.register_blueprint(routes_bp)

    return app 

