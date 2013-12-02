import numpy as np

a = np.array([[569, 106],
              [768, 356],
              [531, 105],
              [800, 139]])

a = np.array([[ 447.5, 502.5],
 [ 299.5, 502.5],
 [ 150.5, 502.5],
 [ 500.5, 502. ],
 [ 398.5, 502. ],
 [ 350. , 502. ],
 [ 250. , 502. ],
 [ 201.5, 502. ],
 [ 102. , 500.5],
 [  55.5, 501. ],
 [ 500. , 451.5],
 [ 447. , 451.5],
 [ 397.5, 451.5],
 [ 348.5, 451.5],
 [ 299. , 452.5],
 [ 249. , 451.5],
 [ 200.5, 451.5],
 [ 151. , 450.5],
 [ 102. , 450. ],
 [  55. , 448.5],
 [ 499.5, 404. ],
 [ 446.5, 403.5],
 [ 397. , 404.5],
 [ 348. , 403. ],
 [ 297.5, 403. ],
 [ 248. , 402.5],
 [ 199.5, 402. ],
 [ 150.5, 401.5],
 [ 103. , 401. ],
 [  55.5, 401. ],
 [ 499.5, 356. ],
 [ 446. , 356. ],
 [ 396. , 356. ],
 [ 347. , 355. ],
 [ 297.5, 354.5],
 [ 248. , 354. ],
 [ 200. , 354. ],
 [ 150.5, 353.5],
 [ 102. , 352.5],
 [  56. , 352.5],
 [ 499. , 305.5],
 [ 446. , 305.5],
 [ 396.5, 305.5],
 [ 347. , 305. ],
 [ 297. , 305. ],
 [ 248. , 304.5],
 [ 199.5, 304.5],
 [ 150. , 303.5],
 [ 102. , 303. ],
 [  55.5, 302. ],
 [ 499. , 256.5],
 [ 445.5, 256. ],
 [ 396. , 255.5],
 [ 347. , 255.5],
 [ 297. , 255. ],
 [ 247.5, 255. ],
 [ 199.5, 254.5],
 [ 150. , 254. ],
 [ 102. , 254. ],
 [  55. , 253. ],
 [ 499.5, 207. ],
 [ 446. , 208. ],
 [ 396.5, 207. ],
 [ 347. , 206.5],
 [ 297.5, 206.5],
 [ 248. , 206. ],
 [ 200. , 206. ],
 [ 150.5, 205.5],
 [ 103.5, 205. ],
 [  56. , 204.5],
 [ 500. , 156.5],
 [ 447. , 156. ],
 [ 397. , 156. ],
 [ 348. , 156. ],
 [ 297.5, 155.5],
 [ 248.5, 155. ],
 [ 200. , 155. ],
 [ 151. , 155. ],
 [  56. , 155.5],
 [ 102.5, 154.5],
 [ 501. , 106.5],
 [ 447.5, 106. ],
 [ 397.5, 106.5],
 [ 348. , 105.5],
 [ 298. , 105.5],
 [  56.5, 105.5],
 [ 249. , 105. ],
 [ 200. , 105. ],
 [ 150.5, 105. ],
 [ 103. , 105. ],
 [ 501.5,  56.5],
 [ 448.5,  56.5],
 [ 397.5,  56. ],
 [ 348.5,  56. ],
 [ 298.5,  55.5],
 [  56.5,  55.5],
 [ 249. ,  55. ],
 [ 200. ,  55.5],
 [ 151. ,  55. ],
 [ 103.  , 55. ]])

w, h = a.shape
sqrt_w = int(np.sqrt(w))

# sort by y
a = a[np.argsort(a[:, 1])]

# put in groups
a = np.reshape(a, (sqrt_w, sqrt_w, 2))

# sort rows by x
a = np.vstack([row[np.argsort(row[:, 0])] for row in a])

# regroup
a = np.reshape(a, (w, 1, 2))

print a