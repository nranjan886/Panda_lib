import os
from flask import Flask

from routes.panda import PANDA_LIB

app = Flask(__name__)
app.register_blueprint(PANDA_LIB)

@app.route("/")
def home():
    return "PANDA'S LIB PYTHON"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 2000))
    app.run(debug=False, host="0.0.0.0", port=port)




