from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get('/', response_class=HTMLResponse)
def read_root():
    return """
    <html>
      <head>
        <title>Hoje é aonde?!</title>
      </head>
      <body>
        <h1>Hoje é aonde?</h1>
      </body>
    </html>"""
