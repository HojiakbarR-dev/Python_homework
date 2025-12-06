# %% [markdown]
# ### Exercise 1: Threaded Prime Number Checker

# %%
import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2,n):
        if n % i == 0:
            return False
    
    return True

def check_range(start, end, result_list, lock):
    for num in range(start, end + 1):
        if is_prime(num):
            # We use a lock so threads do not write at the same time
            with lock:
                result_list.append(num)


def threaded_prime_checker(low, high, num_threads=4):

    # Shared list for primes
    primes = []

    # Lock for safe writing
    lock = threading.Lock()

    # List to store all thread objects
    threads = []

    # Calculate the size of each chunk
    chunk_size = (high - low + 1) // num_threads

    start = low

    for i in range(num_threads):
        end = start + chunk_size - 1

        # Last thread takes remaining numbers
        if i == num_threads - 1:
            end = high

        t = threading.Thread(target=check_range, args=(start, end, primes, lock))
        t.start()
        threads.append(t)

        start = end + 1

    # Wait for all threads to finish
    for t in threads:
        t.join()

    return sorted(primes)



# Run the program

low = 1
high = 50

primes = threaded_prime_checker(low, high, num_threads=4)

print(f"Prime numbers between {low} and {high}:")
print(primes)


# %% [markdown]
# ### Exercise 2: Threaded File Processing

# %%
import threading
from collections import Counter
import re

def tokenize(line):
    """Return a list of words (lowercased) from a line.
    Uses a simple regex to extract word characters (letters, digits, underscore)."""
    return re.findall(r"\b\w+\b", line.lower())

def worker(lines_slice, local_counter):
    """Count words in the given list of lines and update local_counter (a Counter)."""
    for line in lines_slice:
        words = tokenize(line)
        local_counter.update(words)

def threaded_word_count(filename, num_threads=4):
    """
    Count words in filename using num_threads threads.
    Returns a collections.Counter with word -> count.
    """
    # 1) Read all lines (simple and easy to reason about)
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    if not lines:
        return Counter()

    # 2) Split lines into nearly-equal chunks for each thread
    n = len(lines)
    chunk_size = (n + num_threads - 1) // num_threads  # ceiling division

    # Shared objects
    counters = []      # list to hold each thread's local Counter
    threads = []

    for i in range(num_threads):
        start = i * chunk_size
        end = min(start + chunk_size, n)
        if start >= end:
            # no more lines to give this thread
            break

        local_counter = Counter()
        counters.append(local_counter)

        t = threading.Thread(target=worker, args=(lines[start:end], local_counter))
        t.start()
        threads.append(t)

    # 3) Wait for all threads to finish
    for t in threads:
        t.join()

    # 4) Merge counters into one
    total = Counter()
    for c in counters:
        total.update(c)

    return total


if __name__ == "__main__":
    filename = "large_text.txt"   # change to your file
    num_threads = 4

    counts = threaded_word_count(filename, num_threads)

    # Print summary: top 20 most common words
    print("Top 20 most common words:")
    for word, cnt in counts.most_common(20):
        print(f"{word:15} {cnt}")



