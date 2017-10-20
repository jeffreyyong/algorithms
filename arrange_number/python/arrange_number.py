def create_largest_number(num_array):
    sorted_num = sorted(num_array, key=str, reverse=True)
    # [980, 90, 9, 6, 10] 

    data = {}
    for num in sorted_num:
        key = str(num)[:1]
        if data[key] == nil {
            data[key] = [num]
        } else {


        }

        






def main():
    num_array = [9, 980, 10, 6, 90]
    print(num_array)
    largest_num = create_largest_number(num_array)
    print(largest_num)

if __name__ == "__main__": main()

