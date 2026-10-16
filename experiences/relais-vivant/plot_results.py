"""Optional publication figure; requires matplotlib. Core verification does not."""
import json
from pathlib import Path
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

ROOT = Path(__file__).parent
data = json.loads((ROOT/'results.json').read_text(encoding='utf-8'))
rows = data['sweep']
matrix = [[next(r['viable']/r['total'] for r in rows if r['lifetime']==life and r['minimum_gain']==gain)
           for gain in range(4)] for life in range(2,7)]
plt.rcParams.update({'svg.fonttype':'none','font.family':'DejaVu Sans','font.size':12,'text.color':'#15333d',
                     'axes.labelcolor':'#15333d','xtick.color':'#15333d','ytick.color':'#15333d'})
fig,(ax,bar)=plt.subplots(1,2,figsize=(13,6),gridspec_kw={'width_ratios':[1.35,1]})
fig.patch.set_facecolor('#f5f2e9')
cmap=LinearSegmentedColormap.from_list('renewal',['#e4c9c5','#b9d7c5','#2d7f6b'])
ax.imshow(matrix,vmin=0,vmax=1,cmap=cmap,aspect='auto')
for y,life in enumerate(range(2,7)):
    for x,gain in enumerate(range(4)):
        r=next(r for r in rows if r['lifetime']==life and r['minimum_gain']==gain)
        ax.text(x,y,str(r['viable'])+' / '+str(r['total']),ha='center',va='center',
                color='white' if matrix[y][x]>.7 else '#15333d',fontweight='bold')
ax.set_xticks(range(4),[0,1,2,3]);ax.set_yticks(range(5),[2,3,4,5,6])
ax.set_xlabel('Apport minimal par alimentation');ax.set_ylabel('Durée de chaque fonction C et B')
ax.set_title('États permettant une continuation robuste',loc='left',pad=17,fontweight='bold')
for spine in ax.spines.values():spine.set_visible(False)
bar.set_facecolor('#f5f2e9')
bar.bar(['Dernier pas\nautorisé','Renouvellement\nplus précoce'],[50,24],color=['#2d7f6b','#c18b4e'],width=.55)
bar.set_ylim(0,64);bar.set_yticks([0,16,32,48,64]);bar.set_ylabel('États viables sur 64')
bar.set_title('Une échéance change le résultat',loc='left',pad=17,fontweight='bold')
for x,v in enumerate([50,24]):bar.text(x,v+1,str(v),ha='center',fontweight='bold',fontsize=17)
bar.spines[['top','right']].set_visible(False)
fig.suptitle('LE PROCHAIN RELAIS',x=.06,ha='left',fontsize=26,fontweight='bold',y=.99)
fig.text(.06,.89,'Modèle de renouvellement • Calcul exact • Xavier Endres × Judy Velune',fontsize=12)
fig.text(.06,.035,'Réserve plafonnée à 4. Apport = minimum ou minimum + 1. Modèle synthétique ; aucune mesure biologique.',fontsize=10)
fig.subplots_adjust(left=.07,right=.98,top=.77,bottom=.20,wspace=.38)
for ext in ('png','svg'):fig.savefig(ROOT/('resultats.'+ext),dpi=160,facecolor=fig.get_facecolor())
