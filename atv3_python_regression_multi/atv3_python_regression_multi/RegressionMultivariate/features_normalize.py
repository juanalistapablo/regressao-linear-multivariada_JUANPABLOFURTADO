"""
@file features_normalizes.py
@brief Funções para normalização de features em datasets.
@details Este módulo contém funções para normalizar as features de um dataset
         utilizando diferentes abordagens, como média e desvio padrão, ou
         mínimo e máximo.
@author Your Name <your.email@example.com>
"""

import numpy as np


def features_normalize_by_std(X):
    """
    Normaliza as features de um dataset para média zero e desvio padrão unitário.
    Matematicamente, a formula utilizada é:
        X_norm = (X - mu) / sigma
    onde:
        - X é a matriz de entrada (m x n) onde m é o número de amostras e n é o número de features.
        - mu é o vetor de médias (1 x n) de cada feature.
        - sigma é o vetor de desvios padrão (1 x n) de cada feature.

    :param (ndarray) X: Matriz de entrada onde cada linha é uma amostra e cada coluna é uma feature.
    :return (tuple): Uma tripla contendo:
        - X_norm (ndarray): Matriz normalizada.
        - mu (ndarray): Vetor com as médias de cada feature.
        - sigma (ndarray): Vetor com os desvios padrão de cada feature.
    """
    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    sigma[sigma == 0] = 1  # evita divisão por zero
    X_norm = (X - mu) / sigma
    return X_norm, mu, sigma


def features_normalizes_by_min_max(X):
    """
    Normaliza as features de um dataset para o intervalo [0, 1] utilizando o mínimo e o máximo.
    Matematicamente, a formula utilizada é:
        X_norm = (X - min) / (max - min)
    onde:
        - X é a matriz de entrada (m x n) onde m é o número de amostras e n é o número de features.
        - min é o vetor de mínimos (1 x n) de cada feature.
        - max é o vetor de máximos (1 x n) de cada feature.

    :param (ndarray) X: Matriz de entrada onde cada linha é uma amostra e cada coluna é uma feature.
    :return (tuple): Uma tupla contendo:
        - X_norm (ndarray): Matriz normalizada.
        - min (ndarray): Vetor com os valores mínimos de cada feature.
        - max (ndarray): Vetor com os valores máximos de cada feature.
    """
    min_val = np.min(X, axis=0)
    max_val = np.max(X, axis=0)
    range_val = max_val - min_val
    range_val[range_val == 0] = 1  # evita divisão por zero
    X_norm = (X - min_val) / range_val
    return X_norm, min_val, max_val
