import pandas as pd
import matplotlib.pyplot as pl
import time
def insert_into(year,dictionary):
    d=dictionary
    d_history=pd.read_csv("history.csv")
    d_voter=pd.read_csv("voters.csv")
    votes_casted=0
    for i in d:
        votes_casted+=d[i]
    total_voters=len(d_voter)
    participation=(votes_casted/total_voters)*100
    d_history['Participation']=round((d_history['votes']/total_voters)*100,2)
    insert=[year,votes_casted,d['Bhartiya Janta Party'],d['Bahujan Samaj Party'],
            d['Communist Party of India'],
            d['Communist Party of India (Marxist)'],
            d['Indian National Congress'],
            d['Nationalist Congress Party'],
            d['Independent'],
            votes_casted-(d['Bhartiya Janta Party']+d['Bahujan Samaj Party']+
            d['Communist Party of India']+
            d['Communist Party of India (Marxist)']+
            d['Indian National Congress']+
            d['Nationalist Congress Party']+
            d['Independent']),participation]
    d_history.loc[len(d_history.index)]=insert
    d_history.to_csv('history.csv',index=False)
    
def graph(party=None,participation=False):
    d_history=pd.read_csv('history.csv')
    d_history['Year']=d_history['Year'].astype(float).astype(int)
    if party==None and participation==True:
        d_history.plot(x='Year',y='Participation')
        d_part=d_history[['Participation','Year']]
        d_lastone=d_part.loc[len(d_part)-1]
        d_secondlast=d_part.loc[len(d_part)-2]
        if d_lastone['Participation'] > d_secondlast['Participation']:
            print('')
            print('='*80)
            print('More people participated in last elections than in previous one...')
            time.sleep(1)
            print("Participation's on rise!!!")
            print('='*80)
            print('')
        elif d_lastone['Participation'] < d_secondlast['Participation']:
            print('')
            print('='*80)
            print('Less people participated in last elections than in previous one...')
            time.sleep(1)
            print("Participation suffered setback!!!")
            print('='*80)
            print('')
        else:
            print('')
            print('='*80)
            print('Same number of people participated in last elections than in previous one...')
            time.sleep(1)
            print("Participation's stable!!!")
            print('='*80)
            print('')
        a=str(input('View detailed graph of Participation (Y/N)?...'))
        pl.xlabel("Year")
        pl.ylabel("Percentage(%) vote casted")
        pl.title('Participation of People')
        if a in 'yY':
            pl.show()
        else:
            None
    elif party=='all' and participation==False:
        d_history.plot.bar(x='Year',y=['Bhartiya Janta Party','Bahujan Samaj Party',
                                   'Communist Party of India','Communist Party of India (Marxist)',
                                   'Indian National Congress','Nationalist Congress Party','Independent'])
        
        pl.title('Comparision between parties')
        pl.ylabel('Votes recieved by party')
        pl.show()
    elif participation==False and party!=None and party!='all':
        s=party+' (%)'
        d_party=d_history[[party,'Year']]
        d_lastone=d_party.loc[len(d_party)-1]
        d_secondlast=d_party.loc[len(d_party)-2]
        if d_lastone[party] > d_secondlast[party]:
            print('')
            print('='*80)
            print('Party recieved more votes in last election than previous one...')
            time.sleep(1)
            print("Party's on rise!!!")
            print('='*80)
            print('')
        elif d_lastone[party] < d_secondlast[party]:
            print('')
            print('='*80)
            print('Party recieved less votes in last election than previous one...')
            time.sleep(1)
            print("Party suffered setback!!!")
            print('='*80)
            print('')
        else:
            print('')
            print('='*80)
            print('Party recieved same votes in last election as in previous one...')
            time.sleep(1)
            print("Party's stable!!!")
            print('='*80)
            print('')
        a=str(input('View deatiled graph (Y/N)?...'))
        d_history[s]=(d_history[party]/d_history['votes'])*100
        d_history.plot(x='Year',y=s)
        pl.title('Party performance over years')
        pl.ylabel('% votes recieved by '+party)
        pl.xlabel('Year')
        if a in 'yY':
            pl.show()
        else:
            None
    elif party=='all' and participation==True:
        d_history.plot(x='Year',y='Participation')
        pl.xlabel("Year")
        pl.ylabel("Percentage(%) vote casted")
        pl.title('Participation of People')
        d_history.plot.bar(x='Year',y=['Bhartiya Janta Party','Bahujan Samaj Party',
                                   'Communist Party of India','Communist Party of India (Marxist)',
                                   'Indian National Congress','Nationalist Congress Party','Independent'])
        pl.title('Comparision between parties')
        pl.ylabel('Votes recieved by party')
        pl.show()
    elif participation==True and party!=None and party!='all':
        d_history.plot(x='Year',y='Participation')
        pl.xlabel("Year")
        pl.ylabel("Percentage(%) vote casted")
        pl.title('Participation of People')
        s=party+' (%)'
        d_history[s]=(d_history[party]/d_history['votes'])*100
        d_history.plot(x='Year',y=s)
        pl.title('Party performance over years')
        pl.ylabel('% votes recieved by '+party)
        pl.xlabel('Year')
        pl.show()
def view():
    d_history=pd.read_csv('history.csv')
    d_last=d_history.loc[len(d_history.index)-1]
    year=int(d_last['Year'])
    bjp=int(d_last['Bhartiya Janta Party'])
    bsp=int(d_last['Bahujan Samaj Party'])
    cpi=int(d_last['Communist Party of India'])
    cpim=int(d_last['Communist Party of India (Marxist)'])
    inc=int(d_last['Indian National Congress'])
    ncp=int(d_last['Nationalist Congress Party'])
    ind=int(d_last['Independent'])
    oth=int(d_last['Others'])
    print('')
    print('='*30,str(year)+' RESULTS '+'='*30)
    print('Bhartiya Janta Party :',bjp)
    print('Bahujan Samaj Party :',bsp)
    print('Communist Party of India :',cpi)
    print('Communist Party of India (Marxist) :',cpim)
    print('Indian National Congress :',inc)
    print('Nationalist Congress Party :',ncp)
    print('Independent :',ind)
    print('Others :',oth)
    print('='*len('='*30+str(year)+' RESULTS '+'='*30))
    print('')
#graph(participation=True)

#graph(party='Others',participation=True)

    
