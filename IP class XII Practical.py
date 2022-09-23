import pandas as pd
import registerations
import graphs
import election
import time
d_history=pd.read_csv('history.csv')
d_rep=pd.read_csv('representatives.csv')
print('')
print('='*20+' WELCOME TO ELECTION PORTAL OF INDIA '+'='*20)
time.sleep(1)
print('')
parties=[]
parties_h=list(d_history.columns)
parties_h.remove('Year')
parties_h.remove('votes')
parties_h.remove('Participation')
functions=['Register Voter','Register Candidate','Conduct elections','Analysis','Results of last conducted elections','Exit']
analysis=['Comparision between parties over the years', 'Particular party performance', 'Participation of people in elections']
for i in d_rep['Party Name']:
    if i not in parties:
        parties.append(i)
    else:
        continue
start=True
while start==True:
    print('')
    print('*'*50)
    print('')
    print('              LIST OF ALL FUNCTIONS')
    print('')
    print('*'*50)
    print('')
    print('')
    for i in range(len(functions)):
        print(str(i+1)+') '+functions[i])
        print('')
    print('*'*50)
    print('')
    time.sleep(1)
    resp=input('Select the function by number... ')
    time.sleep(1)
    print('')
    try:
        if int(resp)==6:
            print('Exiting in 3...')
            time.sleep(1)
            print('2...')
            time.sleep(1)
            print('1...')
            time.sleep(1)
            print('')
            print('******* *      *      *      *     *  *    *   *     *  ***  *    * ')
            print('   *    *      *     * *     * *   *  *  *      *   *  *   * *    * ')
            print('   *    ********    *****    *  *  *  * *        * *   *   * *    * ')
            print('   *    *      *   *     *   *   * *  *  *        *    *   * *    * ')
            print('   *    *      *  *       *  *    **  *   *       *    *   * *    * ')
            print('   *    *      * *         * *     *  *    *      *     ***   ****  ')
            start=False
        elif int(resp)==3:  
            year=int(input('Enter current year election conduction...'))
            d_last=d_history.loc[len(d_history.index)-1]
            if (year)-(d_last['Year']) < 5:
                print('')
                print('='*90)
                print('Elections are conducted within 5 years gap')
                print('Last elections were conducted in '+str(int(d_last['Year']))+' hence, elections cant be conducted right now')
                print('='*90)
                print('')
                overrude=str(input('Overrude the the gap (Y/N)?... '))
                print('')
                if overrude in 'yY':
                    print('Beginning elections in 3...')
                    time.sleep(1)
                    print('2...')
                    time.sleep(1)
                    print('1...')
                    time.sleep(1)
                    print('NOW!!!')
                    time.sleep(1)
                    print('')
                    d=election.run_election()
                    sorted_dict = sorted(
                                  d.items(),
                                  key = lambda kv: kv[1], reverse=True)
                    d=dict(sorted_dict)
                    total_votes=0
                    for i in d:
                        total_votes+=d[i]
                    graphs.insert_into(year,d)
                    print('')
                    res=str(input('Display results (Y/N)?... '))
            
                    if res in 'yY':
                        print('')
                        print('='*70)
                        for i in d:
                            print(i+' : '+str(int(d[i])))
                        print('Total votes casted : '+str(total_votes))
                        print('='*70)
                        print('')
                        time.sleep(10)
                    else:
                        time.sleep(1)
                        continue
                
                else:
                    time.sleep(1)
                    continue
            else:
                print('Beginning elections in 3...')
                time.sleep(1)
                print('2...')
                time.sleep(1)
                print('1...')
                time.sleep(1)
                print('NOW!!!')
                time.sleep(1)
                print('')
                d=election.run_election()
                sorted_dict = sorted(
                                  d.items(),
                                  key = lambda kv: kv[1], reverse=True)
                d=dict(sorted_dict)
                total_votes=0
                for i in d:
                    total_votes+=d[i]
                graphs.insert_into(year,d)
                print('')
                res=str(input('Display results (Y/N)?... '))
            
                if res in 'yY':
                    print('')
                    print('='*70)
                    for i in d:
                        print(i+' : '+str(int(d[i])))
                    print('Total votes casted : '+str(total_votes))
                    print('='*70)
                    print('')
                    time.sleep(10)
                else:
                    time.sleep(1)
                    continue
        elif int(resp)==5:
            graphs.view()
            
            time.sleep(10)
        elif int(resp)==1:
            print(registerations.reg_voter())
            print('')
            time.sleep(1)
        elif int(resp)==2:
            print(registerations.reg_cand())
            print('')
            time.sleep(1)
        elif int(resp)==4:
            print('')
            print('='*10,'Select mode of analysis by its number','='*10)
            print('')
            for i in range(len(analysis)):
                print(str(i+1)+')',analysis[i])
                print('')
            print('='*(len('='*10+'Select mode of analysis by its number'+'='*10)+2))
            print('')
            ana=int(input())
            print('')
            time.sleep(1)
            if ana==1:
                graphs.graph(party='all',participation=False)
                time.sleep(1)
            elif ana==2:
                print('='*10+' Select a party by its indicated number '+'='*10)
                print('')
                for i in range(len(parties_h)):
                    print(str(i+1)+') '+parties_h[i])
                print('')
                print('='*len('='*10+' Select a party by its indicated number '+'='*10))
                print('')
                party=int(input())
                party=parties_h[party-1]
                graphs.graph(party=party,participation=False)
                time.sleep(1)
            elif ana==3:
                graphs.graph(party=None,participation=True)
                time.sleep(1)
        else:
            print('Enter input correctly...')
            print('Going to sleep mode for 30 seconds...')
            time.sleep(20)
            for i in range(0,10):
                print(10-i)
                time.sleep(1)
    except:
        print('Enter input correctly...')
        print('Going to sleep mode for 30 seconds...')
        time.sleep(20)
        for i in range(0,10):
            print(10-i)
            time.sleep(1)
        
            
        
        
                    
                

        
    
    
    

