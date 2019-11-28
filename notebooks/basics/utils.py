import numpy as np
from sklearn import datasets
import matplotlib
import pickle
import scipy.signal
import matplotlib.pylab as plt
from scipy.interpolate import interp1d
import json


def reduce_dataset(data, labels, reduce_by=-1, num_obs=-1):
    if reduce_by == -1 and num_obs==-1:
        return data, labels
    elif reduce_by != -1:
        classes = np.unique(labels)
        data_ = []
        labels_ = []
        for ci, c in enumerate(classes):
            idx = np.where(labels == c)[0]
            if ci == 0:
                data_ = np.array(data[idx[:int(((100 - reduce_by) / 100.0) * len(idx))],...])
                labels_ = np.array(labels[idx[:int(((100 - reduce_by) / 100.0) * len(idx))],...])
            else:
                data_ = np.r_[data_, data[idx[:int(((100 - reduce_by) / 100.0) * len(idx))],...]]
                labels_ = np.r_[labels_, labels[idx[:int(((100 - reduce_by) / 100.0) * len(idx))],...]]
        # data_ = np.array(data_)
        # labels_ = np.array(labels_)
        return data_, labels_
    elif reduce_by ==-1 and num_obs != -1:
        classes = np.unique(labels)
        data_ = []
        labels_ = []
        for ci, c in enumerate(classes):
            idx = np.where(labels == c)[0]
            if ci == 0:
                data_ = np.array(data[idx[:num_obs],...])
                labels_ = np.array(labels[idx[:num_obs],...])
            else:
                data_ = np.r_[data_, data[idx[:num_obs],...]]
                labels_ = np.r_[labels_, labels[idx[:num_obs],...]]
        return data_, labels_




def get_iris_data(classes=[0, 1, 2]):
    iris = datasets.load_iris()
    features = np.array(iris.data)
    labels = np.array(iris.target)
    idx = []
    for c in classes:
        if len(idx) == 0:
            idx = np.where((labels == c))[0]
        else:
            idx = np.r_[idx, np.where((labels == c))[0]]
    cmap = matplotlib.cm.get_cmap('Set1')
    colors = cmap(labels)
    return features[idx, :], labels[idx], colors[idx]


def load_one_dollar_ds(gesture=None, path='Lecture4lib/onedol_ds.pkl', resample=False):
    d = pickle.load(open(path, 'rb'))
    data, labels = d['dataset'], d['labels']
    if gesture == None:
        if not resample:
            return data, labels
        else:
            data_ = []
            for g in data:
                n_length = 50
                f_x = interp1d(np.arange(0, len(g)), g[:, 0])
                f_y = interp1d(np.arange(0, len(g)), g[:, 1])
                nx = np.linspace(0, len(g) - 1, num=n_length, endpoint=True)
                g_ = np.zeros((n_length, 2))
                g_[:, 0] = f_x(nx)
                g_[:, 1] = f_y(nx)
                data_.append(g_)
            data_ = np.array(data_)
            labels = np.array(labels)
            return data_, labels

    else:
        idx = []
        if isinstance(gesture, list):
            gesture_list = gesture
        else:
            gesture_list = [gesture]
        for c in gesture_list:
            if len(idx) == 0:
                idx = [i for i, l in enumerate(labels) if l == c]
            else:
                idx_ = [i for i, l in enumerate(labels) if l == c]
                idx = np.r_[idx, idx_]
        data_ = []
        labels_ = []    
        if resample:
            for i in idx:
                g = data[i]
                n_length = 50
                f_x = interp1d(np.arange(0, len(g)), g[:, 0])
                f_y = interp1d(np.arange(0, len(g)), g[:, 1])
                nx = np.linspace(0, len(g) - 1, num=n_length, endpoint=True)
                g_ = np.zeros((n_length, 2))
                g_[:, 0] = f_x(nx)
                g_[:, 1] = f_y(nx)
                data_.append(g_)
                labels_.append(labels[i])
            data_ = np.array(data_)
        else:
            for i in idx:
                data_.append(data[i])
                labels_.append(labels[i])
        return data_, labels_

def load_3d_gesture_data(resample=True):
    data = json.load(open('alphabet_variability_raw_data.json'))
    dataset_ = []
    labels_ = []
    for ci, c in enumerate(sorted(data.keys())):
        plt.subplot(1, len(data.keys()), ci + 1)
        for g in sorted(data[c].keys()):
            dat = []
            for d in data[c][g]:
                v = []
                for k in d['data'].keys():
                    v.append(d['data'][k])
                dat.append(v)
            dat = np.array(dat)
            if (len(dat) > 10):
                dataset_.append(dat)
                labels_.append(ci + 1)
    if resample == True:
        data_ = []
        for g in dataset_:
            n_length = 50
            f = []
            for k in range(g.shape[1]):
                f.append(interp1d(np.arange(0, len(g)), g[:, k]))
                # f_x = interp1d(np.arange(0, len(g)), g[:, 0])
                # f_y = interp1d(np.arange(0, len(g)), g[:, 1])
            nx = np.linspace(0, len(g) - 1, num=n_length, endpoint=True)
            g_ = np.zeros((n_length, g.shape[1]))
            for k in range(g.shape[1]):
                g_[:, k] = f[k](nx)
                # g_[:, 1] = f_y(nx)
            data_.append(g_)
        data_ = np.array(data_)
        labels = np.array(labels_)
        return data_, labels
    else:
        return dataset_, labels_


def mean_gesture(gesture, path='Lecture4lib/onedol_ds.pkl'):
    d, l = load_one_dollar_ds(gesture=gesture, path=path)
    data = []
    for g in d:
        f_x = interp1d(np.arange(0, len(g)), g[:, 0])
        f_y = interp1d(np.arange(0, len(g)), g[:, 1])
        nx = np.linspace(0, len(g) - 1, num=50, endpoint=True)
        g_ = np.zeros((50, 2))
        g_[:, 0] = f_x(nx)
        g_[:, 1] = f_y(nx)
        data.append(g_)
    data = np.array(data)
    return np.mean(data, axis=0)


def std_gesture(gesture, path='Lecture4lib/onedol_ds.pkl'):
    d, l = load_one_dollar_ds(gesture=gesture, path=path)
    data = []
    for g in d:
        f_x = interp1d(np.arange(0, len(g)), g[:, 0])
        f_y = interp1d(np.arange(0, len(g)), g[:, 1])
        nx = np.linspace(0, len(g) - 1, num=50, endpoint=True)
        g_ = np.zeros((50, 2))
        g_[:, 0] = f_x(nx)
        g_[:, 1] = f_y(nx)
        data.append(g_)
    data = np.array(data)
    return np.std(data, axis=0)


if __name__ == '__main__':
    # mean_gesture(1, path='onedol_ds.pkl')
    # ds, lbls = load_3d_gesture_data(resample=True)

    import ssl
    ssl._create_default_https_context = ssl._create_unverified_context
    from sklearn import datasets
    dataset = datasets.fetch_covtype()
    features = dataset.data
    labels = dataset.target
    print(features.shape)
    [features, labels] = reduce_dataset(features, labels, reduce_by=90)
    print(features.shape)


