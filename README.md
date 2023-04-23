# 🎭Automate Web monitoring firewall with [Python](https://www.python.org/) and [Playwright](https://playwright.dev/python/).

## 📖 Documentation:

https://playwright.dev/python/docs/intro

## ❕Requirements:
* To run this testing framework, you will need:

  * [Python](https://www.python.org/) 3.7 or higher
  * [Docker](https://www.docker.com/) (if you want to run the tests in a container)
  * [Docker-compose](https://docs.docker.com/compose/) (if you want to run the tests in a container)
  * [Allure](https://github.com/allure-framework) (if you want to generate test reports)

## 🔧 Installation: 

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.
1. Create a virtual environment:
```sh
python -m venv .venv
```
1. Activate virtual environment:
```sh
source .venv/bin/activate
```
    1. For Windows:
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
