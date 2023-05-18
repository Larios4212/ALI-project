from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(UserMixin, db.Model):
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(255), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    documents = db.relationship('Document', backref='user', lazy=True)

class Document(db.Model):
    document_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.user_id'), nullable=False)
    document_name = db.Column(db.String(255), nullable=False)
    document_type = db.Column(db.String(255), nullable=False)
    document_content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    analysis_results = db.relationship('AnalysisResult', backref='document', lazy=True)

class AnalysisResult(db.Model):
    result_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    document_id = db.Column(db.Integer, db.ForeignKey('document.document_id'), nullable=False)
    improvement_areas = db.Column(db.Text, nullable=False)
    strengths = db.Column(db.Text, nullable=False)
    analyzed_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    recommended_resources = db.relationship('RecommendedResource', backref='analysis_result', lazy=True)

class RecommendedResource(db.Model):
    recommendation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    result_id = db.Column(db.Integer, db.ForeignKey('analysis_result.result_id'), nullable=False)
    resource_name = db.Column(db.String(255), nullable=False)
    resource_url = db.Column(db.String(2048), nullable=False)
    resource_type = db.Column(db.String(255), nullable=False)
    
from app import db
