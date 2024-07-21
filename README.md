# latitude_challenge

## Installation

``` bash
pip install pdm
```

## Usage

``` bash
pdm --help
```
## Usage to install the dependencies
``` bash
pdm  install  
```
## how to run the main program to generate data files ( fake , masked data )
### run the following command  from the prackage location "/src/latitude_challende/"
``` bash
python run.py  
```

## Run the following  test commands  from the prackage test folder location "/tests/"
### how to run test file
``` bash
python -m unittest anonymise_data_test.py
```

### how to run test file with coverage report

``` bash
python -m coverage run -m unittest anonymise_data_test.py
```

### Run coverage report just for  anonymise_data_test.py
``` bash
coverage report -m anonymise_data_test.py

Name                     Stmts   Miss  Cover   Missing
------------------------------------------------------
anonymise_data_test.py      40      7    82%   52-61
------------------------------------------------------
TOTAL                       40      7    82%

```

# SUBMISSION
###  Documentation – Approach, architecture, best standard followed in the coding etc
* The Idea of creating this as a python project is to make it extensible and componetised, easy to test, deploy in the form of a data pipeline. 
* It can be integrated with any CI/CD.This can be deployed in any cloud environemnt or locally. 
* It can be configured in future to read and write to S3 buckets or any cloud data sources. 
* The job can be scheduled/Orchestrated to read and write from the datalake as a AWS Glue job

### Coding Standard
* Cretaed a python project and used pdm for dependency management and unittest for testing inidvidual functions.
* Fake data created with columns Fist_name, Last_name, Address, data_of_birth using  'Faker' python module.
* Chose to use pyspark to load, process, analyse the data 
    * Source Data: 'fake_data' function form the package generates CSV file  containing first_name, last_name, address, date_of_birth. 
            The file is saved here: "datafiles\output_data.csv"
    * Load Data: 'load_fakedata' function loads the fake data from the above locationa nd returns a dataframe for further processing.
    * Transform: After file was successfully loaded, data was validatied for accuracy. 'mask_string' function was registered as an UDF(User Defined Function) to anonymise the Fist_name, Last_name, Address     columns and saved to a new file "datafiles\masked_data.csv"

## Code 
Python file is located in src folder: src/latitude_challenge/anonymise_data.py
## Output results as appropritate
Anonymised data is writtten as a CSV file to this location  'datafiles\masked_data.csv'
## Testing scenario’s
Used "unittest" package  to test the class file individual methods to cover all the corner cases.
### Test file location
Coverage was also reported.
## Source files.
Git source: 






