import sys
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#importing data from csv file
df=pd.read_csv(r"C:\Users\Shivanagachander\OneDrive\Desktop\messistats.csv")
df_ronaldo = pd.read_csv(r"C:\Users\Shivanagachander\OneDrive\Desktop\ronaldostats.csv")
seasons=df['Seasons']
age=df['Age']
squad=df['Squad']
country=df['Country']
tr=df['Team Rank']
goals_messi=df['Goals of Messi']
assists_messi=df['Assists of Messi']
goals_ronaldo = df_ronaldo['Goals of Ronaldo']
assists_ronaldo=df_ronaldo['Assists of Ronaldo']

#creating Submenu2 for data visualization
def Submenu():
    
    ch = 'y'
    while ch == 'y':
        
        print('\n---------------------------------------------------------------')
        print('                      FOOTBALL STATISTICS ANALYSIS               ')
        print('-----------------------------------------------------------------')
        print('1. Line Graph: Goals per season')
        print('2. Scatter Plot: Age vs Goals')
        print('3. Multi Bar Plot')
        print('4. Pie chart of stats')
        print('5. Line Graph: Assists per Age')
        print('6. Back to main menu ')
        
        ch2 = int(input("Enter your choice from the menu: "))
        
        if ch2==1:
            #line plot for goals vs season
            plt.plot(seasons,goals_messi,label='Messi',color='r',linestyle='-')
            plt.xlabel('Season',fontsize=15)
            plt.ylabel('Goals',fontsize=15)
            plt.xticks(rotation=45)
            plt.plot(seasons,goals_ronaldo,label='Ronaldo',color='blue',linestyle='-')
            plt.legend(loc='upper left')
            plt.title('Goals scored per Season')
            plt.grid(True)
            plt.show()
            print("Shown line plot")
            

        elif ch2==2:
            #scatter plot
            plt.scatter(age,goals_ronaldo,s=100,c='b',label='Ronaldo',marker='*')
            plt.scatter(age,goals_messi,s=100,c='r',label='Messi')
            plt.xlabel('Age',fontsize=16)
            plt.ylabel('Goals',fontsize=16)
            plt.xticks(rotation=45)
            plt.legend(loc='upper left')
            plt.title('Age vs Goals')
            plt.show()
            print("Shown scatter plot chart")
            

        elif ch2==3:
            #multi bar plot
            x1=np.arange(1,18,1)
            x2=x1+0.15
            x3=x2+0.15
            x4=x3+0.15
            plt.bar(x1,assists_messi,tick_label=seasons,width=0.15,label='Assists of Messi')
            plt.bar(x2,assists_ronaldo,tick_label=seasons,width=0.15,label='Assists of Ronaldo')
            plt.bar(x3,goals_messi,tick_label=seasons,width=0.15,label='Goals scored by Messi')
            plt.bar(x4,goals_ronaldo,tick_label=seasons,width=0.15,label='Goals scored by Ronaldo')
            plt.legend()
            plt.xticks(rotation=30)
            plt.show()
             
            
           

        elif ch2==4:
            #pie
            plt.pie(goals_messi,labels=seasons)
            plt.pie(goals_ronaldo,labels=seasons)
            plt.axis='equal'
            plt.title('Pie Plot',fontsize=16)
            plt.legend(loc='lower left')
            plt.show()
            print("Shown pie chart")


        elif ch2==5:
            #line graph for assists per age
            plt.plot(age,assists_messi,label='Messi',color='k',linestyle='-')
            plt.plot(age,assists_ronaldo,label='Ronaldo',color='g',linestyle='-')
            plt.xlabel('Age')
            plt.ylabel('Assits')
            plt.xticks(rotation=30)
            plt.title('Assists provided at age')
            plt.show()
            
            

        elif ch2==6:
            mainmenu()
            
        else:
            print("\nInvalid input")
        
        ch = input("Press 'y' to continue or any other key to go to quit: ")        

    sys.exit()
    
#creating main menu
def mainmenu():
    
    u_ch = 's'
    while u_ch == 's':
        print('\n----------------------------------------------------')
        print('                 FOOTBALL STATISTICS ANALYSIS')
        print('------------------------------------------------------')
        print('                 1. Display Data')
        print('                 2. Data Vizualisation')

        choice=int(input('\n Select an option from the menu : '))
        if choice==1:
            print('    Displaying Data...\n')
            print(df)
            print(df_ronaldo)
            print(df.columns)
            print(df_ronaldo.columns)
            u_ch = input("Enter 's' to continue or any other key to quit: ")
        elif choice==2:
            Submenu()
        else:
            print("\nPlease check your input")


mainmenu()
sys.exit()
        

        

    

