def repl(st, **kwargs):
    for i in kwargs:
        if i in st:
            st = st.replace(i, kwargs[i])
    print(st)

repl('replace my val abc', my='s1', abc='fff')