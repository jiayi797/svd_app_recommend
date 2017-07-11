#encoding=utf-8
from time import time
from scipy.sparse import csr_matrix
from sklearn.decomposition import TruncatedSVD

app2user = []
count = 0

t0 = time()
app_list = []

upper_frequency = 10000
bottom_frequency = 20

print("loading file ...")
with open("user_installedapps.txt") as f:
    for line in f:
        app_user = line.strip().split(":")
        users = app_user[1].split(" ")
        if len(users) > upper_frequency or len(users) < bottom_frequency:
            continue

        app_list.append(app_user[0])
        app2user.append(app_user[1].split(" "))
        count += 1

print("load file used %.3f s."%(time() - t0))
print("apps %d"%(count))

t0 = time()
print("get matrix ...")

indptr = [0]
indices = [ ]
data = [ ]
vocabulary = { }
for d in app2user:
    for term in d:
        index = vocabulary.setdefault(term, len(vocabulary))
        indices.append(index)
        data.append(1)
    indptr.append(len(indices))

mtx = csr_matrix((data, indices, indptr), dtype=float)
print("get matrix used %.3f s."%(time() - t0))
print("mtx.shape=", mtx.shape)

t0 = time()
print("reduce features ...")
reducedfeatures = 500
svd = TruncatedSVD(reducedfeatures, algorithm='arpack')
features = svd.fit_transform(mtx)
print("reduce features used %.3f s."%(time() - t0)) 
print(svd.explained_variance_ratio_.sum())

t0 = time()
print("writing features ...")
f = open("reduce_feature.txt", "w")
for i in range(len(app_list)):
    app = app_list[i]
    vec = [str(item) for item in features[i]]
    f.write(app + ":" + " ".join(vec) + "\n")
f.close()
print("writing features in %.3f s."%(time() - t0))

