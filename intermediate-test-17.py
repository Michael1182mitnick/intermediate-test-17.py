# Write a function that partitions a string such that every substring is a palindrome and returns all possible palindrome partitions.

def is_palindrome(s):
    # Check if the string is a palindrome by comparing it with its reverse
    return s == s[::-1]


def partition_palindromes(s):
    def backtrack(start, path):
        # If we reach the end of the string, add the current partition to the result
        if start == len(s):
            result.append(path[:])
            return

        # Try to partition the string from 'start' to 'end'
        for end in range(start + 1, len(s) + 1):
            substring = s[start:end]
            if is_palindrome(substring):  # Check if the current substring is a palindrome
                # Add the palindrome substring to the path
                path.append(substring)
                backtrack(end, path)      # Recurse for the next substring
                path.pop()                # Backtrack and remove the last palindrome substring from the path

    result = []
    backtrack(0, [])
    return result


# Example usage
s = "aab"
partitions = partition_palindromes(s)
print(f"All possible palindrome partitions of '{s}':")
for partition in partitions:
    print(partition)
