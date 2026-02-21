import random as rnd
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

class SimpleBayesClassifier:

    def __init__(self, n_pos, n_neg):
        
        """
        Initializes the SimpleBayesClassifier with prior probabilities.

        Parameters:
        n_pos (int): The number of positive samples.
        n_neg (int): The number of negative samples.
        
        Returns:
        None: This method does not return anything as it is a constructor.
        """

        self.n_pos = n_pos
        self.n_neg = n_neg
        self.prior_pos = n_pos / (n_pos + n_neg)
        self.prior_neg = n_neg / (n_pos + n_neg)

    def fit_params(self, x, y, n_bins=10):

        """
        Computes histogram-based parameters for each feature in the dataset.

        Parameters:
        x (np.ndarray): The feature matrix, where rows are samples and columns are features.
        y (np.ndarray): The target array, where each element corresponds to the label of a sample.
        n_bins (int): Number of bins to use for histogram calculation.

        Returns:
        (stay_params, leave_params): A tuple containing two lists of tuples, 
        one for 'stay' parameters and one for 'leave' parameters.
        Each tuple in the list contains the bins and edges of the histogram for a feature.
        """

        self.stay_params = []
        self.leave_params = []

        # INSERT CODE HERE
        for feature_idx in range(x.shape[1]):   
            _, edges  = np.histogram(x[:, feature_idx], bins=n_bins)
            
            stay_counts  = np.histogram(x[y == 0.0, feature_idx], bins=edges)[0]
            leave_counts = np.histogram(x[y == 1.0, feature_idx], bins=edges)[0]
            
            alpha = 1
            stay_probs  = (stay_counts  + alpha) / (np.sum(stay_counts) + alpha * len(stay_counts))
            leave_probs = (leave_counts + alpha) / (np.sum(leave_counts) + alpha * len(leave_counts))
            
            self.stay_params .append((stay_probs, edges))
            self.leave_params.append((leave_probs, edges))
        
        return self.stay_params, self.leave_params

    def predict(self, x, thresh = 0.0):

        """
        Predicts the class labels for the given samples using the non-parametric model.

        Parameters:
        x (np.ndarray): The feature matrix for which predictions are to be made.
        thresh (float): The threshold for log probability to decide between classes.

        Returns:
        result (list): A list of predicted class labels (0 or 1) for each sample in the feature matrix.
        """

        y_pred = []

        # INSERT CODE HERE
        for sample in x:
            log_stay_prior  = np.log(self.prior_neg)
            log_leave_prior = np.log(self.prior_pos)
            
            log_stay_prob  = log_stay_prior
            log_leave_prob = log_leave_prior
            
            for feature_idx in range(x.shape[1]):
                stay_prob, edges = self.stay_params[feature_idx]
                leave_prob, _    = self.leave_params[feature_idx]
                
                bin = np.digitize(sample[feature_idx], edges, right=False) - 1
                bin = np.clip(bin, 0, len(stay_prob) - 1)
                
                log_stay_prob  += np.log(stay_prob[bin])
                log_leave_prob += np.log(leave_prob[bin])
            
            if (log_leave_prob - log_stay_prob > thresh):
                y_pred.append(1)
            else:
                y_pred.append(0)

        return y_pred
    
    def fit_gaussian_params(self, x, y):

        """
        Computes mean and standard deviation for each feature in the dataset.

        Parameters:
        x (np.ndarray): The feature matrix, where rows are samples and columns are features.
        y (np.ndarray): The target array, where each element corresponds to the label of a sample.

        Returns:
        (gaussian_stay_params, gaussian_leave_params): A tuple containing two lists of tuples,
        one for 'stay' parameters and one for 'leave' parameters.
        Each tuple in the list contains the mean and standard deviation for a feature.
        """

        self.gaussian_stay_params = []
        self.gaussian_leave_params = []

        # INSERT CODE HERE
        for feature_idx in range(x.shape[1]):   
            stay_mean = np.mean(x[y == 0.0, feature_idx])
            stay_std  = np.std(x[y == 0.0, feature_idx])
            print(x[y == 0.0, feature_idx], stay_mean, stay_std)
            
            leave_mean = np.mean(x[y == 1.0, feature_idx])
            leave_std  = np.std(x[y == 1.0, feature_idx])
            
            self.gaussian_stay_params.append((stay_mean, stay_std))
            self.gaussian_leave_params.append((leave_mean, leave_std))
            
        return self.gaussian_stay_params, self.gaussian_leave_params
    
    def gaussian_predict(self, x, thresh = 0):

        """
        Predicts the class labels for the given samples using the parametric model.

        Parameters:
        x (np.ndarray): The feature matrix for which predictions are to be made.
        thresh (float): The threshold for log probability to decide between classes.

        Returns:
        result (list): A list of predicted class labels (0 or 1) for each sample in the feature matrix.
        """

        y_pred = []

        # INSERT CODE HERE
        for sample in x:
            log_stay_prior  = np.log(self.prior_neg)
            log_leave_prior = np.log(self.prior_pos)
            
            log_stay_prob  = log_stay_prior
            log_leave_prob = log_leave_prior
            
            for feature_idx in range(x.shape[1]):
                stay_mean,  stay_std  = self.gaussian_stay_params[feature_idx]
                leave_mean, leave_std = self.gaussian_leave_params[feature_idx]
                
                stay_std = max(stay_std, 1e-9)
                leave_std = max(leave_std, 1e-9)
                
                stay_dist  = stats.Normal(mu=stay_mean,  sigma=stay_std)
                leave_dist = stats.Normal(mu=leave_mean, sigma=leave_std)
                
                log_stay_prob  += stay_dist.logpdf(sample[feature_idx])
                log_leave_prob += leave_dist.logpdf(sample[feature_idx])
                
            if (log_leave_prob - log_stay_prob > thresh):
                y_pred.append(1)
            else:
                y_pred.append(0)

        return y_pred
