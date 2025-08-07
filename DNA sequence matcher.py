def longest_common_substring(s1, s2):
    m = len(s1)
    n = len(s2)
    max_len = 0
    ending_index_s1 = 0

    # Create a 2D array to store lengths of longest common suffixes of substrings
    length_table = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                length_table[i][j] = length_table[i - 1][j - 1] + 1
                if length_table[i][j] > max_len:
                    max_len = length_table[i][j]
                    ending_index_s1 = i
            else:
                length_table[i][j] = 0

    # Extract longest common substring
    longest_substring = s1[ending_index_s1 - max_len: ending_index_s1]
    return longest_substring, max_len

# Example usage
if __name__ == "__main__":
    dna_seq1 = input("Enter first DNA sequence: ").upper()
    dna_seq2 = input("Enter second DNA sequence: ").upper()

    match, length = longest_common_substring(dna_seq1, dna_seq2)
    if length > 0:
        print(f"Longest matching DNA sequence: {match} (length {length})")
    else:
        print("No matching sequence found.")

