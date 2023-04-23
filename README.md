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

1. Use the package manager [pip](https://pip.pypa.io/en/stable/) to install the requirements.

2. Create and activate a virtual environment:
```sh
python3 -m venv venv
source venv/bin/activate
```
2.1 For Windows:
```sh
.\.venv\Scripts\Activate.ps1
```

3. Install project dependencies: 
```sh
pip install -r requirements.txt
```
4. Install Playwright:
```sh
playwright install
```

## 🚀 Running:
Follow these steps to install the necessary packages:

1. Clone the repository:
```sh
git clone https://github.com/ZhikharevAl/python-playwright-demo-project.git
```

2. To run the example tests, more information [docs](https://playwright.dev/python/docs/running-tests):
```sh
pytest .\tests\ sv --slowmo 800 --headed --screenshot only-on-failure --video on
```

..... NOT READY!!!.....
..... NOT READY!!!.....
..... NOT READY!!!.....
..... NOT READY!!!.....
..... NOT READY!!!.....

## 🐳 [Docker](https://www.docker.com/):
>Docker is a platform for developing, delivering, and running applications in containers. In the context of testing, Docker can be used to run tests in isolated containers to ensure environment consistency and avoid conflicts between dependencies. In this example, if you want to run tests in a Docker container, you need to install Docker and Docker-compose. Then, to run tests in a container, use the following command:
```sh
docker build -t <Container name> .
docker run -it <Container name>
docker-compose up
```
## 📈 [Allure Framework](https://github.com/allure-framework):
>Allure is a framework and report generator that can be used to create beautiful and informative reports on test results. In this example, Allure is used to generate reports on test execution results. If you want to generate reports, you need to install Allure and run tests with the --alluredir parameter, as shown below:
```sh
pytest --clean-alluredir
```
>After running tests, you can generate Allure reports using the command:

```sh
allure serve allure-results
```
## Testing report using the [Pandas library](https://github.com/pandas-dev/pandas):
```sh
pip install pandas
```
1. Load the test data into a Pandas DataFrame.
2. Write test functions that validate the expected behavior of the code being tested.
3. Run the test functions on the test data, and store the results in a new DataFrame.
4. Generate a summary of the test results using the Pandas library.
### Here's some example code that demonstrates how to do this:
```sh
import pandas as pd

# Load the test data into a DataFrame
test_data = pd.read_csv('test_data.csv')

# Define a test function
def test_function(input_data, expected_output):
    output = my_function(input_data)
    assert output == expected_output, f"Expected {expected_output}, but got {output}."

# Run the test function on the test data
test_results = []
for i, row in test_data.iterrows():
    input_data = row['input_data']
    expected_output = row['expected_output']
    try:
        test_function(input_data, expected_output)
        test_results.append('Pass')
    except AssertionError as e:
        test_results.append('Fail')

# Store the test results in a new DataFrame
test_data['test_result'] = test_results

# Generate a summary of the test results
summary = test_data.groupby('test_result').size()
print(summary)
```
>In this example, we load the test data into a Pandas DataFrame, define a test function, run the test function on the test data, store the test results in a new DataFrame, and generate a summary of the test results using the groupby() method. The resulting summary shows the number of tests that passed and the number of tests that failed.