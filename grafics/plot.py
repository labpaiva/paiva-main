import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def plot(name_dataset, times_paral, times_nparal, save = False):
    #print('plotando graficos de tempo')
    plt.title(f'tempo de processamento do {name_dataset}')

    red_patch = mpatches.Patch(color='red', label='Não paralelizado')
    green_patch = mpatches.Patch(color='green', label='Paralelizado')
    plt.legend(handles=[green_patch, red_patch])

    plt.ylabel('tempo por segundo')

    plt.bar(name_dataset+' paralelizado', [times_paral], color='green')
    plt.bar(name_dataset+' original', [times_nparal], color='red')

    if save == True:
        plt.savefig(name_dataset+'.png')

    plt.show()

plot('fibers', 724.08, 24557, True)