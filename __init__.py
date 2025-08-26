import time

GREEN   = "\033[32m"
CYAN    = "\033[36m"
YELLOW  = "\033[33m"
RED     = "\033[31m"
MAGENTA = "\033[35m"
BRIGHT  = "\033[1m"
WHITE   = "\033[37m"
RESET   = "\033[0m"

def timestamp() -> str:
    return time.strftime("%I:%M:%S %p")

class Debug:
    @staticmethod
    def info(text: str) -> None:
        print(GREEN + f"[{timestamp()} INFO]" + RESET + " " + WHITE + text + RESET)

    @staticmethod
    def debug(text: str) -> None:
        print(CYAN + f"[{timestamp()} DEBUG]" + RESET + " " + WHITE + text + RESET)

    @staticmethod
    def warn(text: str) -> None:
        print(YELLOW + f"[{timestamp()} WARNING]" + RESET + " " + WHITE + text + RESET)

    @staticmethod
    def err(text: str) -> None:
        print(RED + f"[{timestamp()} ERROR]" + RESET + " " + WHITE + text + RESET)

    @staticmethod
    def succ(text: str) -> None:
        print(MAGENTA + BRIGHT + f"[{timestamp()} SUCCESS]" + RESET + " " + WHITE + text + RESET)