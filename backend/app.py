from flask import Flask, render_template,request, url_for, abort, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:TIMMY@localhost:5432/joint'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db= SQLAlchemy(app)

class Todo(db.Model):
    __tablename__: 'todos'
    id = db.Column(db.Integer(), primary_key=True)
    description = db.Column(db.String, nullable =False)
    complete = db.Column(db.Boolean, nullable = False)


db.create_all()
@app.route('/')
def index():
    #show todos
    todo_list = Todo.query.all()
    
    return render_template('index.html', todo_list=todo_list )

@app.route('/todo', methods=['POST'])
def add_todo():
    try:
        description = request.form.get('description')
        new_todo= Todo(description=description, complete = False)
        db.session.add(new_todo)
        db.session.commit()
        return redirect(url_for('index'))
    except:
        db.session.rollback()
        abort(500)
    finally:
        db.session.close()


@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    
    app.run(debug=True)