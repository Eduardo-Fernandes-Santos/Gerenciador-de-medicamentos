import json
import os

ARQUIVO_DADOS = "medicamentos.json"

def carregar_dados():
    # Aqui já está com o "exists" corrigido!
    if not os.path.exists(ARQUIVO_DADOS):
        return []
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

# Interface CLI interativa
if __name__ == "__main__":
    while True:
        print("\n--- Gerenciador de Medicamentos CLI (v1.0.1) ---")
        print("1. Adicionar Medicamento")
        print("2. Listar Medicamentos")
        print("3. Remover Medicamento")
        print("4. Sair")
        
        escolha = input("\nEscolha uma opção: ")
        
        if escolha == '1':
            nome = input("Nome do medicamento: ")
            dosagem = input("Dosagem (ex: 500mg, 1 comprimido): ")
            horario = input("Horário (ex: 08:00, 12h em 12h): ")
            try:
                med = adicionar_medicamento(nome, dosagem, horario)
                print(f"✅ Sucesso! Medicamento '{med['nome']}' cadastrado com o ID {med['id']}.")
            except ValueError as e:
                print(f"❌ Erro: {e}")
                
        elif escolha == '2':
            medicamentos = listar_medicamentos()
            if not medicamentos:
                print("📭 Nenhum medicamento cadastrado.")
            else:
                print("\n--- Lista de Medicamentos ---")
                for m in medicamentos:
                    print(f"[ID: {m['id']}] {m['nome']} | Dosagem: {m['dosagem']} | Horário: {m['horario']}")
                    
        elif escolha == '3':
            try:
                id_remover = int(input("Digite o ID do medicamento para remover: "))
                remover_medicamento(id_remover)
                print("🗑️ Medicamento removido com sucesso!")
            except ValueError:
                print("❌ Erro: O ID deve ser um número inteiro.")
            except KeyError as e:
                print(f"❌ Erro: {e}")
                
        elif escolha == '4':
            print("Saindo... Lembre-se de tomar seus remédios na hora certa! 👋")
            break
        else:
            print("⚠️ Opção inválida. Tente novamente.")