import markdown
from markupsafe import Markup
from flask import Flask, render_template, request
from model_files.generate import generate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    if 'search' in request.form:
        query = request.form.get('query')
        topic_name, result_text = generate(topic_name = query)
    elif 'surprise' in request.form:
        topic_name, result_text = generate()
    else:
        topic_name, result_text = "No topic mentioned", "No text generated."
    
    result_html = markdown.markdown(result_text)
    return render_template('result.html', topic=topic_name, result=result_html)

if __name__ == '__main__':
    app.run(debug=True)
