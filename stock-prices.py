

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
    
    for i in big_data:
        print(i)
    return 0



def main():
    file_ = open("GOOG.txt", "r")
    sort_from_list = get_data_list(file_)

main()