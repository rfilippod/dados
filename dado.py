import pandas as pd


def read(data):
    # Use a breakpoint in the code line below to debug your script.
    df = pd.read_csv(data, sep=",", encoding='cp1252')

    df['Country Name'].fillna('No data', inplace=True)  # Press Ctrl+F8 to toggle the breakpoint.
    print(df.head(5).to_string())  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    data = "./archive/0d292e16-2f1b-452b-9c91-4a3f9fed30cc_Data.csv"
    read(data)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
