print ('program menghitung luas, volume, dan keliling balok')
p=int(input('masukkan panjang balok: '))
l=int(input('masukkan lebar balok: '))
t=int(input('masukkan tinggi balok: '))

def luas_permukaan(p,l,t): 
    L=2*((p*l)+(p*t)+(l*t))
    return L

def volume(p,l,t):
    V=p*l*t
    return V

def keliling(p,l,t):
    K=4*(p+l+t)
    return K

print ('jadi balok dengan panjang: {}, lebar: {}, dan tinggi: {} \n mempunyai luas:{}, volume:{}, dan keliling: {}'.format(p,l,t,luas_permukaan(p,l,t),volume(p,l,t),keliling(p,l,t)))
