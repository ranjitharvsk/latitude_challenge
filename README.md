# latitude_challenge

## Installation

### Clone the repository

``` bash
git clone https://github.com/ranjitharvsk/latitude_challenge.git
```
### hnage directory 
``` bash
cd latitude_challenge
```

### Crete docker image from  Dockerfile location
``` bash
docker build -t my-latitude-app .
```
### Run the applcation using the created image
``` bash
docker run my-latitude-app
```

### run the individual jobs locally or docker shell
``` bash
docker run -it my-latitude-app sh
```
#### how to main file file
``` bash
python  run.py 
```
#### how to run test file
``` bash
python -m unittest anonymise_data_test.py
```
#### how to run test file with coverage report
``` bash
python -m coverage run -m unittest anonymise_data_test.py
```

#### Run coverage report just for  anonymise_data_test.py
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
* Cretaed a python project "Latitude_challenge"  and a package "Latitude_challenge1" within that.
* model [text](latitude_challenge1/anonymise_data.py) has all the core logic with multiples methods. 
* Fake data created with columns Fist_name, Last_name, Address, data_of_birth using  'Faker' python module.
* Chose to use pyspark to load, process, analyse the data 
    * Source Data: 'fake_data' function form the package generates CSV file  containing first_name, last_name, address, date_of_birth. 
            The file is saved here: "datafiles\output_data.csv"
    * Load Data: 'load_fakedata' function loads the fake data from the above locationa nd returns a dataframe for further processing.
    * Transform: After file was successfully loaded, data was validatied for accuracy. 'mask_string' function was registered as an UDF(User Defined Function) to anonymise the Fist_name, Last_name, Address     columns and saved to a new file "datafiles\masked_data.csv"

## Code 
Python file is located in the package "Latitude_challenge1" folder: anonymise_data.py
## Output results as appropritate
Fake data is written as a CSV ile to this location  'datafiles\output_data.csv'
Anonymised data is writtten as a CSV file to this location  'datafiles\masked_data.csv'
## Testing scenario’s
Used "unittest" package  to test the class file. The unit test file [text](anonymise_data_test.py) tests individual methods to cover all the corner cases.
Test fake data is written as a CSV ile to this location  'test_datafiles\output_data_test.csv'
Test anonymised data is writtten as a CSV file to this location  'test_datafiles\masked_data.csv'
### Test file location
Coverage was also reported.
## Source files.
Git source: https://github.com/ranjitharvsk/latitude_challenge.git






