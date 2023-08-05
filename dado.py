import pandas as pd


def read(data):
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_csv(data, sep=",", encoding='cp1252')

    print(df.to_string())  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = './archive/teste.csv'
    read(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
