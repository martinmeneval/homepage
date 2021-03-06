# menev.al

## How it works

This is mostly intended at future Martin for when he'll want to update his website, to avoid having to figure out what his past self did.

### File tree

```bash
homepage
│   .gcloudignore
│   .gitignore
│   app.py
│   app.yaml            # Run instructions for App Engine
│   cloudbuild.yaml     # Default build steps for Cloud Build
│   LICENSE
│   README
│   requirements.txt    # Automatically installed by App Engine
│
├───static
│   │   favicon.ico
│   │   logo-smol.png
│   │   logo.png
│   │   qrcode-gh.png
│   │   qrcode-home.png
│   │   qrcode-li.png
│   │   resume.pdf      # Don't forget to update :)
│   │
│   └───styles
│           styles.css
│
└───templates
        base.j2
        home.j2
        resume.j2
```

### Useful links

[App Engine](https://console.cloud.google.com/appengine/services?authuser=1)  
[Cloud Build](https://console.cloud.google.com/cloud-build/dashboard?authuser=1)  

### QRCodes

Made on [QRCode Monkey](https://www.qrcode-monkey.com).  
Color #0bc  
Downloaded at 2000x2000, background removed, borders cut, downscaled to 256x256

### Run locally

```bash
pip install -r requirements.txt
uvicorn --port 8080 app:app --reload
```
