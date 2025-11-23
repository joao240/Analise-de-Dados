import pandas as pd
from src.transform import transform_data


def main():
    df = pd.read_csv('sales_data_sample.csv', encoding='latin-1')
    df_t = transform_data(df)
    out_path = 'sales_data_transformed.csv'
    df_t.to_csv(out_path, index=False, encoding='utf-8')
    print('Pronto — arquivo salvo em', out_path)
    print('Tamanho: antes =', df.shape, 'depois =', df_t.shape)
    print(df)

if __name__ == '__main__':
    main()
