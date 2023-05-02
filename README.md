# 🎭Automate Web monitoring firewall with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/).

https://user-images.githubusercontent.com/65646599/235766796-a151e678-2abd-4d3d-99e2-84c1eab6a636.mov

https://user-images.githubusercontent.com/65646599/235766275-25b07996-cf64-4630-a00a-09915acb6b5a.mov

## 📖 Documentation:

https://playwright.dev/python/docs/intro

## ❕Requirements:
* To run this testing framework, you will need:

  * [Python](https://www.python.org/) 3.7 or higher
  * [Docker](https://www.docker.com/) (if you want to run the Allure in a container)
  * [Docker-compose](https://docs.docker.com/compose/) (if you want to run the Allure in a container)

## 🔧 Installation: 

 Clone the repository:
```sh
git clone https://github.com/l-SK-l/pytest_playwright.git
```
 Open directory:
```sh
cd pytest_playwright/
```

 Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

 Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```

    For Windows:

```sh
.\.venv\Scripts\Activate.ps1
```

 Install project dependencies: 
```sh
pip install -r requirements.txt
```
 Install Playwright:
```sh
playwright install
```
 Install Playwright dependencies:
```sh
playwright install-deps
```


## 🚀 Running:


 To run the example tests, more information [docs](https://playwright.dev/python/docs/running-tests):

 Windows with Video
```sh
pytest .\tests\ -sv --slowmo 800 --headed --screenshot only-on-failure --video on
```

 Linux
```sh
pytest tests/
```
   With Video
```sh
pytest tests/ -sv --screenshot only-on-failure --video on
```
   With Allure
```sh
pytest tests/ -sv --screenshot only-on-failure --video on --alluredir=allure-results
```


## 🐳 [Docker](https://www.docker.com/) with 📈[Allure](https://github.com/allure-framework):

* Check permissions or change
```sh
deactivate
```

 Check permissions or change
```sh
chmod 777 *
```

 Run container
```sh
      docker run -p 5050:5050 -e CHECK_RESULTS_EVERY_SECONDS=3 -e KEEP_HISTORY=1 \
                 -v ${PWD}/allure-results:/app/allure-results \
                 -v ${PWD}/allure-reports:/app/default-reports \
                 frankescobar/allure-docker-service
```

 Open report:
```sh
http://IP:5050/allure-docker-service/emailable-report/render?project_id=default
http://IP:5050/allure-docker-service/projects/default/reports/latest/index.html
```

More information abour [allure-docker-service-ui](https://github.com/fescobar/allure-docker-service-ui)