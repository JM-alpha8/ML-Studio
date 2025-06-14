from flask import Flask, render_template
from routes.linear import linear_bp
from routes.logistic import logistic_bp
from routes.ridge import ridge_bp
from routes.lasso import lasso_bp
from routes.sgdregressor import sgdregressor_bp
from routes.gd import gd_bp

app = Flask(__name__)
app.register_blueprint(linear_bp)
app.register_blueprint(logistic_bp)
app.register_blueprint(ridge_bp)
app.register_blueprint(lasso_bp)
app.register_blueprint(sgdregressor_bp)
app.register_blueprint(gd_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
