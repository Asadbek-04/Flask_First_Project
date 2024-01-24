from flask import Flask
import utils as u

app = Flask(__name__)

candidates = u.load_candidates()


@app.route("/")
def page_index():
    str_candit = '<pre>\n'
    for c in candidates.values():
        str_candit += f"{c['name']}\n{c['position']}\n{c['skills']}\n\n"
    str_candit += '</pre>'
    return str_candit


@app.route("/candidates/<int:id>")
def profile(id):
    candidate = candidates[id]
    return f'<img src={candidate["picture"]}></img><br><br>{candidate["name"]}<br>{candidate["position"]}<br>{candidate["skills"]}<br><br>'


@app.route("/skills/<skill>")
def skills(skill):
    str_candit = '<pre>'
    for candit in candidates.values():
        candit_skills = candit['skills'].split(', ')
        candit_skills = [x.lower() for x in candit_skills]
        if skill.lower() in candit_skills:
            str_candit += f"{candit['name']}\n{candit['position']}\n{candit['skills']}\n\n"
    str_candit += '</pre>'
    return str_candit


app.run(debug=True)
