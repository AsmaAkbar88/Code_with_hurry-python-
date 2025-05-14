
def function(status):
    match status:
        case 200:
            return ("ok")
        
        case 404:
            return ("Not Found")

        
        case 500:
            return ("Internal Server Error")

        
        case _:
            return ("Unknown status")
        
print(function(300))     #Output:    Unknown status
print(function(500))     #Output:    Internal Server Error
print(function(404))     #Output:    Not Found
print(function(200))     #Output:    ok

