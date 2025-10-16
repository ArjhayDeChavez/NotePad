from flask import Blueprint, render_template, request, redirect, url_for
from database import SessionLocal
from models import Note

note_routes = Blueprint('note_routes', __name__)
session = SessionLocal()

# Home page (show titles only)
@note_routes.route('/')
def index():
    query = request.args.get('q', '')
    if query:
        notes = session.query(Note).filter(
            (Note.title.contains(query)) | (Note.content.contains(query))
        ).order_by(Note.created_at.desc()).all()
    else:
        notes = session.query(Note).order_by(Note.created_at.desc()).all()
    return render_template('index.html', notes=notes, query=query)

# Read note
@note_routes.route('/note/<int:id>')
def read_note(id):
    note = session.query(Note).get(id)
    return render_template('read.html', note=note)

# Create note
@note_routes.route('/create', methods=['GET', 'POST'])
def create_note():
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        new_note = Note(title=title, content=content)
        session.add(new_note)
        session.commit()
        return redirect(url_for('note_routes.index'))
    return render_template('create.html')

# Edit note
@note_routes.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_note(id):
    note = session.query(Note).get(id)
    if request.method == 'POST':
        note.title = request.form['title']
        note.content = request.form['content']
        session.commit()
        return redirect(url_for('note_routes.read_note', id=note.id))
    return render_template('edit.html', note=note)

# Delete note
@note_routes.route('/delete/<int:id>')
def delete_note(id):
    note = session.query(Note).get(id)
    session.delete(note)
    session.commit()
    return redirect(url_for('note_routes.index'))