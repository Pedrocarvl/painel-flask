from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///nomes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelo da tabela
class Nome(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    conteudo = db.Column(db.String(100), nullable=False)

# Rota principal
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome_digitado = request.form["nome"]
        if nome_digitado:
            novo_nome = Nome(conteudo=nome_digitado)
            db.session.add(novo_nome)
            db.session.commit()

    nomes = Nome.query.all()
    return render_template("index.html", nomes=nomes)

# Rota para remover
@app.route("/remover/<int:id>")
def remover(id):
    nome = Nome.query.get_or_404(id)
    db.session.delete(nome)
    db.session.commit()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)