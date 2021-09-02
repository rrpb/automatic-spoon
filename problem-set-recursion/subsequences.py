def get_all_subsequences(input):


    def recurse_helper(input,output):
        if len(input)==0:
            result.add(output)
            return

        recurse_helper(input[1:],output+input[0])
        recurse_helper(input[1:],output)

    result = set()
    recurse_helper(input,"")
    return result

subsequences =get_all_subsequences("abc")

print(subsequences)
