print ("Programa de evaluación de notas de alunos")
nota_alumno=input("Introduce la nota del alumno:")
def evaluacion (nota):
    valoracion="aprobado"
    if nota<5:
        valoracion="supenso"
    return valoracion
print (evaluacion(int(nota_alumno)))