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
    temp_dict = {}
    # Data file starts at the 18-19 season.
    current_season = "18-19"
    
    # Goes through each line in the file.
    for i, line in enumerate(file_ptr):
        # i is the index, line is the line as a string.
        
        # Skips the headers.
        if i > 0:
            # File is .csv, so split on commas.
            line_list = line.split(",")
            season = line_list[0]
            team = line_list[1]
            # Cast points to int to be easier to evaluate.
            points = int(line_list[2])
            
            # Keep track of data only for the current season.
            if season == current_season:
                temp_dict[team] = points
            
            # If we get to the next season, put the last season's  data in the
            # return dictionary and start collecting data for this season.
            else:
                return_dict[current_season] = temp_dict
                current_season = season
                temp_dict = {}
                temp_dict[team] = points
            
        
    return return_dict


def main():
    ''' Controls the flow of the program. '''
    
    file = open_file("EPL stats.csv")
    
    data = create_dict(file)
    
    


if __name__ == "__main__":
    main()            