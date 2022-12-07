# write your code here
memory = 0
while True:
    
    
    print("Enter an equation")
    a, b, c = input().split()

    #Memory consideration
    if a == "M":
        a = memory
    if c == "M":
        c = memory

        
    try:
        a = float(a)
        c = float(c)
    except ValueError:
        print("Do you even know what numbers are? Stay focused!")
        continue

    
    if b not in ["+", "-", "*", "/"]:
        print("Yes ... an interesting math operation. You've slept through all classes, haven't you?")
        continue
    
    msg_6 = " ... lazy"
    msg_7 = " ... very lazy"
    msg_8 = " ... very, very lazy"
    msg_9 = "You are"
    msg = ["a","b","c","3","d","c","g","h","b","k" "s","d","3","e","x"]
    msg[10] = "Are you sure? It is only one digit! (y / n)"
    msg[11]= "Don't be silly! It's just one number! Add to the memory? (y / n)"
    msg[12]= "Last chance! Do you really want to embarrass yourself? (y / n)"
    

    
    # fonction is_one_digit
    def is_one_digit(v):
        if v > -10 and v<10 and v==int(v):
            return "yes" 
        else:
            return "no"
    # fonction check(a,b,c)
    def check(a, b, c):
        
        msg=""
        if is_one_digit(a)=="yes" and is_one_digit(c)=="yes":
            msg = msg + msg_6
        
        if (a == 1 or c == 1) and b == "*":
            msg = msg + msg_7
        if (a == 0 or c == 0) and (b == "*" or b == "+" or b == "-"):
            msg = msg + msg_8
        if msg != "":
            msg = msg_9 + msg
        print(msg)
            
    
    #appel de la fonction check
    check(a, b, c)




    if b =="+":
        result = a+c
        print(result)
        
    if b =="-":
        result = a-c
        print(result)
        
    if b =="*":
        result = a*c
        print(result)
        
    if b =="/":
        
        try:
            result = a/c
        except ZeroDivisionError:
            print("Yeah... division by zero. Smart move...")
            continue
       
        print(result)
        
    
  
    print("Do you want to store the result? (y / n):")
    answer = input()
    if answer == "y":
        #print(is_one_digit(result))
        
        
        if is_one_digit(result) =="yes":
            
            msg_index=10
            while (msg_index<=12):
                print(msg[msg_index])
                answer = input()
                if answer == "y":
                    msg_index += 1
                    #continue
                elif answer == "n":
                    break
            else:
                memory = result
  
        elif is_one_digit(result) == "no":
            memory = result
            #print(memory)
    
    elif answer == "n":
        memory = memory
    else:
        continue
        
    print("Do you want to continue calculations? (y / n):")
    answer = input()
    if answer == "y":
        continue
    elif answer == "n":
       
        break
  
    else:
        continue

    break