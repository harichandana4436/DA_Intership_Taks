#hackerrank:-https://www.hackerrank.com/challenges/collections-counter/problem
if __name__ == '__main__':
    n = int(input())
    my_list = []
    for _ in range(n):
        command_parts = input().split()
        action = command_parts[0]
        if action == "insert":
            index = int(command_parts[1])
            element = int(command_parts[2])
            my_list.insert(index, element)   
        elif action == "print":
            print(my_list)     
        elif action == "remove":
            element = int(command_parts[1])
            my_list.remove(element)  
        elif action == "append":
            element = int(command_parts[1])
            my_list.append(element)
        elif action == "sort":
            my_list.sort()        
        elif action == "pop":
            my_list.pop()    
        elif action == "reverse":
            my_list.reverse()
