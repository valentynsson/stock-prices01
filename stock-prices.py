




def get_data_list(file_data):
    

    adj_close = 0
    volume = 0

    for words in file_data:
    
        words = words.strip()
        words = words.split(",")
        
        adj_close = words.index("Adj Close")
        volume = words.index("Volume")
        break
    
   
    return 0



def main():
    file_ = open("GOOG.txt", "r")
    sort_from_list = get_data_list(file_)

main()