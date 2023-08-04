"""
write generator function that has as input some range value and chunk_size
produces output as lists with len == chunk size
Example:
Call:  chunk_generator(range(11), chunk_size=3) ->
Output:  [0, 1, 2]
         [3, 4, 5]
         [6, 7, 8]
         [9, 10]
"""

def chunk_generator(input_range, chunk_size):
    iterator = iter(input_range)
    while True:
        chunk = []
        try:
            for _ in range(chunk_size):
                chunk.append(next(iterator))
            yield chunk
        except StopIteration:
            if chunk:
                yield chunk
            break

for chunk in chunk_generator(range(11), chunk_size=3):
    print(chunk)