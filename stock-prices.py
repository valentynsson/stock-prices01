

def get_data_list(file_data):
    
    adj_close = 0
    volume = 0

    big_data = []
    for words in file_data:
    
        words = words.strip()
        words = words.split(",")
        
        adj_close = words.index("Adj Close")
        volume = words.index("Volume")
        break
    
    
    for line_by_line in file_data:
        
        line_by_line = line_by_line.strip()
        line_by_line = line_by_line.split(",")
        big_data.append(line_by_line)
    
    
    check_date = []
    date_list = []
    current_date = ""
    for i in big_data:
        current_date = i[0][0:7]
        
        for c in big_data:
            if current_date == c[0][0:7]:
                check_date.append(c)
            
        date_list.append(check_date)
        break  
            
    for k in date_list:
        print(k)    
    
    return 0




def main():
    file_ = open("GOOG.txt", "r")
    sort_from_list = get_data_list(file_)

main()