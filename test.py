import os
import sys
import pywt
from pywt import wavedec
from __init__ import ap_entropy, samp_entropy
import numpy as np
import matplotlib
from matplotlib import pyplot as plt
from nn import mlp, create_training_set
A=[]
B=[]
C=[]
D=[]
E=[]
for fl in os.listdir("../../ALL/A/"):
                inp = []
                path = "../../ALL/A/" + fl
                txt = open(path,'r')
                for line in txt:
                        feature = line.split()[0]
                        inp.append(feature)
		a = np.array(inp)
                A.append(a)

for fl in os.listdir("../../ALL/B/"):
                inp = []
                path = "../../ALL/B/" + fl
                txt = open(path,'r')
                for line in txt:
                        feature = line.split()[0]
                        inp.append(feature)
                a = np.array(inp)
                B.append(a)

for fl in os.listdir("../../ALL/C/"):
                inp = []
                path = "../../ALL/C/" + fl
                txt = open(path,'r')
                for line in txt:
                        feature = line.split()[0]
                        inp.append(feature)
                a = np.array(inp)
                C.append(a)

for fl in os.listdir("../../ALL/D/"):
                inp = []
                path = "../../ALL/D/" + fl
                txt = open(path,'r')
                for line in txt:
                        feature = line.split()[0]
                        inp.append(feature)
                a = np.array(inp)
                D.append(a)

for fl in os.listdir("../../ALL/E/"):
                inp = []
                path = "../../ALL/E/" + fl
                txt = open(path,'r')
                for line in txt:
                        feature = line.split()[0]
                        inp.append(feature)
                a = np.array(inp)
                E.append(a)

A_ = []
B_ = []
C_ = []
D_ = []
E_ = []
for x in A:
	coeffs = wavedec(x,'db4',level=8)
	A_.append(coeffs)
	
for x in B:
	coeffs = wavedec(x,'db4',level=8)
	B_.append(coeffs)
	
for x in C:
	coeffs = wavedec(x,'db4',level=8)
	C_.append(coeffs)
for x in D:
	coeffs = wavedec(x,'db4',level=8)
	D_.append(coeffs)
for x in E:
	coeffs = wavedec(x,'db4',level=8)
	E_.append(coeffs)

a=[]
b=[]
c=[]
d=[]
e=[]
y_a = []
y_b = []
y_c = []
y_d = []
y_e = []
minm = [1000000000000 for i in range(1,46)]
maxm = [0 for i in range(1,46)]
inp = []
out = []
for x in A_:
	features = []
	j=0
	for y in x:
		coef = np.array(y)
		energy = np.sum(coef**2)
		minm[j] = min(minm[j],energy)
		maxm[j] = max(maxm[j],energy)
		j=j+1
		approx_en = ap_entropy(coef,2,0.5)
		minm[j] = min(minm[j],approx_en)
		maxm[j] = max(maxm[j],approx_en)
		j=j+1
		samp_en = samp_entropy(coef,2,0.5)
		minm[j] = min(minm[j],samp_en)
		maxm[j] = max(maxm[j],samp_en)
		j=j+1
		mean = np.mean(coef)
		minm[j]= min(minm[j],mean)
		maxm[j] = max(maxm[j],mean)
		j=j+1
		std = np.std(coef)
		minm[j] = min(minm[j],std)
		maxm[j] = max(maxm[j],std)
		j=j+1
		features.append(energy)
		features.append(approx_en)
		features.append(samp_en)
		features.append(mean)
		features.append(std)
	a.append(features)
	y_a.append(0)

print("A done")

for x in B_:
        features = []
	j=0
        for y in x:
                coef = np.array(y)
                energy = np.sum(coef**2)
		minm[j] = min(minm[j],energy)
		maxm[j] = max(maxm[j],energy)
                j=j+1
                approx_en = ap_entropy(coef,2,0.5)
                minm[j] = min(minm[j],approx_en)
		maxm[j] = max(maxm[j],approx_en)
                j=j+1
                samp_en = samp_entropy(coef,2,0.5)
                minm[j] = min(minm[j],samp_en)
		maxm[j] = max(maxm[j],samp_en)
                j=j+1
                mean = np.mean(coef)
                minm[j]= min(minm[j],mean)
		maxm[j] = max(maxm[j],mean)
                j=j+1
                std = np.std(coef)
                minm[j] = min(minm[j],std)
		maxm[j]= max(maxm[j],std)
                j=j+1

                features.append(energy)
                features.append(approx_en)
                features.append(samp_en)
                features.append(mean)
                features.append(std)
        b.append(features)
	y_b.append(1)

