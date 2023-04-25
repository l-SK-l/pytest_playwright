# 🎭Automate Web monitoring firewall with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/).

https://user-images.githubusercontent.com/65646599/233857975-6b84c02a-2a0d-404c-94aa-bba2a5c56a08.mov

## 📖 Documentation:

https://playwright.dev/python/docs/intro

## ❕Requirements:
* To run this testing framework, you will need:

  * [Python](https://www.python.org/) 3.7 or higher
  * [Docker](https://www.docker.com/) (if you want to run the tests in a container)
  * [Docker-compose](https://docs.docker.com/compose/) (if you want to run the tests in a container)
  * [Allure](https://github.com/allure-framework) (if you want to generate test reports)

## 🔧 Installation: 

1. Clone the repository:
```sh
git clone https://github.com/l-SK-l/pytest_playwright.git
```
1. Open directory:
```sh
cd pytest_playwright/
```

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

1. Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
 For Windows:
```sh
.\.venv\Scripts\Activate.ps1
```

1. Install project dependencies: 
```sh
pip install -r requirements.txt
```
1. Install Playwright:
```sh
playwright install
```
1. Install Playwright dependencies:
```sh
playwright install-deps
```

## 🚀 Running:


1. To run the example tests, more information [docs](https://playwright.dev/python/docs/running-tests):

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

..... NOT READY!!!.....
..... NOT READY!!!.....
..... NOT READY!!!.....
..... NOT READY!!!.....
..... NOT READY!!!.....

## 🐳 [Docker](https://www.docker.com/):
>Docker is a platform for developing, delivering, and running applications in containers. In the context of testing, Docker can be used to run tests in isolated containers to ensure environment consistency and avoid conflicts between dependencies. In this example, if you want to run tests in a Docker container, you need to install Docker and Docker-compose. Then, to run tests in a container, use the following command:
```sh
docker-compose up -d allure allure-ui
```

You can see the logs:
```sh
docker-compose logs -f allure
docker-compose logs -f allure-ui
```
## 📈 [Allure Framework](https://github.com/allure-framework):
>Allure is a framework and report generator that can be used to create beautiful and informative reports on test results. In this example, Allure is used to generate reports on test execution results. If you want to generate reports, you need to install Allure and run tests with the --alluredir parameter, as shown below:
```sh
pytest --clean-alluredir
```
>After running tests, you can generate Allure reports using the command:

```sh

```
Open Reports:
```sh

```