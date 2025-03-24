from collections import defaultdict

def caching_fibonacci() -> None:
    cached = defaultdict(int)
    def fibonacci(n: int) -> int:
        if n <= 0:
            return 0
        
        if n <= 1:
            return 1
        
        if n in cached:
            return cached[n]
        
        cached[n] = fibonacci(n - 1) + fibonacci(n - 2)
        return cached[n]
    
    return fibonacci

if __name__ == "__main__":
    calculate_fib = caching_fibonacci()

    assert calculate_fib(10) == 55
    assert calculate_fib(15) == 610