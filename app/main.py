from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Home"
    }
    return templates.TemplateResponse("pages/index.html", {"request": request, "data": data})


@app.get("/about", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "About"
    }
    return templates.TemplateResponse("pages/about.html", {"request": request, "data": data})


@app.get("/services", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Services"
    }
    return templates.TemplateResponse("pages/services.html", {"request": request, "data": data})


@app.get("/process", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Process"
    }
    return templates.TemplateResponse("pages/process.html", {"request": request, "data": data})


@app.get("/contacts", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Contacts"
    }
    return templates.TemplateResponse("pages/contact.html", {"request": request, "data": data})


@app.get("/interactive-security", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Interactive Security"
    }
    return templates.TemplateResponse("pages/interactive_security.html", {"request": request, "data": data})


@app.get("/video-monitoring", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Video Monitoring"
    }
    return templates.TemplateResponse("pages/video_monitoring.html", {"request": request, "data": data})


@app.get("/energy-management", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Energy Management"
    }
    return templates.TemplateResponse("pages/energy_management.html", {"request": request, "data": data})


@app.get("/product-page", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Product Page"
    }
    return templates.TemplateResponse("pages/product_page.html", {"request": request, "data": data})


@app.get("/intelligent-home", response_class=HTMLResponse)
async def home(request: Request):
    data = {
        "page": "Intelligent Home"
    }
    return templates.TemplateResponse("pages/intelligent_home.html", {"request": request, "data": data})


@app.get("/page/{page_name}", response_class=HTMLResponse)
async def page(request: Request, page_name: str):
    data = {
        "page": page_name
    }
    return templates.TemplateResponse("page.html", {"request": request, "data": data})
