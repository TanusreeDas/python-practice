from nltk.stem import LancasterStemmer
ps = LancasterStemmer()
words = ["programs", "programmer"]
for w in words:
    print(ps.stem(w),end=" ")