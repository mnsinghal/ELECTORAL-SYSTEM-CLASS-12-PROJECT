import pandas as pd
import time
d_rep=pd.read_csv('representatives.csv')
d_voter=pd.read_csv('voters.csv')
parties=[]
for i in d_rep['Party Name']:
    if i not in parties:
        parties.append(i)
    else:
        continue

parties.remove('Independent')
parties.append('Independent')
def reg_cand(parties=parties,d_rep=d_rep):
    firstName=str(input('Enter your first name.. ')).capitalize()
    lastName=str(input('Enter your last name... ')).capitalize()
    Name=lastName+', '+firstName

    Age=int(input('Enter your Age.. '))
    if Age >= 25 :
        time.sleep(1)
        print('')
        print('='*10+'Welcome '+Name+'='*10)
        print('')
        print('Select your party number or choose independent if candidate is independent')
        print('')
        for i in range(len(parties)):
            print(str(i+1)+') '+parties[i])
        print('')
        print('='*(len(list(Name))+28))
        print('')
        party=int(input(''))
        print('')
        party=parties[party-1]
    else:
        print('Minimum age for contesting elections is 25 years hence you are not eligible')
        return None
    cons=str(input('Enter your contituency...')).capitalize()
    state=str(input('Enter your state...')).capitalize()
    constituency=cons+' ('+state+')'
    
    d_rep.loc[len(d_rep.index)]=[Name,constituency,party]
    print('')
    print('='*10+'Your details'+'='*10)
    print('Name : '+Name)
    print('Party Name : '+party)
    print('Constituency : '+constituency)
    print('='*32)
    print('')
    confirm=str(input('Confirm registeration (Y/N)?...'))
    if confirm in 'yY':
        
        d_rep.to_csv('representatives.csv',index=False)
        time.sleep(1)
        return 'Registeration done successfully!!'
    else:
        return None
def reg_voter(d_voter=d_voter):
    Name=str(input('Enter your name... ')).capitalize()
    print('')
    print('='*10+'Welcome '+Name+'='*10)
    print('')
    Age=int(input('Enter you Age... '))
    if Age>=18:
        cons=str(input('Enter your constituency... ')).capitalize()
        state=str(input('Enter your state... ')).capitalize()
        constituency=cons+' ('+state+')'
    else:
        print('Legal age for voters is 18 hence you are not eligible')
    vid=cons.upper()[:2]+str(len(d_voter.index)+1)
    insert=[Name,constituency,vid]
    d_voter.loc[len(d_voter.index)]=insert
    print('')
    print('='*10+'Your Details'+'='*10)
    print('Name : ',Name)
    print('Age : ',Age)
    print('Constituency : ',constituency)
    print('Voter ID : ',vid)
    print('='*32)
    print('')
    
    confirm=str(input('Confirm Registeration (Y/N)?... '))
    if confirm in 'yY':
        d_voter.to_csv('voters.csv',index=False)
        time.sleep(1)
        return 'Registeration done successfully!!'
    else:
        return None
    
    
#print(reg_cand())
#print(reg_voter())

























        
        
        
    
    
    
    
