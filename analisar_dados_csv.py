import pandas as pd
import matplotlib.pyplot as plt

def analyze_data(file_path, max_lines=128):
    try:
        # Ler o arquivo CSV
        data = pd.read_csv(file_path.strip(), delimiter=';')  # Ajuste o delimitador conforme necessário
        print("Colunas disponíveis no arquivo CSV:", data.columns.tolist())
        
        # Imprimir todas as linhas e colunas do CSV até o limite especificado
        for index, row in data.iterrows():
            if index >= max_lines:
                print(f"Exibindo apenas as primeiras {max_lines} linhas.")
                break
            print(f"Linha {index + 1}:")
            for col in data.columns:
                print(f"  {col}: {row[col]}")
            print("\n")
        
        # Análise Estatística e Resumo
        print("Resumo Estatístico:")
        print(data.describe(include='all'))
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

def plot_data(file_path):
    try:
        data = pd.read_csv(file_path.strip(), delimiter=';')
        print("Colunas disponíveis no arquivo CSV:", data.columns.tolist())
        
        # Solicitar ao usuário que escolha as colunas para o eixo X e Y
        x_column = input("Digite o nome da coluna para o eixo X: ")
        y_column = input("Digite o nome da coluna para o eixo Y: ")
        
        # Verificar se as colunas existem
        if x_column in data.columns and y_column in data.columns:
            data.plot(kind='line', x=x_column, y=y_column)
            plt.title(f'Gráfico de {y_column} vs {x_column}')
            plt.xlabel(x_column)
            plt.ylabel(y_column)
            plt.show()
        else:
            print(f"Uma ou ambas as colunas '{x_column}' e '{y_column}' não foram encontradas no arquivo CSV.")
    except Exception as e:
        print(f"Erro ao ler o arquivo CSV: {e}")

if __name__ == "__main__":
    file_path = input("Digite o caminho do arquivo CSV: ").strip()
    analyze_data(file_path)
    plot_data(file_path)