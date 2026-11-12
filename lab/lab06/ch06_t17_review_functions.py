def shutdown(s: str) -> str:
    if s == "yes":
        return "Shutting down"
    elif s == "no":
        return "shutdown aborted"
    else:
        return "Sorry"
