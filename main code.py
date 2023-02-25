import pandas as pd
from IPython.display import display
from datetime import date , datetime ,timedelta

class book_list:
    def __init__(self,dataframe):
        self.df = dataframe
    def add_book(self,name,author,genre,yop):
        self.name=name
        self.author=author
        self.genre=genre
        self.yop=yop
        self.df.loc[self.name] = [self.author, self.genre, self.yop]
        return self.df
    
    def edit_book(self,editbook):
        if editbook in self.df.index:
            message = '''What do you want to edit in the book
            1. Edit the Author/'s name
            2. Edit the genre
            3. Edit the year of publication '''
            choice = int(input(message))
            if choice == 1:
                author=input("Enter the new author's name:\n")
                self.df.loc[self.name] = [author, self.genre, self.yop]
                print("Book record updated")
            elif choice == 2:
                genre=input("Enter the new genre:\n ")
                self.df.loc[self.name] = [self.author, genre, self.yop]
                print("Book record updated")
            elif choice == 3:
                yop=input("Enter the new year of publication:\n")
                self.df.loc[self.name] = [self.author, self.genre, yop]
                print("Book record updated")
            else:
                print("INVALID CHOICE")
        else:
            print("Sorry, there is no such book present")
            
            
    def remove_book(self,remove_book):
        self.rembook = remove_book
        if self.rembook in self.df.index:
            self.df.drop([self.rembook], inplace = True)
            print(f'{self.rembook} removed from the record')
        else:
            print("There is no such book")
            
class Member:
    def __init__(self,dataframe,name,address,Id,Books_issued=None,Date_issued=None,Deadline=None):
        self.mdf=dataframe
        self.name=name
        self.address = address
        self.id=Id
        self.bookissued=Books_issued
        self.dateissued=Date_issued
        self.deadline=Deadline
        
        self.mdf.loc[self.name]=[self.address,self.id,self.bookissued,self.dateissued,self.deadline]
        
        
    def del_member(self,delname):
        self.delname = delname
        if self.delname not in self.mdf.index:
            print("No record of such user exists")
        else:
            self.mdf.drop([self.delname], inplace = True)
            print(f"{self.delname}'s membership have been successfully cancelled.") 
            
            
    def check_out_book(self,checkbook,booklist,reservelist):
        self.checkbook = checkbook
        self.booklist = booklist
        self.reservelist = reservelist
        if self.checkbook not in booklist.index:
            print("Sorry, the book you requested is not available")
        else:
            a=date.today()             #today's date
            b=date.today()             #storing today's date in another variable to update that later
            b += timedelta(days = 4)   #date after 4 days
            self.mdf.loc[self.name]=[self.address,self.id,self.checkbook,a,b]
            self.bookissued=self.checkbook
            self.dateissued=a
            self.deadline=b

            
            d=0                             #this fragment is for getting the numeric index of the desired book
            for i in self.booklist.index:
                d+=1
                if i == self.checkbook:
                    break
            rob=self.booklist.iloc[b-1]                 #selecting the particular row of the sheet with the desired book  
            self.reservelist.loc[self.checkbook]=[rob[0],rob[1],rob[2]] #reserving the book into another sheet of reserved books
            self.booklist.drop([self.checkbook], inplace = True)
            
            
    def renew_book(self,renbook):
        self.renbook = renbook
        if self.renbook==self.bookissued:
            self.deadline += timedelta(days = 4) #extending the deadline after 4 days
            self.mdf.loc[self.name]=[self.address,self.id,self.checkbook,self.dateissued,self.deadline]
            
        else:
            print("The user was never issued this book")
            
            
    def return_book(self,return_book,booklist,reservelist):
        self.retbook=return_book
        self.booklist = booklist
        self.reservelist = reservelist
        #temp=self.bookissued
        c=0                             #this fragment is for getting the numeric index of the desired book
        for i in self.reservelist.index:
            c+=1
            if i == self.bookissued:
                break
        rob=self.reservelist.iloc[c-1]                 #selecting the particular row of the sheet with the desired book
        self.booklist.loc[self.retbook]=[rob[0],rob[1],rob[2]]     #putting the book into original sheet
        self.mdf.loc[self.name]=[self.address,self.id,None,None,None]
        self.reservelist.drop([self.retbook], inplace = True)
        self.bookissued=None
        self.dateissued=None
        self.deadline=None


def sort_alpha(excel_file, sheet_name=0,index_col=1):
    data=pd.read_excel(excel_file,sheet_name=sheet_name) 
    df=pd.DataFrame(data)

    for i in range (len(df)):
        min_pos=i
        for j in range(i+1,len(df)):
            if df.Title[min_pos] > df.Title[j]:
                min_pos = j            
        df.iloc[i],df.iloc[min_pos]=df.iloc[min_pos],df.iloc[i]
    
    return (df.set_index(index_col))

def view_booklist():
    data=pd.read_excel("Book_Sheet.xlsx",index_col="Title") 
    df=pd.DataFrame(data)
    display(df)
    


        

