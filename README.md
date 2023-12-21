# menev.al

## How it works

This is mostly intended at future Martin for when he'll want to update his website, to avoid having to figure out what his past self did.

### File tree

```bash
homepage
├── LICENSE
├── Pipfile
├── Pipfile.lock
├── README.md
├── _sass
│   └── main.scss       # Source stylesheet
├── app.py
├── app.yaml            # Run instructions for App Engine
├── cloudbuild.yaml     # Default build steps for Cloud Build
├── css
│   └── styles.css      # Compiled stylesheet
├── package-lock.json
├── package.json
├── requirements.txt    # Automatically installed by App Engine
├── static
│   ├── favicon.ico
│   └── resume.pdf      # Don't forget to update :)
└── templates
    ├── base.j2
    ├── home.j2
    └── resume.j2
```

### Useful links

[App Engine](https://console.cloud.google.com/appengine/services?authuser=1)  
[Cloud Build](https://console.cloud.google.com/cloud-build/dashboard?authuser=1)  

### QRCode

Made on [QRCode Monkey](https://www.qrcode-monkey.com).  

### Run locally

```bash
pipenv install
pipenv run uvicorn --port 8888 app:app --reload
```

### Update dependencies

```bash
pipenv run pip freeze > requirements.txt
```
