import Matrix as Sp
from stress_kruskal import *
import time
import grafics.plot as gp
from stress_kruskal import paralleled, unparalleled


def Main(name):
    '''name = nome do arquivo que será feito o cáculo'''

    link_Mo = 'C:\\Users\\ander\\Documents\\paiva-main\\DataFiles\\'+ name +'.data'  # caminnho da matriz original
    link_Mp = 'C:\\Users\\ander\\Documents\\paiva-main\\resultados\\proj-'+ name +'.data'  # caminho da matriz projetada

    Mo = Sp.form_matrix(open(link_Mo, 'r'), 1000)  # transforma a matriz original em seu dataset puro
    Mp = Sp.form_matrix(open(link_Mp, 'r'), 1000)  # transforma matriz projetada em seu dataset puro

    return Mo, Mp  # retorna matriz original e projetada

def liken_time(Mo, Mp, name): #função para comparar tempos de execução do codigo paralelizado e não paralelizado
    time_init1 = time.time() #tempo de inicio do calculo paralevlizado
    stress_paralleled = paralleled.somatorio(Mo, Mp)
    time_init2 = time.time() #tempo de fim do calculo paralelizado e inicio do não paralelizado
    stress_unparalleled = unparalleled.somatorio(Mo, Mp)
    time_init3 = time.time() #tempo de fim do calculo não paralelizado

    gp.plot(name, time_init2-time_init1, time_init3-time_init2)


nomes = ['multifield.0099-normcols.bin-200000']
for nome in nomes:
    Matriz_original, Matriz_projetada = Main(nome)

    #liken_time(Matriz_original, Matriz_projetada, nome) # para comparar o codigo paralelizado e o não

    stress = paralleled.somatorio(Matriz_original, Matriz_projetada) # calcula o stress apenas

    print(f'stress1: {stress}')



#os.system('shutdown -s')