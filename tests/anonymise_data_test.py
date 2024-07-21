import os
import unittest
from pyspark.sql.functions import col, date_format,to_date
from pyspark.sql import functions as F
import coverage

from latitude_challenge.anonymise_data import anonymisedata

class TestAnonymise(unittest.TestCase):
    
    def setUp(self):
        
        self.t_filename = "output_data_test.csv"
        self.t_path = path = os.path.join(os.getcwd(),"test_data_files") 
        self.test = anonymisedata(self.t_path,self.t_filename,10)
        
        
    def test_file_exists(self):
        
        test_output_file_path = os.path.join(self.t_path, self.t_filename)
        print(f"test_output_file_path :{test_output_file_path}" )
        self.test.fake_data()
        self.assertTrue(os.path.exists(test_output_file_path), "File was not created.")
    
    def test_file_count(self):
        
        test_outout_df = self.test.fake_data()
        assert test_outout_df.count() == 10
        
    def test_mask_string(self):
        test_string_val = "Testingastringvalue"
        test_return_string = self.test.mask_string(test_string_val)
        assert test_return_string != "Testingastringvalue"
        
    def test_load_fakedata(self):    
        test_fake_data = self.test.fake_data() 
        test_load_fd_df = self.test.load_fakedata()  
        assert test_load_fd_df.count() == test_fake_data.count()
        
    def test_run(self):
            
        test_masked_data_df = self.test.run() 
        
        assert test_masked_data_df.select("FirstName").collect() != test_masked_data_df.select("MaskedFname").collect()
        assert test_masked_data_df.select("LastName").collect() != test_masked_data_df.select("MaskedLname").collect()
        assert test_masked_data_df.select("Address").collect() != test_masked_data_df.select("MaskedAddress").collect()
        
    
        
if __name__ == '__main__':
    
    cov = coverage.Coverage()
    cov.start()

    unittest.main()

    cov.stop()
    cov.save()

    cov.html_report()
    print("Done.")     
       
# python -m unittest anonymise_data_test.py
# python -m coverage run -m unittest anonymise_data_test.py
# coverage report -m anonymise_data.py

# /Users/krayakota/development/git-repo/latitude_challenge/output_data.csv