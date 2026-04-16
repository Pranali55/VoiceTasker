from flask import Flask, render_template, request, redirect
from models import init_db, add_task, get_tasks
from utils.speech_to_text import listen_task
from utils.text_to_speech import speak_text

app = Flask(__name__)
init_db()

@app.route("/")
def index():
    tasks = get_tasks()
    return render_template("index.html", tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        add_task(task)
    return redirect("/")

@app.route("/voice")
def voice():
    task = listen_task()
    add_task(task)
    return redirect("/")

@app.route("/speak")
def speak():
    tasks = get_tasks()
    text = "Your tasks are: " + ", ".join([t[1] for t in tasks])
    speak_text(text)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
