from datetime import date
from calendario import Calendario
from disciplina import Disciplina

def obter_feriados_2024_2025() -> list[date]:
    return [
        date(2024, 11, 2),   
        date(2024, 11, 15), 
        date(2024, 12, 25),  
        date(2025, 1, 1), 
    ]

def main():
    try:
        inicio_disciplina = date(2024, 10, 1)  
        fim_disciplina = date(2025, 1, 31)
        feriados = obter_feriados_2024_2025()
        
        calendario = Calendario(inicio_disciplina, fim_disciplina, feriados)

        nome_disciplina = "POO - Outubro a Janeiro"
        horas_por_dia = 2.0 
        disciplina = Disciplina(nome_disciplina, horas_por_dia, calendario)

        horas_totais = disciplina.calcular_horas_totais()
        print(f"\nDisciplina: {nome_disciplina}")
        print(f"Dias uteis no periodo: {calendario.calcular_dias_uteis()}")
        print(f"Horas totais disponiveis para o projeto: {horas_totais:.2f} horas")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

main()