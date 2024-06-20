# simple voting system

candidate_1="ram" #input("enter the name of candidate_1  :")
candidate_2="sham" #input("enter the name of candidate_2  :")

print("________________________________________")


candidate_1_votes=0
candidate_2_votes=0

voters_id=[1,2,3,4,5,6,7,8,9,10]

number_of_voters=len(voters_id)


while True:
    if voters_id==[]:
        print("close voting session")
        if candidate_1_votes>candidate_2_votes:
            
            percent=(candidate_1_votes/number_of_voters)*100
            winby=number_of_voters-candidate_1_votes
            print(candidate_1,"has won","with",percent,"% votes")
            print(candidate_1,"has won by",winby,"votes")
            break
            
        elif candidate_2_votes>candidate_1_votes:
            
            percent=(candidate_2_votes/number_of_voters)*100
            winby=number_of_voters-candidate_2_votes
            print(candidate_2,"has won","with",percent,"% votes") 
            print(candidate_2,"has won by",winby,"votes")
            break   
    
    else:
        voter=int(input("Enter the your voter id  :"))
        
        
        if voter in voters_id:
            print("This are the candidates")
            voters_id.remove(voter)
            print(f"1.{candidate_1}\n2.{candidate_2}  \n3. For exit")
                        
            choice=int(input("enter your choice to vote candidate : "))
            
            
            if choice==1:
                print("you are voted for",candidate_1)
                candidate_1_votes+=1
                print("thank you for your vote")
                print("_______________________________________")
                
            elif choice==2:
                print("you are voted for",candidate_2)
                candidate_2_votes+=1
                print("thank you for your vote")
                print("______________________________________")
                
            
                
                
            elif choice!=1 and 2 and 3:
                print("invalid choice")
                print("________________________________")
                                
        elif voter not in voters_id:
            print("you are not allow to vote or you are already voted") 
            
                   