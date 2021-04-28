import sqlite3
import pandas as pd
import bar_chart_race as bcr 


connection = sqlite3.connect('Vaccine.db')
cursor = connection.cursor()
cursor.execute("select * from Moderna_allocation")
modernalist = cursor.fetchall()
#print(moderna)
Jurisdiction = []
Week_allocation = []
first_dose = []
second_dose = []
for idx in range(0, len(modernalist)):
    Jurisdiction.append(modernalist[idx][0])
for idx in range(0, len(modernalist)):
    Week_allocation.append(modernalist[idx][1])
for idx in range(0, len(modernalist)):
    first_dose.append(modernalist[idx][2])
for idx in range(0, len(modernalist)):
    second_dose.append(modernalist[idx][3])
cursor.execute("select * from Pfizer_allocation")
pfizerlist = cursor.fetchall()
#print(moderna)
Jurisdiction = []
Week_allocation = []
first_dose = []
second_dose = []
for idx in range(0, len(pfizerlist)):
    Jurisdiction.append(pfizerlist[idx][0])
for idx in range(0, len(pfizerlist)):
    Week_allocation.append(pfizerlist[idx][1])
for idx in range(0, len(pfizerlist)):
    first_dose.append(pfizerlist[idx][2])
for idx in range(0, len(pfizerlist)):
    second_dose.append(pfizerlist[idx][3])

pfizer = pd.DataFrame({'Jurisdiction':Jurisdiction ,'Week of Allocations': Week_allocation,'1st Dose Allocations':first_dose,'2nd Dose Allocations':second_dose})
moderna = pd.DataFrame({'Jurisdiction':Jurisdiction ,'Week of Allocations': Week_allocation,'1st Dose Allocations':first_dose,'2nd Dose Allocations':second_dose})

pfizer.columns=['Jurisdiction','Week of Allocations','pfizer_first','pfizer_second']
total_long = pd.merge(moderna,pfizer, on=['Jurisdiction','Week of Allocations'],how='left')
total_long['total_allocation']=total_long['1st Dose Allocations']+total_long['pfizer_first']
total_long=total_long.drop(columns=['1st Dose Allocations','2nd Dose Allocations','pfizer_first','pfizer_second'])
total_short = total_long.pivot_table(index=['Week of Allocations'],columns=['Jurisdiction'],values=['total_allocation'])
total_short = total_short.sort_values(by=['Week of Allocations'])

total_short['total_allocation']=total_short['total_allocation'].cumsum()

bcr.bar_chart_race(
    df=total_short, 
    filename='race_plot.html', 
    orientation='h', 
    sort='desc', 
    n_bars=10, 
    fixed_order=False, 
    fixed_max=True, 
    steps_per_period=50, 
    period_length=500, 
    end_period_pause=0,
    interpolate_period=False, 
    period_label={'x': .98, 'y': .3, 'ha': 'right', 'va': 'center'}, 
    #period_template='%B %d, %Y', 
    period_summary_func=lambda v, r: {'x': .98, 'y': .2, 
                                          's': f'Total Allocation: {v.sum():,.0f}', 
                                          'ha': 'right', 'size': 11}, 
    perpendicular_bar_func='median', 
    colors='dark12', 
    title='Top 10 Dose Allocation', 
    bar_size=.95, 
    bar_textposition='inside',
    bar_texttemplate='{x:,.0f}', 
    bar_label_font=7, 
    tick_label_font=7, 
    #tick_template='{x:,.0f}',
    shared_fontdict=None, 
    scale='linear', 
    fig=None, 
    writer=None, 
    bar_kwargs={'alpha': .7},
    fig_kwargs={'figsize': (6, 3.5), 'dpi': 144},
    filter_column_colors=False) 
  
