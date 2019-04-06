from starlette.applications import Starlette
from starlette.templating import Jinja2Templates
from starlette.staticfiles import StaticFiles
import uvicorn

templates = Jinja2Templates(directory='web/templates')

app = Starlette(debug=True)
app.mount('/static', StaticFiles(directory='web/statics'), name='static')


@app.route('/')
async def homepage(request):
    return templates.TemplateResponse('index.html', {'request': request})