print("B done")
for x in C_:
        features = []
	j=0
        for y in x:
                coef = np.array(y)
                energy = np.sum(coef**2)
		minm[j] = min(minm[j],energy)
                maxm[j] = max(maxm[j],energy)
                j=j+1
                approx_en = ap_entropy(coef,2,0.5)
                minm[j] = min(minm[j],approx_en)
                maxm[j] = max(maxm[j],approx_en)
                j=j+1
                samp_en = samp_entropy(coef,2,0.5)
                minm[j] = min(minm[j],samp_en)
                maxm[j] = max(maxm[j],samp_en)
                j=j+1
                mean = np.mean(coef)
                minm[j]= min(minm[j],mean)
                maxm[j] = max(maxm[j],mean)
                j=j+1
                std = np.std(coef)
                minm[j] = min(minm[j],std)
                maxm[j]= max(maxm[j],std)
                j=j+1


                features.append(energy)
                features.append(approx_en)
                features.append(samp_en)
                features.append(mean)
                features.append(std)
        c.append(features)
	y_c.append(2)

print("C done")
for x in D_:
        features = []
	j=0
        for y in x:
                coef = np.array(y)
                energy = np.sum(coef**2)
		
		minm[j] = min(minm[j],energy)
                maxm[j] = max(maxm[j],energy)
                j=j+1
                approx_en = ap_entropy(coef,2,0.5)
                minm[j] = min(minm[j],approx_en)
                maxm[j] = max(maxm[j],approx_en)
                j=j+1
                samp_en = samp_entropy(coef,2,0.5)
                minm[j] = min(minm[j],samp_en)
                maxm[j] = max(maxm[j],samp_en)
                j=j+1
                mean = np.mean(coef)
                minm[j]= min(minm[j],mean)
                maxm[j] = max(maxm[j],mean)
                j=j+1
                std = np.std(coef)
                minm[j] = min(minm[j],std)
                maxm[j]= max(maxm[j],std)
                j=j+1


                features.append(energy)
                features.append(approx_en)
                features.append(samp_en)
                features.append(mean)
                features.append(std)
        d.append(features)
	y_d.append(3)

print("D Done")

for x in E_:
        features = []
	j=0
        for y in x:
                coef = np.array(y)
                energy = np.sum(coef**2)
			
		minm[j] = min(minm[j],energy)
                maxm[j] = max(maxm[j],energy)
                j=j+1
                approx_en = ap_entropy(coef,2,0.5)
                minm[j] = min(minm[j],approx_en)
                maxm[j] = max(maxm[j],approx_en)
                j=j+1
                samp_en = samp_entropy(coef,2,0.5)
                minm[j] = min(minm[j],samp_en)
                maxm[j] = max(maxm[j],samp_en)
                j=j+1
                mean = np.mean(coef)
                minm[j]= min(minm[j],mean)
                maxm[j] = max(maxm[j],mean)
                j=j+1
                std = np.std(coef)
                minm[j] = min(minm[j],std)
                maxm[j]= max(maxm[j],std)
                j=j+1



                features.append(energy)
                features.append(approx_en)
                features.append(samp_en)
                features.append(mean)
                features.append(std)
        e.append(features)
	y_e.append(4)
print("E done")
i=0
while i < 100:
	inp.append(a[i])
	out.append(y_a[i])
	inp.append(b[i])
	out.append(y_b[i])
	inp.append(c[i])
	out.append(y_c[i])
	inp.append(d[i])
	out.append(y_d[i])
	inp.append(e[i])
	out.append(y_e[i])
	i=i+1

i=0
z= [i for i in range(1,len(e)+1)]
import matplotlib.pyplot as plt
while i < 49:
	j=0
	p=[]
	q=[]
	r=[]
	s=[]
	t=[]
	u=[]
	while j < len(e):
		p.append(a[j][i])
		q.append(b[j][i])
		r.append(c[j][i])
		s.append(d[j][i])
		t.append(e[j][i])
		j=j+1
	plt.plot(z,np.array(p))
	plt.plot(z,np.array(q))
	plt.plot(z,np.array(r))
	plt.plot(z,np.array(s))
	plt.plot(z,np.array(t))
        plt.savefig("images/"+str(i)+"_out.jpg")
        plt.clf()
	i=i+1
print("done")
P,Q,R,S,T,U = create_training_set(inp,out,minm,maxm)
mlp(P,Q,R,S,T,U)

