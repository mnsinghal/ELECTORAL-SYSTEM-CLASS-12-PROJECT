import pandas as pd
import time
import os


def run_election():
    d_vote={}
    df_voter = pd.read_csv("voters.csv")
    df_representative = pd.read_csv("representatives.csv")


    '''code for the election conduction'''
    
    run=True
    done_cand=[]
    while run==True:
        v_id=input('Please enter voter ID or type "end" to end the elections... ')
        if v_id.upper() not in done_cand:
            if v_id=='end':
                #Here code for saving the poll result don't write in this go at the end
                run=False
                continue
            s1=df_voter.loc[df_voter['Voter ID']== v_id.upper()]
            if s1.empty:
                print("please enter correct voter id")
                continue
            cons=s1['Constituency & State']
            c=""
            for i in cons:
                c=c+i
            cons=c.strip()
            name=s1['Voter name']
            s2=df_representative.loc[df_representative['Constituency & State']==cons]
            party_df=s2[['Party Name','Name of Member']]
            party_df=party_df.reset_index()
            party2=[]
            party=[]
            party_lower=[]
            for i in range(len(party_df)):
                if party_df['Party Name'][i] not in party and party_df['Party Name'][i]!='Independent':
                    party2.append(party_df['Party Name'][i])
                    party.append(party_df['Party Name'][i])
                    party_lower.append(party_df['Party Name'][i].lower())
                elif party_df['Party Name'][i] not in party and party_df['Party Name'][i]=='Independent':
                    party2.append(party_df['Name of Member'][i]+'(Independent)')
                    party.append(party_df['Party Name'][i])
                    party_lower.append(party_df['Party Name'][i].lower())
                else:
                    continue
            n=''
            for i in name:
                n+=str(i)
            print('')
            print('='*25+'Welcome '+str(n).capitalize()+'='*25)
            print('')
            print('Parties/Candidates contesting from you constituency i.e. '+cons)
            print('')
        
            for i in range(0,len(party2)):
                print(str(i+1)+") "+party2[i])
            print('='*len('='*25+'Welcome '+str(n).capitalize()+'='*25))
            print('')
            print("Choose one of them by number or their name")
            print('')
            done=False
            while done==False:
                r=input()
                print('')
                try:
                    r=int(r)
                    r=r-1
                    d_vote[v_id]=party[r]
                    done=True
                except:
                    try:
                        for i in range(0,len(party_lower)):
                            if r.lower()==party_lower[i]:
                                d_vote[v_id]=party[i]
                                done=True
                            else:
                                done=False
                        print("Please enter correctly")
                        
                    except:
                        if done==True:
                            done=False
                            print("Please enter correctly")
                        else:
                            continue
            done_cand.append(v_id.upper())
            print("Thank you your vote registerd")
            print('')
            time.sleep(1)
            os.system('cls')
        else:
            print('')
            print('You can cast vote only once')
            print('')
    

    '''counting votes'''

    voted_parties=[]
    for i in d_vote:
        voted_parties.append(d_vote[i])
    party_name=[]
    for i in df_representative['Party Name']:
        if i not in party_name:
            party_name.append(i)
        else:
            continue
    vote_count={}
    for i in party_name:
        vote_count[i]=voted_parties.count(i)
    return vote_count

#print(run_election())  

