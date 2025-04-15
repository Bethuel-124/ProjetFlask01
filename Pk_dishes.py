from flask import Flask, render_template, redirect, request

app = Flask(__name__)

recettes = [
    {"id": 1, "nom": "Tarte aux pommes", "description": "Une délicieuse tarte aux pommes."},
    {"id": 2, "nom": "Soupe à l'oignon", "description": "Une soupe savoureuse à l'oignon."},
    {"id": 3, "nom": "Spaghetti bolognaise", "description": "Les classiques spaghetti bolognaise."}
]

# Route pour la page d'accueil qui affiche toutes les recettes
@app.route('/')
def index():
    return render_template('index.html', recettes=recettes)
 
@app.route("/dishes")
def dishes():
    return render_template('dishes.html')
    
@app.route('/essai')
def essai():
    return render_template('essai.html')

@app.route('/command', methods=['GET', 'POST'])
def command():
    if request.method == 'GET':
        return render_template('command.html')
    else:
        name = request.form.get('name')
        email = request.form.get('email')
        dishe = request.form.get('dishe')
        if not dishe:
            return "Aucun plat sélectionné. Veuillez choisir un plat."
        transport = request.form.get('trans')
        return f"Vous; {name} avez commandé avec succès du {dishe} et comptez le retirer par vous meme" if transport == "Passer" else f"Vous; {name} avez commandé avec succès du {dishe} et comptez le retirer par GoZem"
        return redirect(url_for('command'))
    
@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
