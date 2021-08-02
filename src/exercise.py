def main():
    #write your code below this line
    longest_name = ''
    longest_name_len = 0
    sum_of_years = 0
    year_count = 0

    while True:
        line = input()

        if line == '':
            break

        data = line.split(",")
        name = data[0]
        name_len = len(name)
        year = int(data[1])
        
        year_count += 1
        sum_of_years += year

        if name_len > longest_name_len:
            longest_name = name
            longest_name_len = name_len

    average = sum_of_years / year_count

    print("Longest name: " + longest_name)
    print("Average of the birth years: " + str(average))

if __name__ == '__main__':
    main()
