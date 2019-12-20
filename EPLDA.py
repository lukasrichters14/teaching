# English Premier League Data Analysis

def open_file(file_name):
    ''' Opens the file that contains the data and returns that data as a file
    pointer. '''
    
    file_ptr = open(file_name, "r")
    
    return file_ptr


def create_dict(file_ptr):
    ''' Takes a file pointer and creates a dictionary with this format:
        
        {season:{team_name:points}} '''
    
    return_dict = {}
    current_season = "18-19"
    temp_dict = {}
    
    # Goes through each line in the file.
    for i, line in enumerate(file_ptr):
        # i is the index, line is the line as a string.
        
        if i > 0:
            # File is .csv, so split on commas.
            line_list = line.split(",")
            season = line_list[0]
            team = line_list[1]
            points = int(line_list[2])
            
            if season == current_season:
                temp_dict[team] = points
            
            else:
                return_dict[current_season] = temp_dict
                current_season = season
                temp_dict = {}
                temp_dict[team] = points
            
        
    return return_dict


def main():
    
    file = open_file("EPL stats.csv")
    
    data = create_dict(file)
    
    


if __name__ == "__main__":
    main()            