
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()
    string_list = user_input.split(",")
    num_list = [float(num) for num in string_list]
    return num_list


def calc_average(num_list):
    ave=sum(num_list)/len(num_list)
    return ave
    

def find_min_max(num_list):
    min1 = min(num_list)
    max1 = max(num_list)
    return [min1, max1]



def sort_temperature(num_list):
    sorted_list = sorted(num_list)
    return sorted_list

def calc_median_temperature(num_list):
    sorted_list = sorted(num_list)
    n = len(sorted_list)
    middle = n // 2

    if n % 2 == 1:
        return sorted_list[middle]
    else:
        return (sorted_list[middle - 1] + sorted_list[middle]) / 2


def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(num_list)
    print("average is "+ str(calc_average(num_list)))
    min_max = find_min_max(num_list)
    print("min is " + str(min_max[0]))
    print("max is " + str(min_max[1]))
    print(sort_temperature(num_list))
    print(calc_median_temperature(num_list))


if __name__ == "__main__":
    main()
