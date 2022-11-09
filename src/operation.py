import numpy as np
import cv2

# matriks[0] kolom

def JumlahMatriks (matriksGambar1, matriksGambar2):
    for i in range(len(matriksGambar1)):
        for j in range(len(matriksGambar1[0])):
            matriksGambar1[i][j] += matriksGambar2[i][j]
    return matriksGambar1

def KurangMatriks (matriksGambar1, matriksGambar2):
    for i in range(len(matriksGambar1)):
        for j in range(len(matriksGambar1[0])):
            matriksGambar1[i][j] -= matriksGambar2[i][j]
    return matriksGambar1

def KaliMatriks (matriksGambar1, matriksGambar2):
    matrikshasil = np.dot(matriksGambar1, matriksGambar2)
    return matrikshasil

def TransposeMatriks (matriksGambar):
    matrikshasil = np.transpose(matriksGambar)
    return matrikshasil
