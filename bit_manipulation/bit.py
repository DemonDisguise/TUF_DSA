# Utility tools for bit manipulation

def bit(num: int, width: int = 8) -> str:
    mask = (1 << width) - 1
    return format(num & mask, f"0{width}b")
