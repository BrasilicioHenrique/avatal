from dataclasses import dataclass

@dataclass
class Data:
    dia: int = int(input("dia de nascimento: "))
    mes: int = int(input("mes de nascimento: "))
    ano: int = int(input("ano de nascimento: "))


@dataclass
class Estudante:
    nome: str = str(input("nome e sobrenome: "))
    matricula: str = int(input("matricula: "))
    data_nascimento: Data = f"{Data.dia}/{Data.mes}/{Data.ano}"
