from flask import Flask, render_template
from utils import \
    load_candidates_from_json, \
    get_candidate, \
    get_candidates_by_name, \
    get_candidates_by_skill

app = Flask(__name__)

data = load_candidates_from_json('candidates.json')


@app.route("/")
def index_page():
    return render_template('list.html', candidates=data)


@app.route("/candidate/<int:uid>")
def single(uid):
    candidate = get_candidate(uid)
    return render_template('single.html', candidate=candidate)


@app.route("/search/<name>")
def search(name):
    candidates = get_candidates_by_name(name)
    return render_template('search.html', candidates=candidates, candidates_len=len(candidates))


@app.route("/skills/<skill_name>")
def skill(skill_name):
    candidates = get_candidates_by_skill(skill_name)
    return render_template('skills.html', candidates=candidates, candidates_len=len(candidates), skill_name=skill_name)


app.run()
