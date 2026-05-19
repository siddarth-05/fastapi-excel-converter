import pandas as pd
# class MyError(Exception):
#     """Exception for bad reads"""
#     def __init__(self, )

def convert_excel_to_records(file):
    """convert excel to dataframe, then dataframe to dict"""
    try:
        data = pd.read_excel(file)
        return (data.to_dict(orient = 'records'))
    
    except(ValueError):
        raise ValueError("Couldn't read file")
    
