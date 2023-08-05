import pandas as pd


def read(data):

    df = pd.read_csv(data, sep=",", encoding='cp1252')

    df['Country Name'].fillna('No data', inplace=True)
    df['2019 [YR2019]'].fillna('0', inplace=True)
    df['2019 [YR2019]'] = df['2019 [YR2019]'].str.replace('..','0')
    dado_int = df['2019 [YR2019]'].astype('float')
    dado_int = dado_int.astype('int')
    pd.to_numeric(dado_int)
    print(dado_int.mean())
    print(dado_int.head())


if __name__ == '__main__':
    data = "./archive/0d292e16-2f1b-452b-9c91-4a3f9fed30cc_Data.csv"
    read(data)

