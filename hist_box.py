def criar_hist(list_vars, list_labels, titulo, limit, save=False, fig_size=(10, 5), limit_left=0, l_range=0):
    
    Cor1='#fcbf49'
    Cor1_1='#f77f00'
    Cor2_1='#f77f00'
    cor_borda='w'
    
    cor_borda='w'
    ratios=[]
    n=0
    for i in range(0, len(list_vars)*3):
        n=n+1
        if n==3:
            ratios.append(.2)
            n=0
        elif n==1:
            ratios.append(3)
        else: ratios.append(1)
            
    fig_size2=(fig_size[0],fig_size[1]*(len(list_vars)))
    fig, ax = plt.subplots(len(list_vars)*3, 1, gridspec_kw={'height_ratios': ratios}, figsize=fig_size2)
    #axxis
    limit=limit
    for i in range(0, len(list_vars)*3):
        ax[i].set_xlim(limit_left, limit, emit=True)
    #-----------------------------------------------------------
    n=0
    for i in range(0, len(list_vars)*3):
        n=n+1
        if n==3:
            an=list_vars[int((i-1)/3)].mean()
            an2=list_vars[int((i-1)/3)].median()
            plt.setp(ax[i].spines.values(), color='w')
            ax[i].tick_params(axis='y', colors='w', length=0)
            ax[i].tick_params(axis='x', colors='w', length=0)
            ax[i].annotate(('Média = '+str(an)[0:str(an).find('.')+3]), xy=(0.2, 0.6), xytext=(0.3,0.3),
                            xycoords='axes fraction', 
                            arrowprops={'color':Cor1_1,  'ConnectionStyle':'arc', 
                                         'arrowstyle':'-', 'linewidth':2})
            ax[i].annotate(('Mediana = '+str(an2)[0:str(an2).find('.')+3]), xy=(0.5, 0.6), xytext=(0.6,0.3),
                            xycoords='axes fraction',
                            arrowprops = {'linestyle':':', 'color':'k',  'ConnectionStyle':'arc',
                                            'arrowstyle':'-', 'linewidth':2})
            n=0
        elif n==1:
            #print(i)
            plt.setp(ax[i].spines.values(), color='w')

            p1=ax[i].hist(list_vars[int(i/3)], bins=35, color=Cor1, edgecolor=cor_borda, zorder=3, range=(l_range, limit))
            ax[i].grid(True, axis='y', zorder=1, alpha=.2)
            ax[i].set_ylabel(list_labels[int(i/3)],fontsize=14)
        else:
            #print(i)
            #construindo boxplot
            #ax[1]=fig.add_subplot(612)
            plt.setp(ax[i].spines.values(), color='w')

            box_aplha=.4

            l=ax[i].boxplot(list_vars[int((i-1)/3)], vert=False, widths=.8, medianprops = dict(linestyle=':', 
                            linewidth=2.5, color='k'), showmeans=True, meanline=True, 
                            meanprops = dict(linestyle='-', linewidth=2.5, color=Cor2_1))

            ax[i].set_yticklabels([], color='w')
            ax[i].set_xticklabels([], color='w')

            ax[i].grid(True, axis='x')

    a=titulo
    a=a.replace('Apos_hist: ', '')
    a=a.replace('Pens_hist: ', '')
    a=a.replace('Ativ_hist: ', '')
    a=(a[0].upper()+a[1:])
    ax[0].set_title(a, fontsize=16, pad=25)
    

    if save==True:

        plt.savefig(('Gráficos gerados/'+titulo+'.png'), bbox_inches='tight')

