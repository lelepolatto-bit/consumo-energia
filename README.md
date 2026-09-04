#  Calculadora de Consumo de Energia

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![GitHub](https://img.shields.io/badge/GitHub-Repositório-181717?logo=github&logoColor=white)
![Energia](https://img.shields.io/badge/Energia-Consumo%20Consciente-F7B500?logo=lightning&logoColor=black)
![Licença](https://img.shields.io/badge/licença-MIT-green)

##  Sobre o projeto

Este projeto é uma calculadora de consumo elétrico desenvolvida para estimar quanto um aparelho consome de energia por mês. A pessoa informa o nome do aparelho, sua potência em watts e o tempo médio de uso diário.

O programa também apresenta uma estimativa do custo mensal, considerando uma tarifa fixa de **R$ 0,75 por kWh**.

##  Tecnologia utilizada

- [Python 3](https://www.python.org/)

##  Fórmula utilizada

O consumo mensal é calculado da seguinte forma:

```text
consumo mensal (kWh) = (potência (W) × horas de uso por dia × 30) / 1000
```

O custo estimado é calculado por:

```text
custo mensal = consumo mensal × tarifa por kWh
```

##  Como executar

1. Tenha o Python 3 instalado.
2. Clone este repositório:

   ```bash
   git clone https://github.com/lelepolatto-bit/consumo-energia.git
   ```

3. Entre na pasta do projeto:

   ```bash
   cd consumo-energia
   ```

4. Execute o programa:

   ```bash
   python3 app.py
   ```

##  Exemplo de uso

```text
 Calculadora de Consumo de Energia 

Nome do aparelho: Geladeira
Potência do aparelho (W): 100
Tempo médio de uso diário (horas): 15

--- Resultado ---
Aparelho: Geladeira
Consumo estimado: 45.00 kWh/mês
Custo estimado: R$ 33.75/mês
(Tarifa considerada: R$ 0.75 por kWh)
```

##  Estrutura do projeto

```text
consumo-energia/
├── app.py
└── README.md
```

##  Atividade acadêmica

Projeto desenvolvido para a **Agenda 05 — Desenvolvimento de Sistemas I**, com o objetivo de praticar algoritmos, programação em Python, Git e GitHub.

