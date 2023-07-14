import numpy as np


def convolve(image, kernel):
    base = np.zeros(image.shape, dtype=float)
    iheight = image.shape[0]
    iwidth = image.shape[1]
    ichannel = 1  # default channels
    kheight = kernel.shape[0]
    kwidth = kernel.shape[1]
    kchannel = 1  # default channels
    # kernel = np.reshape(kernel,(kernel.shape[0],kernel.shape[1],1))



    # Flipping the received kernel
    flipped_kernel = np.zeros(kernel.shape, dtype=float)
    for i in range(kernel.shape[0]):
        for j in range(kernel.shape[1]):
            flipped_kernel[kernel.shape[0] - i - 1, kernel.shape[1] - j - 1] = kernel[i, j]
    kernel = flipped_kernel



    # identfying number of channels for a 3d Image
    try:
        ichannel = image.shape[2]
    except:
        image = np.reshape(image,(image.shape[0], image.shape[1], ichannel))  # Reshaping image shape from (x,y) --> (x,y,1)

    stride = 1  # default stride
    padd_h = int((iheight * (stride - 1) + kheight - 1) / 2)  # Calculating padding height
    padd_w = int((iwidth * (stride - 1) + kwidth - 1) / 2)  # Calculating padding width
    conv = np.zeros((iheight, iwidth, ichannel), dtype=float)  # numpy array to store the results of the convolution



    # Padding the image before convolution
    temp = np.zeros((iheight + (2 * padd_h), iwidth + (2 * padd_w), ichannel), dtype=float)
    for i in range(iheight):
        for j in range(iwidth):
            temp[i + padd_h, j + padd_w, :] = image[i, j, :]

    # Performing Convolution
    for k in range(ichannel):
        for i in range(iheight):
            for j in range(iwidth):
                tempp = temp[i:i + kheight, j:j + kwidth, k]
                prod = tempp * kernel
                sum = prod.sum()
                conv[i][j][k] = sum

    conv = np.reshape(conv, (conv.shape[0], conv.shape[1])) if ichannel == 1 else conv

    return conv

