from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num_events = int(request.form["num_events"])
            return redirect(url_for("events", num=num_events))
        except ValueError:
            return render_template("index.html", error="Please enter a valid number!")
    return render_template("index.html")

@app.route("/events/<int:num>")
def events(num):
    return f"You asked for {num} events. (This page will show event entry fields.)"

if __name__ == "__main__":
    app.run(debug=True)


app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for session

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        try:
            num_events = int(request.form["num_events"])
            session["num_events"] = num_events  # store it temporarily
            return redirect(url_for("events"))
        except ValueError:
            return render_template("index.html", error="Please enter a valid number!")
    return render_template("index.html")

@app.route("/events", methods=["GET", "POST"])
def events():
    num = session.get("num_events", 1)
    if request.method == "POST":
        event_names = []
        event_times = []
        for i in range(num):
            event_name = request.form.get(f"event_{i}")
            event_time = request.form.get(f"time_{i}")
            event_names.append(event_name)
            event_times.append(event_time)
        # Placeholder: Show result or redirect
        return f"Received {len(event_names)} events! (Next page coming soon)"
    return render_template("events.html", num=num)

if __name__ == "__main__":
    app.run(debug=True)

@app.route("/names", methods=["GET", "POST"])
def names():
    if request.method == "POST":
        pam_names = request.form["pam_names"].strip().splitlines()
        nsm_names = request.form["nsm_names"].strip().splitlines()
        session["pam_names"] = [name.strip() for name in pam_names if name.strip()]
        session["nsm_names"] = [name.strip() for name in nsm_names if name.strip()]
        status = f"Processed {len(session['pam_names']) + len(session['nsm_names'])} names successfully!"
        return render_template("names.html", status=status)
    return render_template("names.html")

