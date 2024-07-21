from latitude_challenge.anonymise_data import anonymisedata
import os

if __name__ == '__main__':
    
    filename = "output_data.csv"
    path = os.path.join(os.getcwd(),"data_files") 
    reccount = 100

    test = anonymisedata(path,filename,reccount)
    test.run()