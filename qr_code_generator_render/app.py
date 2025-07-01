from flask import Flask, request, render_template
import qrcode
import os

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    qr_code_path = None
    if request.method == "POST":
        link = request.form["link"]
        img = qrcode.make(link)

        # Ensure static folder exists
        os.makedirs("static", exist_ok=True)

        file_path = os.path.join("static", "qr.png")
        img.save(file_path)
        qr_code_path = file_path

    return render_template("index.html", qr_code=qr_code_path)

if __name__ == "__main__":
    app.run(debug=True)