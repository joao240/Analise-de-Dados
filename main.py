import pandas as pd
from src.extract import extract_data, missing_values, validate_and_convert_types
from src.transform import calculation_total_value, Addressing_outliers, handle_empty_values

def main():
    # extract.py
    # 1. Extração
    df_extracted = extract_data()
    print("Extração concluída.")
    
    # 2. Inspeção de Dados Brutos
    print("\n--- DADOS BRUTOS ---")
    missing_values(df_extracted)
    
    # 3. Validação e Conversão de Tipos
    df_cleaned_types = validate_and_convert_types(df_extracted)
    print("\nConversão de tipos concluída.")

    # transform.py
    # 1. Calculo do Valor Total
    df_calculation = calculation_total_value(df_cleaned_types) 
    print("Calculo e mudança no DAtaFrame concluída.")
    
    # 2. Tratamento de Outliers
    df_Addressing = Addressing_outliers(df_calculation)
    print("Tratamento de outliers concluído.")

    # 3. Tratamento de Valores Vazios
    df_handle = handle_empty_values(df_Addressing)
    print("Tratamento de valores vazios concluído.")
    
    # Exibição dos dados finais
    print("\n--- DADOS FINAIS ---")
    missing_values(df_handle) # Variável corrigida
    
    out_path = 'sales_data_transformed.csv'
    df_handle.to_csv(out_path, index=False, encoding='utf-8') # Variável corrigida
    
    print('\n--- RESULTADO FINAL ---')
    print('Pronto — arquivo salvo em', out_path)
    print('Tamanho: antes =', df_extracted.shape, 'depois =', df_handle.shape) # Variável corrigida
    print(df_handle.head()) # Variável corrigida

if __name__ == '__main__':
    main()