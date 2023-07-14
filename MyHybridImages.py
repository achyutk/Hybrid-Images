import math
import numpy as np

from MyConvolution import convolve

# Function for creating a hybrid image
def myHybridImages (lowImage, lowSigma, highImage, highSigma):

    low_kernel = makeGaussianKernel(lowSigma)   #Making gausian kernel for first image
    high_kernel = makeGaussianKernel(highSigma) #Making gausian kernel for second image
    filtered_low_image = convolve(lowImage,low_kernel)  #Convolving first image ----> This is a low pass image
    filtered_low_image2 =convolve(highImage,high_kernel) #Convolving second image image  ----> This is a low pass image
    filtered_high_image2 = highImage - filtered_low_image2  #Converting low pass image to high pass image
    hybridimage = filtered_low_image + filtered_high_image2  #Combining image

    return  hybridimage


def makeGaussianKernel(sigma):

    #finding kernel size
    kernelsize = math.floor(8 * sigma + 1)
    kernelsize = math.floor(8 * sigma + 1) + 1 if kernelsize % 2 == 0 else kernelsize

    kernel = np.zeros((kernelsize, kernelsize))  # Creating empty kernel
    centre = math.floor(kernelsize / 2) + 1     # Finding center of the kernel
    sum = 0

    # Giving weights to each element of kernel using gausian function
    for i in range(kernelsize):
        for j in range(kernelsize):
            x = (i - centre)
            y = (j - centre)
            kernel[i, j] = (1 / (math.pi * math.sqrt(2))) * math.exp(-1 * ((x ** 2) + (y ** 2)) / (2 * (sigma ** 2)))
            sum = sum + kernel[i, j]

    kernel = kernel / sum

    return kernel