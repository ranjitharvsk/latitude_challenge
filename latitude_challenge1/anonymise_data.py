import findspark
findspark.init()

import pyspark
from pyspark import SparkContext,SQLContext
from pyspark.sql.session import SparkSession
from pyspark.sql.types import *
import os.path
from functools import reduce
from pyspark.sql import functions as F
from pyspark.sql.functions import col, date_format,to_date,round,format_number
from pyspark.sql import Row
from datetime import datetime,timedelta
import glob
from pyspark.sql.functions import udf
from pyspark.sql.functions import *

from faker import Faker
import random
import string


class anonymisedata:

    def __init__(self,p_path,p_filename,p_reccount):
        # get spark session initialised.
        
        self.path =p_path
        self.filename = p_filename
        self.recordscount  = p_reccount
        
        
        
        APP_NAME = "Bupa: ASSESSMENT"
        try:
            self.spark = SparkSession.builder.appName(APP_NAME).getOrCreate()
            
        except RuntimeError:
            print("Exception occurred.")
            
    def fake_data(self):
        f = Faker()
        rows = []
        
        for _ in range(self.recordscount):
            rows.append(Row(FirstName=f.first_name(),LastName =f.last_name(), Address = f.address().replace("\n",""), DOB = f.date_of_birth()))
            
        columns = ["FirstName","LastName","Address","DOB"]
        df = self.spark.createDataFrame(rows,columns) 
        
        
        print("Current directory :", os.getcwd())
        output_file_path = os.path.join(self.path,self.filename)
        print("output_file_path",output_file_path)
        df.coalesce(1).write.mode("overwrite").csv(output_file_path, header = True, sep="|" )
        df.show()
        
        return df
    
    def load_fakedata(self):
        
        input_file_path = os.path.join(self.path,self.filename )
        
        df_fd = self.spark.read.csv(input_file_path, header = True,sep="|")
        df_fd.printSchema()
        df_fd.show()
        
        return df_fd
    
    @staticmethod
    def mask_string(p_val):
        # p_val = "Ranjeetha"
        
        n = len(p_val)
        lst_chars = list(p_val)
        # lst_chars[1:int(n)-1]=random.choice(string.ascii_letters)*int(n-2)
        lst_chars[1:int(n)-1] = ''.join(random.choice(string.ascii_letters) for x in range(n-2))
        mask_strng  = "".join(lst_chars)
        return mask_strng
        
    def run(self):
        
        self.fake_data()
        data_df = self.load_fakedata()
        
        # Register mask_string function as udf
        mask_string_udf = udf(self.mask_string,StringType())
        
        masked_data_df = data_df.withColumn("MaskedFname",mask_string_udf(data_df["FirstName"]))
        masked_data_df = masked_data_df.withColumn("MaskedLname",mask_string_udf(data_df["LastName"]))
        masked_data_df = masked_data_df.withColumn("MaskedAddress",mask_string_udf(data_df["Address"]))
        masked_data_df.show()
        
        
        output_mfile_path = os.path.join(self.path,"masked_data.csv")
        print("output_mfile_path",output_mfile_path)
        masked_data_df.select("MaskedFname","MaskedLname","MaskedAddress","DOB").coalesce(1).write.mode("overwrite").csv(output_mfile_path, header = True, sep="|" )
        
        return masked_data_df
 


