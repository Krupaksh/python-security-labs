def main():
    fileread()

def fileread():

    count = 0
    error = 0
    warning = 0
    info = 0   
    with open ("Serverlog.txt" , "r") as file:
        for line in file:
            cleanstring= line.strip().lower()
            count += 1 
            if cleanstring.startswith("error") :
                 error += 1
            elif cleanstring.startswith("warning") :
                 warning += 1
            elif cleanstring.startswith("info") :
                info += 1
        
        print("No of lines : ", count)
        print("No of errors : ", error)
        print("No of warnings : ", warning)
        print("No of info : ", info)



if __name__ == "__main__" :
    main() 