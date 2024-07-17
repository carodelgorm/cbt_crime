import os

data_root = r'C:/'

DATA_PATH = os.path.join(
    data_root, "Users", "CarolynGorman", "OneDrive", "repos", 
    "cbt_crime", "data"
    )

PJCT_PATH = os.path.join(
    data_root, "Users", "CarolynGorman", "OneDrive", "repos", 
    "cbt_crime", "cbt-crime"
    )

def data_path(*args):
    return os.path.join(DATA_PATH, *args)

def icpsr_data_path(version: str, *args):
    """version must be str of 1,2,3,4,5"""
    return os.path.join(DATA_PATH, "ICPSR_27382", f"DS000{version}", *args)

def out_path(*args):
    return os.path.join(PJCT_PATH, "out", *args)

def out_data_path(*args):
    return out_path("clean_data", *args)