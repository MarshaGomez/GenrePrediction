import csv
import preprocessor as p


def createModelFiles(filename, type):
    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        file_name = 0
        i = 0
        count=[0,0,0,0,0,0,0,0,0,0,0,0]
        genres = ['Action', 'Adventure', 'RPG', 'Shooter', 'Puzzle', 'Educational', 'Simulation', 'Strategy', 'Fighting', 'BoardGames', 'Sports', 'Racing']
        for row in csv_reader:
            if line_count == 0:
                print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                option = row[1]

                while (i <= 11):
                    if count[i]<400 and genres[i] == option:
                        option = option if (type=="") else type
                        with open("./data/dataset/"+genres[i]+"/"+option+"/" + str(file_name) + ".txt", "w+") as f:
                            count[i]=count[i]+1
                            f.write(row[0])
                            f.close()
                    i = i+1
                file_name += 1
                i = 0
                line_count += 1
        print(f'Processed {line_count} lines.')


def initProcess():
    # Create Model Principal Files []
    createModelFiles('./data/binaryOneGenre.csv', "")

    #Create Model Other Files 
    createModelFiles('./data/binaryOtherTags.csv', "other")

initProcess()