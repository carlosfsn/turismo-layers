# 🌍 Turismo Layers

Sistema acadêmico desenvolvido para demonstrar a aplicação prática da **Arquitetura em Camadas (Layered Architecture)** em um contexto de agência de turismo.

---

## 📌 Objetivo

Demonstrar, de forma prática, como a Arquitetura em Camadas organiza um sistema real, separando:

* Interface (UI)
* Casos de uso (Application)
* Regras de negócio (Domain)
* Persistência (Infrastructure)

---

## 🏗 Arquitetura Utilizada

```
UI → Application → Domain → Infrastructure
```

### 📂 Estrutura do Projeto

```
turismo/
│
├── ui/                # Interface com o usuário
├── app/               # Casos de uso
├── domain/            # Regras de negócio
├── infra/             # Persistência (SQLite)
├── main.py            # Ponto de entrada
```

---

## 🧠 Conceitos Aplicados

* Separação de responsabilidades
* Baixo acoplamento
* Alta coesão
* Princípio da Inversão de Dependência (DIP)
* Uso de interfaces (contratos de repositório)

---

## 🔄 Exemplo de Fluxo – Cadastro de Cliente

1. UI recebe os dados
2. Application executa o caso de uso
3. Domain valida regras
4. Infrastructure salva no banco

---

## 🛠 Tecnologias Utilizadas

* Python 3
* SQLite
* Programação Orientada a Objetos

---

## ▶ Como Executar

```bash
git clone https://github.com/carlosfsn/turismo-layers
cd turismo-layers
python main.py
```

---

## 👨‍💻 Equipe / Contatos

### Carlos Sicsu

📧 [carlosfnsicsu@gmail.com](mailto:carlosfnsicsu@gmail.com)
🔗 [https://www.linkedin.com/in/carlos-sics%C3%BA-131980236/](https://www.linkedin.com/in/carlos-sics%C3%BA-131980236)


### Emilly Morais

📧 [moraisemilly358@gmail.com](mailto:moraisemilly358@gmail.com)
🔗 [http://linkedin.com/in/emilly-morais-bulcão-1a17bb2b2/](http://linkedin.com/in/emilly-morais-bulcão-1a17bb2b2)


### Jean Oliveira

📧 [jeanoliveiraes1@gmail.com](mailto:jeanoliveiraes1@gmail.com)
🔗 [https://www.linkedin.com/in/jean-oliveira-8642a4280/](https://www.linkedin.com/in/jean-oliveira-8642a4280/)


### Anny Beatriz

📧 [beatrizteixeira3913@gmail.com](mailro:beatrizteixeira3913@gmail.com)
🔗 [https://www.linkedin.com/in/beatriz-t/](https://www.linkedin.com/in/beatriz-t/)


### Flavio Holanda

📧 [flavicarvalho9029@gmail.com](mailto:flavicarvalho9029@gmail.com)
🔗 [https://www.linkedin.com/in/flávio-carvalho-79294a217/](https://www.linkedin.com/in/flávio-carvalho-79294a217/)

---

## 🎓 Finalidade Acadêmica

Projeto desenvolvido para disciplina de **Arquitetura de Software**, demonstrando que arquitetura é uma decisão estrutural baseada em necessidades reais e princípios de engenharia.

---
