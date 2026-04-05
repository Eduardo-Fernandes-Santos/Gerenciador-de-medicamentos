# 💊 Gerenciador de Medicamentos CLI

[![CI](https://github.com/Eduardo-Fernandes-Santos/Gerenciador-de-medicamentos/actions/workflows/ci.yml/badge.svg)](https://github.com/Eduardo-Fernandes-Santos/Gerenciador-de-medicamentos/actions/workflows/ci.yml)
**Versão:** 1.0.1

## 🎯 A Dor Real (O Problema)
Cuidadores de idosos, familiares ou pacientes com rotinas médicas complexas frequentemente enfrentam dificuldades para organizar e lembrar os horários e dosagens de múltiplos medicamentos. A falta de organização pode levar a falhas na medicação, superdosagem ou esquecimento, impactando diretamente a saúde.

## 💡 A Solução e Público-Alvo
Este projeto é uma aplicação de Linha de Comando (CLI) simples e direta, voltada para cuidadores e pacientes. Ela permite cadastrar, listar e remover medicamentos, suas dosagens e horários. A interface via terminal foi escolhida pela sua leveza e rapidez de uso. 

## 🛠️ Tecnologias Utilizadas
- **Linguagem:** Python
- **Armazenamento:** Arquivo local em memória (`.json`)
- **Testes Automatizados:** `pytest`
- **Linting / Análise Estática:** `flake8`
- **Integração Contínua (CI):** GitHub Actions

## 🚀 Como Instalar e Executar

1. **Clone o repositório:**
   ```bash
   git clone [https://github.com/Eduardo-Fernandes-Santos/Gerenciador-de-medicamentos.git](https://github.com/Eduardo-Fernandes-Santos/Gerenciador-de-medicamentos.git)
   cd Gerenciador-de-medicamentos
   ```
2. **Crie um ambiente virtual (opcional, mas recomendado):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # No Windows use: venv\Scripts\activate
   ```
3. **Instale as dependências:**
  ```bash
   pip install -r requirements.txt
  ```
4. **Execute a aplicação:**
  ```bash
  python src/gerenciador.py
  ```
## 🧪 Como Rodar os Testes e o Lint
O projeto conta com testes cobrindo os cenários de sucesso, erro de validação e casos limite (como remoção de itens inexistentes).

**Para rodar o Linting (Verificação de qualidade de código):**
  ```Bash
  flake8 src/ tests/
  ```
**Para rodar os Testes Automatizados:**
  ```Bash
  python -m pytest tests/
  ```
👨‍💻 Autor
Desenvolvido por Eduardo Fernandes.
