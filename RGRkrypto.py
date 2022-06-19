class RGRCrypto():
    def __init__(self):
        self.program()

    def table(self, n1, n2):
        num = 0
        self.x0 = 1
        self.x1 = 0
        self.y0 = 0
        self.y1 = 1
        while True:
            if num == 0 or num == 1:
                if num == 0:
                    print(f'{num}  q: -     n1: {n1}        n2: {n2}        xi: {self.x0}       yi: {self.y0}')
                if num == 1:
                    q = n1 // n2
                    ostatok = n1 % n2
                    n1 = n2
                    n2 = ostatok
                    print(f'{num}  q: {q}       n1: {n1}        n2: {n2}        xi: {self.x1}       yi: {self.y1}')
            if num>1:
                self.x = self.x0 - self.x1 * q
                self.y = self.y0 - self.y1 * q
                q = n1 // n2
                ostatok = n1 % n2
                n1 = n2
                n2 = ostatok
                print(f'{num}  q: {q}       n1: {n1}        n2: {n2}        xi: {self.x}        yi: {self.y}')
                self.x0 = self.x1
                self.x1 = self.x
                self.y0 = self.y1
                self.y1 = self.y
            num+=1
            if n2 == 0:
                break

    def task1(self,b,c):
        while True:
            try:
                self.num = int(input("Введите целое число или пропустите чтобы вернуться в начальное меню: "))
            except ValueError:self.program()
            d = self.num ** b
            e = d % c
            print("вот остаток", e)


    def program(self):
        while True:
            print("\n\nЕсли задание требует значения yi из таблици сначала нажмите 1")
            print("1.table\n2.task1\n3.task2\n4.task4")
            self.choise=input("Chose next: ")
            if self.choise == '1':
                try:
                    n1 = int(input("n1: "))
                    n2 = int(input("n2: "))
                    self.table(n1=n1, n2=n2)
                except ValueError:self.program()
            elif self.choise == '2':
                try:
                    self.modnum = int(input("Введите модульное число: "))
                except ValueError:self.program()
                self.task1(c=self.modnum, b=self.y1)
            elif self.choise == '3':
                try:
                    modn = int(input("mod n = "))
                    G = int(input("G= "))
                    v = int(input("v= "))
                    r = int(input("r= "))
                    d = int(input("d= "))
                    modGv = (G ** v) % modn
                    print(f"G^v=_{modGv}(mod{modn})")
                    self.table(n1=modn, n2=modGv)
                    J = self.y1
                    modJ = J%modn
                    modT = (r ** v) % modn
                    modD = (r * (G ** d)) % modn
                    modT1 = ((modD ** v) * (modJ ** d)) % modn
                    print(f"\nJ≡{modJ} (mod {modn})\nT≡{modT}(mod{modn})", f"\nD≡{modD}(mod{modn})", f"\nT`≡{modT1}(mod{modn})")
                except ValueError:self.program()
            elif self.choise == '4':
                try:
                    p = int(input("p = "))
                    q = int(input("q = "))
                    x = int(input("x = "))
                    m = int(input("m=h(M) = "))
                    k = int(input("k = "))
                    modY = (q ** x) % p
                    moda = (q ** k) % p
                    self.table(n1=p-1,n2=k)
                    k_1 = self.y1
                    modb = k_1*(m - moda * x) % (p-1)
                    V = ((modY ** moda) * (moda ** modb)) % p
                    W = (q ** m) % p
                    print(f"Y≡{modY}(mod {p})\na≡{moda} (mod {p})\nk^-1 = {k_1}\nb≡{modb} (mod {p - 1})\nV ≡ {V} (mod {p})\nW ≡ {W} (mod {p})")
                except ValueError:self.program()
            else:self.program()

if __name__ == "__main__":
    RGRCrypto()
