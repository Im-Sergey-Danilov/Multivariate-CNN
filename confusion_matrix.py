# from CNN import result
# from sklearn.metrics import classification_report, confusion_matrix
#
# index = 1
# for each_prediction in result:
#     print(each_prediction, index)
#     index += 1

import itertools
import numpy as np
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix

import get_yTrue_yPred

y_pred, y_true = get_yTrue_yPred.get_yTrue_yPred()


def plot_confusion_matrix(y_true, y_pred, title = "Confusion matrix",
                          cmap = plt.cm.Blues, save_flg = False):
    classes = [str(i) for i in range(0, 23)]
    print(classes)
    labels = []
    labels.append(0)
    for i in range(0, 22):
        labels.append(1+10*i)
    print(labels)
    print("HEREHERE")

    cm = confusion_matrix(y_true, y_pred, labels=labels)
    plt.figure(figsize=(14, 12))
    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title, fontsize=40)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, labels, fontsize=10)
    plt.yticks(tick_marks, labels, fontsize=10)
    print(cm)
    print('Confusion matrix, without normalization')

    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, cm[i, j],
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label', fontsize=30)
    plt.xlabel('Predicted label', fontsize=30)

    if save_flg:
        plt.savefig("./confusion_matrix.png")

    plt.show()


y_true = [int(x) for x in y_true]
y_pred = [int(x) for x in y_pred]


plot_confusion_matrix(y_true=y_true, y_pred=y_pred)
