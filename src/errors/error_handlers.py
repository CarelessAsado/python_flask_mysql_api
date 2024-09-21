
from src.db.connect import db
from flask import jsonify
from sqlalchemy import exc

def registerErrorHandlers(app):
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()  
        return jsonify({"errorHandler": str(error)}), 500
    

    @app.errorhandler(exc.SQLAlchemyError)
    def handle_db_exceptions(error):
        #log the error: app.logger.error(error)
        db.session.rollback()
        return jsonify({"errorHandler": str(error)}), 500

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({"errorHandler": str(error)}), 400