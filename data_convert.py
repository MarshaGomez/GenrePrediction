import csv
import preprocessor as p

with open('./binaryOneGenre.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    file_name = 0
    count=[0,0,0,0,0,0,0,0,0,0,0,0]
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            #print(row[0] + "\n")
            print(str(count) + "\n")
            option = row[1]
            if count[0]<100:
                if option == "Puzzle":
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Puzzle/" + str(file_name) + ".txt", "w+") as f:
                        count[0]=count[0]+1
                        f.write(row[0])
                        f.close()
            elif count[1]<100:
                if option =='Adventure': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Adventure/" + str(file_name) + ".txt", "w+") as f:
                        count[1]=count[1]+1
                        f.write(row[0])
                        f.close()
            elif count[2]<100:
                if option =='Action': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Action/" + str(file_name) + ".txt", "w+") as f:
                        count[2]=count[2]+1
                        f.write(row[0])
                        f.close()
                  
            elif count[3]<100:
                if option =='RPG': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_RPG/" + str(file_name) + ".txt", "w+") as f:
                        count[3]=count[3]+1
                        f.write(row[0])
                        f.close()
                    
            elif count[4]<100:
                if option =='Simulation': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Simulation/" + str(file_name) + ".txt", "w+") as f:
                        count[4]=count[4]+1
                        f.write(row[0])
                        f.close()
                  
            elif count[5]<100:
                if option =='Strategy': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Strategy/" + str(file_name) + ".txt", "w+") as f:
                        count[5]=count[5]+1
                        f.write(row[0])
                        f.close()
                  
            elif count[6]<100:
                if option =='Shooter': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Shooter/" + str(file_name) + ".txt", "w+") as f:
                        count[6]=count[6]+1
                        f.write(row[0])
                        f.close()
                   
            elif count[7]<100:
                if option =='Sports': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Sport/" + str(file_name) + ".txt", "w+") as f:
                        count[7]=count[7]+1
                        f.write(row[0])
                        f.close()
               
            elif count[8]<100:
                if option =='Racing': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Racing/" + str(file_name) + ".txt", "w+") as f:
                        count[8]=count[8]+1
                        f.write(row[0])
                        f.close()
                    
            elif count[9]<100:
                if option =='Educational': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Educational/" + str(file_name) + ".txt", "w+") as f:
                        count[9]=count[9]+1
                        f.write(row[0])
                        f.close()
                  
            elif count[10]<100:
                if option =='Fighting': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_Fighting/" + str(file_name) + ".txt", "w+") as f:
                        count[10]=count[10]+1
                        f.write(row[0])
                        f.close()
                  
            elif count[11]<100:
                if option =='BoardGames': 
                    with open("c:/Users/Matilde/Desktop/GitHub/datamin/GenrePrediction/dataset/dir_BoardGames/" + str(file_name) + ".txt", "w+") as f:
                        count[11]=count[11]+1
                        f.write(row[0])
                        f.close()
                   
            file_name += 1
            line_count += 1
    print(f'Processed {line_count} lines.')