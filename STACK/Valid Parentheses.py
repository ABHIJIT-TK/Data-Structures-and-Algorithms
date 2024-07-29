def isValid(self, s: str) -> bool:
    # st=[]
    st=[]
    mp={')':'(','}':'{',']':'['}
    for i in s:
        if i in mp.values():
            st.append(i)
        elif i in mp.keys():
            if not st or mp[i]!=st.pop():
                return False
    return not st

print(isValid(input()))
