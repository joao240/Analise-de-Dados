import pandas as pd
from src.transform import transform_data
from src.extract import extract_data

def main():
    # usar a função de extração para obter o DataFrame inicial
    df_extracted = extract_data()

    # aplicar transformação sobre o DataFrame extraído
    df_t = transform_data(df_extracted)

    # salvar resultado final
    out_path = 'sales_data_transformed.csv'
    df_t.to_csv(out_path, index=False, encoding='utf-8')
    print('Pronto — arquivo salvo em', out_path)
    print('Tamanho: antes =', df_extracted.shape, 'depois =', df_t.shape)
    # opcional: mostrar amostra do resultado
    print(df_t.head())

if __name__ == '__main__':
    main()
