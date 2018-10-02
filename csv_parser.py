import matplotlib.pyplot as plt
import pandas as pd
# %matplotlib inline  # for Jupyter Notebook/Console, but not for terminal
import click

@click.group()
def cli():
    """Can display and plot csv files."""
    pass

@cli.command()
@click.argument('filename')
def display(filename):
    """Displays the column names and their data type."""
    df = pd.read_csv(filename)
    print(df.dtypes)

@cli.command()
@click.argument('filename')
@click.option('--column', default=None, help="Name of column to plot. If not used, all will be plotted.")
def plot(filename, column):
    """Plots a histogram of a column of the csv file."""
    df = pd.read_csv(filename)
    if column is None:
        df.hist()
    else:
        df.hist(column=column);
    plt.show()  # for terminal

if __name__ == '__main__':
    cli()
    # import sys
    # command = sys.argv[1]
    # filename = sys.argv[2]
    # if command == 'display':
    #     display_columns(filename)
    # elif command == 'plot':
    #     plot_hist(filename)
    # else:
    #     raise IOError("csv_parser requires 'plot' or 'display' commands")

# df.plot(kind='scatter', x='bier_preis', y='bier_konsum')
# df.plot(kind='scatter', x='jahr', y='bier_preis')