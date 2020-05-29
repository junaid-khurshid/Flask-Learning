"""In this example, we're returning valid HTML code.

If you open this example in your browser, you'll see the page rendered
nicely as a real HTML page. That means that Flask took care of returning
to the client the `Content-Type: 'text/html'`.

**TODO**
Use the list of authors present in the `hello_world` view to
return a <ul> HTML tag containing the authors in the list.
"""
from flask import Flask
from flask import render_template_string

app = Flask(__name__)


@app.route('/')
def hello_world():
    hello_name = "Khurshid"
    html = """
        <html>
            <h1>Welcome to {{hello}} Library HTML!</h1>
        </html>
    """
    render_html = render_template_string(html, hello=hello_name)
    authors = ["Junaid", "Asaad", "Ahmed"]
    authors_list = "<ul>"
    authors_list += "\n".join(["<li>{author}</li>".format(author=author) for author in authors])
    authors_list += "<ul>"
    print(authors_list)
    # build an <ul> with authors
    #return html.format(authors= authors_list)
    return render_html
