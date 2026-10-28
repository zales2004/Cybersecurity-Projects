from flask import Flask, render_template, request
import re

app = Flask(__name__)

def check_password_strength(password):
    strength = 0
    remarks = ''

    if len(password) >= 8:
        strength += 1
    else:
        remarks += "Password should be at least 8 characters long.<br>"

    if re.search(r'[A-Z]', password):
        strength += 1
    else:
        remarks += "Include at least one uppercase letter.<br>"

    if re.search(r'[a-z]', password):
        strength += 1
    else:
        remarks += "Include at least one lowercase letter.<br>"

    if re.search(r'[0-9]', password):
        strength += 1
    else:
        remarks += "Include at least one digit.<br>"

    if re.search(r'[@$!%*?&]', password):
        strength += 1
    else:
        remarks += "Include at least one special character (@$!%*?&).<br>"

    if strength == 5:
        result = "✅ Very Strong"
    elif 3 <= strength < 5:
        result = "⚠️ Moderate"
    else:
        result = "❌ Weak"

    return result, remarks

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        password = request.form.get("password")
        strength, suggestions = check_password_strength(password)
        return render_template("index.html", strength=strength, suggestions=suggestions, password=password)
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
