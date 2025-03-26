from flask import Flask, render_template, request, send_file
from io import BytesIO
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/doc1', methods=['GET', 'POST'])
def doc1():
    if request.method == 'POST':
        a = request.form['a']
        b = request.form['b']
        c = request.form['c']
        d = request.form['d']
        e = request.form['e']

        content = f"""
Данный документ {a}, который используется представителем {b} был создан {c}.
{a} необходимо реализовать до {d}.
{e if e else ''}

---

a) {a}
b) {b}
c) {c}
d) {d}
e) {e if e else '—'}
"""
        return render_template('result.html', content=content, filename="document1.txt")
    return render_template('doc1.html')

@app.route('/doc2', methods=['GET', 'POST'])
def doc2():
    if request.method == 'POST':
        f = request.form['f']
        g = request.form['g']
        h = request.form['h']
        i = request.form['i']
        j = request.form['j']

        content = f"""
{f} используется представителем {g} {h}.
Документ действует до {i}.
{j if j else ''}

---

f) {f}
g) {g}
h) {h}
i) {i}
j) {j if j else '—'}
"""
        return render_template('result.html', content=content, filename="document2.txt")
    return render_template('doc2.html')

@app.route('/download', methods=['POST'])
def download():
    content = request.form['content']
    filename = request.form['filename']

    buffer = BytesIO()
    buffer.write(content.encode('utf-8'))
    buffer.seek(0)
    return send_file(buffer, as_attachment=True, download_name=filename, mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)
