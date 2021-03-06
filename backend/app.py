from flask import Flask,render_template
import json 

app=Flask(__name__)

#error handler for wrong URl
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

#routing for displaying required output
@app.route('/api/pokemon/')
def index():
    poke_names={"pokemon":["bulbasaur","charmander","squirtle"]}
    return json.dumps(poke_names)
    
if __name__ == '__main__':
    app.run("localhost",port=8006,debug=True)

