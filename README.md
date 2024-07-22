# latitude_challenge

## Installation

### Clone the repository

``` bash
git clone https://github.com/ranjitharvsk/latitude_challenge.git
```
### Change directory 
``` bash
cd latitude_challenge
```

### Create docker image from  Dockerfile location
``` bash
docker build -t latitude-app .
```
### Run the application using the created image
``` bash
docker run latitude-app
```

### run the individual jobs locally or from docker shell
#### Connect to docker shell
``` bash
docker run -it latitude-app sh
```
#### Main file execution
``` bash
python  run.py 
```
#### Running test file
``` bash
python -m unittest anonymise_data_test.py
```
#### Generate coverage report
``` bash
python -m coverage run -m unittest anonymise_data_test.py
```

#### Run coverage report just for  anonymise_data_test.py
``` bash
coverage report -m anonymise_data_test.py
```

# SUBMISSION
### Approach, architecture.
* The Idea of creating this as a python project is to make it extensible and componentized, easy to test, deploy in the form of a data pipeline. 
* Delivering it as a docker container (Dockerfile) that can be used to run the code locally or any cloud environment
* It can be integrated with any CI/CD.
* It can be configured in future to read and write to S3 buckets or any cloud delta lakes like Snowflake and Databricks.
* The job can be scheduled/Orchestrated using Airflow or can be registered as a AWS Glue job with internal scheduling.

### Coding Standard
* Cretaed a python project "Latitude_challenge” and a package "Latitude_challenge1" within that.
* model [text](latitude_challenge1/anonymise_data.py) has all the core logic with multiples methods. 
* Fake data created with columns Fist_name, Last_name, Address, data_of_birth using ‘Faker' python module.
* Chose to use pyspark to load, process, analyse the data 
    * Source Data: 'fake_data' function form the package generates CSV file containing first_name, last_name, address, date_of_birth. 
            The file is saved here: "datafiles\output_data.csv"
    * Load Data: 'load_fakedata' function loads the fake data from the above locationa nd returns a dataframe for further processing.
    * Transform: After file was successfully loaded, data was validatied for accuracy. 'mask_string' function was registered as an UDF(User Defined Function) to anonymise the Fist_name, Last_name, Address     columns and saved to a new file "datafiles\masked_data.csv"

## Code 
Python file is in the package "Latitude_challenge1" folder: anonymise_data.py
## Output results as appropriate
Fake data is written as a CSV file to this location  'datafiles\output_data.csv'
Anonymised data is written as a CSV file to this location  'datafiles\masked_data.csv'
## Testing scenario’s
Used "unittest" package  to test the class file. The unit test file [text](anonymise_data_test.py) tests individual methods to cover all the corner cases.
Test fake data is written as a CSV file to this location  'test_datafiles\output_data_test.csv'
Test anonymised data is written as a CSV file to this location ‘test_datafiles\masked_data.csv'
### Test coverage report 
``` bash

Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
anonymise_data_test.py      40      7    82%   52-61
------------------------------------------------------
TOTAL                       40      7    82%
``` 

## Source files.
Git source: https://github.com/ranjitharvsk/latitude_challenge.git







