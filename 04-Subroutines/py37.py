def fibonaci(n):
    fin_seq=[0,1]
    for i in range(2,n):
        fin_seq.append(fin_seq[i-1] + fin_seq[i-2])
    return f"suma tego ciągu to {sum(fin_seq)}"



if __name__=="__main__":
    a=fibonaci(7)
    print(a)