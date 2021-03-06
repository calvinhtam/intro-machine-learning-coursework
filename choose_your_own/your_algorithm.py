#!/usr/bin/python
#import matplotlib
#matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]
#print('hj')
#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
plt.savefig('dataplot')
#plt.show()
################################################################################


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

#"""
#knn
#accuracy = .94
from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=int(len(features_train[0]) * .5))
#"""

"""
#adaboost
#accuracy = .924
from sklearn.ensemble import AdaBoostClassifier
clf = AdaBoostClassifier()
"""

"""
#randomTree
#accuracy = .912, .924, .92, .912, .912, .908
from sklearn.ensemble import RandomForestClassifier
#clf = RandomForestClassifier(n_estimators=10, criterion='gini', max_depth=None,min_samples_split=2, min_samples_leaf=1, min_weight_fraction_leaf=0.0, max_features='auto', max_leaf_nodes=None,bootstrap=True, oob_score=False, n_jobs=1, random_state=None, verbose=0, warm_start=False,class_weight=None)
clf = RandomForestClassifier()
"""

clf.fit(features_train, labels_train)
accuracy = clf.score(features_test, labels_test)
print(accuracy)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass
