from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from transformers import pipeline

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///notes.db'
db = SQLAlchemy(app)

# Load AI model once
summarizer = pipeline("summarization", model="facebook/bart-large-cnn", use_safetensors=True)

# Database model
class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)

# Initialize database
with app.app_context():
    db.create_all()

# --- CRUD Routes ---

# Create a new note
@app.route('/notes', methods=['POST'])
def create_note():
    data = request.get_json()
    note = Note(content=data['content'])
    db.session.add(note)
    db.session.commit()
    return jsonify({'id': note.id, 'content': note.content}), 201

# Read all notes
@app.route('/notes', methods=['GET'])
def get_notes():
    notes = Note.query.all()
    return jsonify([{'id': n.id, 'content': n.content} for n in notes])

# Read one note
@app.route('/notes/<int:note_id>', methods=['GET'])
def get_note(note_id):
    note = Note.query.get_or_404(note_id)
    return jsonify({'id': note.id, 'content': note.content})

# Update a note
@app.route('/notes/<int:note_id>', methods=['PUT'])
def update_note(note_id):
    note = Note.query.get_or_404(note_id)
    data = request.get_json()
    note.content = data['content']
    db.session.commit()
    return jsonify({'id': note.id, 'content': note.content})

# Delete a note
@app.route('/notes/<int:note_id>', methods=['DELETE'])
def delete_note(note_id):
    note = Note.query.get_or_404(note_id)
    db.session.delete(note)
    db.session.commit()
    return jsonify({'message': 'Note deleted'})

# --- AI Route ---

# Summarize a note using Hugging Face model
@app.route('/notes/<int:note_id>/summarize', methods=['POST'])
def summarize_note(note_id):
    note = Note.query.get_or_404(note_id)
    summary = summarizer(note.content, max_length=50, min_length=10, do_sample=False)[0]['summary_text']
    return jsonify({'summary': summary})

# Run the server
if __name__ == '__main__':
    app.run(debug=True)
