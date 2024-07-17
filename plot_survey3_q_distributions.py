"""
This script reads in data directly downloaded from the Criminal Justice Drug Abuse
Treatment Studies (CJ-DATS):ICPSR 27382 National Criminal Justice Treatment Program 
(NCJTP) Survey in the United States, 2002-2008), available via the following link:
https://www.icpsr.umich.edu/web/NAHDAP/studies/34988

It then includes functions that are called to plot the distribution of various 
survey variables and their unique values
"""
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt

from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

import datetime as dt

from util.env import icpsr_data_path, out_path, out_data_path

def set_properties():
    """sets mpl properties"""
    mpl.rcParams['legend.handlelength'] = 1
    mpl.rcParams['legend.fontsize'] = 10
    mpl.rcParams['xtick.labelsize'] = 9
    mpl.rcParams['ytick.labelsize'] = 9
    mpl.rcParams['figure.titlesize'] = 18
    mpl.rcParams['axes.titlesize'] = 12
    mpl.rcParams['axes.titlepad'] = 20


def format_axes() -> plt.Axes:
    """fcn used to format plot axes"""
    
    ax = plt.gca()
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    
    ax.yaxis.grid(True, alpha=0.5, zorder=1, color='#d4d2d2')
    
    return ax


def get_vars_and_vals(df: pd.DataFrame) -> None:
    """This fcn reads in ICPSR data as a pandas dataframe, and saves the variables 
    (columns) and their unique values as a new csv file with the first column
     being all column names, and the second column being all unique values per
    variable. This facilitates easier review of variables and values 
    """
    column_names = df.columns.tolist()
    
    # create a list to hold unique values for each column
    unique_values = [df[col].unique().tolist() for col in column_names]
    
    # create a new df with the collected information
    unique_df = pd.DataFrame({
        'col_names': column_names,
        'unique_values': unique_values
    })

    unique_df.to_csv(
        out_data_path('vars_and_vals_from_0003.csv'), 
        index=False
        )

    return 


def plot_distribution(df: pd.DataFrame, column_name: str, title: str, 
                      save: bool=False) -> None:
    """This fcn takes a pandas dataframe, plots the distribution of parameter
    "column_name", and sets the plot title to "title"

    param: save (bool) if True, will save the plot to the out folder
    """
    df = _recode_vals(df)

    if column_name not in df.columns:
        raise ValueError(f"Column {column_name} does not exist in the df.")

     # calculate the count of each unique value in the specified column
    value_counts = df[column_name].value_counts()
    
    set_properties()

    # create a bar chart
    fig, ax = plt.subplots(figsize=(12,6))

    # plot the bar chart on the axes object
    bars = ax.bar(value_counts.index, 
                  value_counts.values, 
                  color='cornflowerblue')
    
    # label the bars with their counts
    for bar in bars:
        height = bar.get_height()
        ax.annotate(f'{height}',
                    xy=(bar.get_x() + bar.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom')
    

    plt.title(f'{title} ({column_name})')
    plt.xlabel('Values')
    plt.grid(axis='y')
    format_axes()

    if save==True:
        plt.savefig(
            out_path(f'{column_name}_{title}.png'),
            dpi=300, 
            bbox_inches='tight')
    else:
        plt.show() 
    
    return


def _recode_vals(df: pd.DataFrame) -> pd.DataFrame:
    """This helper fcn recodes all values in columns as strings for ease of 
    manipulation because they are all categorical"""
    for col in df.columns:
        df[col] = df[col].astype('string')

    return df


if __name__ == '__main__':
    
    # read in the raw data
    df = pd.read_csv(
        # 3 is the specific survey, each saved in a diff folder
        icpsr_data_path('3', '27382-0003-Data.tsv'), 
        # using '\t' as the separator for TSV files
        sep='\t'
        )

    # save variables and their unique vals to a csv for ease of reference
    get_vars_and_vals(df)

    # plot all variables of interest
    plot_distribution(
        df=df, 
        column_name='S3BQ39_3',
        title='distribution of facilities that provided mental health counseling',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ4',
        title='Population served, adult or juvenile',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ5',
        title='Type of organization',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ8_6',
        title='Provider field of education is psychology (0=No, 1=Yes)',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ13',
        title='Setting that provider works in',
        save=True
        )

    plot_distribution(
        df=df,
        column_name='S3BQ39_3',
        title='Provided mental health counseling (0=No, 1-Yes)',
        save=True
        )

    plot_distribution(
        df=df,
        column_name='S3BQ40E',
        title='Program(s) use cognitive approaches',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ40F',
        title='Program(s) use behavioral management approaches',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ40H',
        title='Program(s) use social skill development',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='S3BQ40K',
        title='Program(s) use individual drug counseling',
        save=True
        )
        
    plot_distribution(
        df=df,
        column_name='S3BQ48G',
        title='Facility is involved with mental health program',
        save=True
        )
        
    plot_distribution(
        df=df,
        column_name='S3BQ51C',
        title='Importance of mental health counseling compared to substance use treatment',
        save=True
        )
    
    plot_distribution(
        df=df,
        column_name='s3bq41cbt',
        title='providers that report using CBT',
        save=True
        )
    
    



