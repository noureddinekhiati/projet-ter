from matplotlib import pyplot as plt
import numpy as np
def extarct_data():
    gan = 'G_GAN: '
    gl1 = 'G_L1: '
    dreal = 'D_real: '
    dfake = 'D_fake: '
    f = open('loss_log.txt')
    gan_list=[0]
    gl1_list = [0]
    dreal_list = [0]
    dfake_list = [0]
    for line in f:
        gan_pos = line.find(gan) + len(gan)
        gl1_pos = line.find(gl1) + len(gl1)
        dreal_pos = line.find(dreal) + len(dreal)
        dfake_pos = line.find(dfake) + len(dfake)
        if gan in line:
            gan_list.append(float(line[gan_pos:gan_pos+5]))
        if gl1 in line:
            gl1_list.append(float(line[gl1_pos:gl1_pos+5]))
        if dreal in line:
            dreal_list.append(float(line[dreal_pos:dreal_pos + 5]))
        if dfake in line:
            dfake_list.append(float(line[dfake_pos:]))
    return gan_list,gl1_list,dreal_list,dfake_list

def plot_loss():
    gan,gl1,dreal,dfake = extarct_data()
    gan_moy =[ sum(gan[i:i+7])/7 for i in range(0, len(gan) - 7, 7) ]
    gl1_moy = [ sum(gl1[i:i+7])/7 for i in range(0, len(gl1) - 7, 7) ]
    dfake_moy = [sum(dfake[i:i + 7]) / 7 for i in range(0, len(dfake) - 7, 7)]
    dreal_moy = [sum(dreal[i:i + 7]) / 7 for i in range(0, len(dreal) - 7, 7)]
    return gan_moy,gl1_moy,dfake_moy,dreal_moy

gan,gl1,dreal,dfake= plot_loss()
plt.plot(gan,label="G_GAN")
plt.plot(gl1,label="G_L1")
plt.plot(dreal,label="D_real")
plt.plot(dfake,label="D_fake")
plt.show()
#[8.973, 14.729833333333334, 9.618166666666665
