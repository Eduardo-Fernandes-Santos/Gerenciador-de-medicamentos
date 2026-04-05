import pytest
import os
from src.gerenciador import adicionar_medicamento, listar_medicamentos, remover_medicamento, ARQUIVO_DADOS

# Configuração para limpar o arquivo de testes antes e depois
@pytest.fixture(autouse=True)
def setup_teardown():
    if os.path.exists(ARQUIVO_DADOS):
        os.remove(ARQUIVO_DADOS)
    yield
    if os.path.exists(ARQUIVO_DADOS):
        os.remove(ARQUIVO_DADOS)

# 1. Caminho Feliz
def test_adicionar_medicamento_com_sucesso():
    med = adicionar_medicamento("Paracetamol", "500mg", "08:00")
    assert med["nome"] == "Paracetamol"
    assert len(listar_medicamentos()) == 1

# 2. Entrada Inválida
def test_adicionar_medicamento_campos_vazios():
    with pytest.raises(ValueError, match="Todos os campos"):
        adicionar_medicamento("", "500mg", "08:00")

# 3. Caso Limite (Remover item inexistente)
def test_remover_medicamento_inexistente():
    with pytest.raises(KeyError, match="Medicamento não encontrado"):
        remover_medicamento(999)
