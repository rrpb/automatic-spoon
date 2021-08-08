"""Given a string s and an integer array indices of the same length.

The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string."""


def get_shuffle_string(input_str,indices):
    shuffled_string=["" for s in input_str]
    for index in range(len(input_str)):
        shuffled_string[indices[index]]=input_str[index]
    return "".join(shuffled_string)

s = "codeleet"
indices = [4,5,6,7,0,2,1,3]
print(get_shuffle_string(s,indices))