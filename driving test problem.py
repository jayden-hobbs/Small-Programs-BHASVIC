#drving test problem
#subroutine to output pass or fail for driving test

def PassFail(MinorFaults):
    if MinorFaults < 16:
        return "pass"
    else:
        return "fail"

#main programme
print(PassFail(16))
