# match_case is similar to a switch statement in other languages (like C or JavaScript).

def http_status(status):
    match status:
        case 200:
            return "ok"
        case 404:
            return "not found"
        case 500:
            return "internal server error"
        case _:
            return "unknown status"
print(http_status(200))
print(http_status(404))
print(http_status(500))
print(http_status(600))


# another example
status = "success"
match status:
    case "success" | "done":
        print("Operation completed.")
    case "pending" | "in-progress":
        print("Still running...")
    case _:
        print("Unknown status.")

