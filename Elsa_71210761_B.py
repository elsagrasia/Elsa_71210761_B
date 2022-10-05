class NodeMahasiswa:
    def __init__(self,nama,ipk,n=None,p=None):
        self._element = nama   
        self._ipk = ipk
        self._next = n
        self._prev = p

    def getNama(self):
        return self._element

    def getIpk(self):
        return self._ipk

    def setNama(self,nama):
        self._element = nama

    def setIpk(self,ipk):
        self._ipk = ipk

class DLLNC:
    def __init__(self):
        self._head=None
        self._tail=None
        self._size = 0

    def __len__(self):
        return self._size
    
    def isEmpty(self):
        return self._size == 0


    def addElementTail(self,nama,ipk):
        baru = NodeMahasiswa(nama,ipk, None, None)
        if self.isEmpty()==True:
            self._head = baru
            self._tail = baru
            self._head._next = None
            self._head._prev = None
            self._tail._next = None
            self._tail._prev = None
        else:
            baru._next = self._head
            self._head._prev = baru
            self._head = baru
        self._size += 1
        print("data masuk ke tail")

    def deleteLast(self):
        if self.isEmpty() == False:
            d = None
            bantu = self._head
            if(self._head._next != None):
                hapus = self._tail 
                self._tail = self._tail._prev
                d = hapus._element
                self._tail._next = None
                del hapus
            else :
                d = self._tail._element
                self._head=tail=None
            self._size -= 1
            print(d, " terhapus!")
        else:
            print("Kosong!")
     
    def printDescending(self):
        if self.isEmpty()==False:
            bantu = self._tail
            while(bantu._prev !=None):
                print("Nama : ", bantu.getNama(), "\nIPK : ", bantu.getIpk())
                bantu = bantu._prev
            print()
        else:
            print("Kosong")  

    def rataIpk(self):
        helper = self._head
        totalIpk = 0
        while(helper!=None):
            totalIpk += helper.getIpk()    
            helper = helper._next
        rataRata=round(totalIpk/self._size,2)
        print('Rata - rata: ', rataRata)

#TEST CASE
DLLNC1 = DLLNC()
DLLNC1.addElementTail('Shalom',3.9)
DLLNC1.addElementTail('Nabilla',3.8)
DLLNC1.addElementTail('Kurniadi',3.7)
DLLNC1.addElementTail('Harris',3.6)
DLLNC1.printDescending()

DLLNC1.deleteLast()
DLLNC1.printDescending()

DLLNC1.rataIpk()