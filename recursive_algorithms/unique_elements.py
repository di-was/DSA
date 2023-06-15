def unique3(S, start, stop):
    if stop - start <= 1: return True
    elif not unique3(S, start, stop-1): return False 
    elif not unique3(S, start+1, stop): return False 
    else: return S[start] != S[stop-1]

