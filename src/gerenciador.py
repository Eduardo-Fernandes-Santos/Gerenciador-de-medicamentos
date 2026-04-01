import json
import os

ARQUIVO_DADOS = "medicamentos.json"

def carregar_dados():
    if not os.path.exixts(ARQUIVO_DADOS):
        return[]
    with open(ARQUIVO_DADOS, "r", encoding="utf-8") as f:
        return json.load(f)

def salvar_dados(dados):
    with open(ARQUIVO_DADOS, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4)

def adicionar_medicamento(nome, dosagem, horario):
    if not nome or not dosagem or not horario:
        raise ValueError("Todos os campos (nome, dosagem, horário) são obrigatórios.")
    
    dados = carregar_dados()
    novo_medicamento = {
        "id": len(dados) + 1,
        "nome": nome,
        "dosagem": dosagem,
        "horario": horario
    }
    dados.append(novo_medicamento)
    salvar_dados(dados)
    return novo_medicamento

def listar_medicamentos():
    return carregar_dados()

def remover_medicamento(id_medicamento):
    dados = carregar_dados()
    dados_filtrados = [m for m in dados if m["id"] != id_medicamento]
    
    if len(dados) == len(dados_filtrados):
        raise KeyError("Medicamento não encontrado.")
        
    salvar_dados(dados_filtrados)
    return True

# Interface CLI básica
if __name__ == "__main__":
    print("--- Gerenciador de Medicamentos CLI ---")
    print("1. Adicionar Medicamento")
    print("2. Listar Medicamentos")
    # Para o escopo da atividade, você pode expandir o menu com inputs do usuário (input())