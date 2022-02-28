#From python 3.10 we have match statements. we can us these insted od if/elif/else blocks. for example, in the following code, we are taking an integer as input and then matching the value with some predifined HTTP status codes and print the names.

status = int(input("Give us a status code: "))
match status:
    case 200:
        print("OK")
             case 201:
             print("Created")
             case 301:
             print("Moved Permanantly")
             case 302:
             print("Found")
             case_:
             print("The status is unknown to us.")
             
