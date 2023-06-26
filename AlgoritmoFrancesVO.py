class PlanDePagos:
    def __init__(self):
        self._NDxA = None #Numero de dias por anio (360 por ser vencido ordinario)
        self._T = None #Tipo de tasa a ingresar
        self._TEA = None #Tasa efectiva anual
        self._TEP = None #Tasa efectiva del periodo
        self._PV = None #Precio de venta del bien
        self._pCI = None #Porcentaje de cuota inicial (en %, no en decimales)
        self._Frec = None #Frecuencia de pago (cada 30 dias por ser vencido ordinario)
        self._NA = None #Numero de anios durante los que se pagara
        self._CI = None #Cuota inicial (numero, ya no porcentaje)
        self._C = None #Cantidad del prestamo
        self._NCxA = None #Numero de cuotas por anio (12 por ser vencido ordinario)
        self._N = None #Numero total de cuotas (numero de cuotas por anio * numero de anios)
        self._PG = None #Tipo de periodo de gracia
        self._NPG = None #Cantidad de periodos que abarca el periodo de gracia
        self._NC = None #Numero actual de cuota
        self._R = None #Cuota del periodo
        self._R2 = None #Cuota delta de R
        self._I = None #Interes del periodo
        self._A =None #Amortizacion del periodo
        self._SI = None #Saldo inicial del periodo
        self._SF = None #Saldo final del periodo
        self._RT = None #Cuota total
        self._AT = None #Amortizacion total
        self._IT = None #Interes total
        self._CN = None #Costos notariales
        self._CR = None #Costos registrales
        self._TSD = None #Tasa del seguro de desgravamen
        self._TSDA = None #Tasa del seguro de desgravamen anual
        self._TSDP = None #Tasa del seguro de desgravamen ajustada al plazo (mensual)
        self._SD = None #Valor monetario del seguro de desgravamen
        self._TSR = None #Tasa del seguro contra todo riesgo
        self._TSRA = None #Tasa del seguro contra todo riesgo anual
        self._TSRP = None #Tasa del seguro contra todo riesgo ajustada al plazo (mensual)
        self._SR = None #Valor monetario del seguro contra todo riesgo
        self._GA = None #Gastos administrativo
        self._P = None #Portes
        self._VPSF = None #Valor presente del saldo final
        self._CP = None #Comision periodica
        self._vueltas = None #Numero de veces que se ha repetido el plan de pagos
        self._AUX = None #Variable auxiliar
        self._AUX2 = None #Variable auxiliar 2
        self._AUX3 = None #Variable auxiliar 3

    @property
    def NDxA(self):
        return self._NDxA

    @NDxA.setter
    def NDxA(self, valor):
        self._NDxA = valor

    @property
    def T(self):
        return self._T

    @T.setter
    def T(self, valor):
        self._T = valor

    @property
    def TEA(self):
        return self._TEA

    @TEA.setter
    def TEA(self, valor):
        self._TEA = valor
    
    @property
    def TEP(self):
        return self._TEP

    @TEP.setter
    def TEP(self, valor):
        self._TEP = valor

    @property
    def PV(self):
        return self._PV

    @PV.setter
    def PV(self, valor):
        self._PV = valor

    @property
    def pCI(self):
        return self._pCI

    @pCI.setter
    def pCI(self, valor):
        self._pCI = valor

    @property
    def Frec(self):
        return self._Frec

    @Frec.setter
    def Frec(self, valor):
        self._Frec = valor

    @property
    def NA(self):
        return self._NA

    @NA.setter
    def NA(self, valor):
        self._NA = valor

    @property
    def CI(self):
        return self._CI

    @CI.setter
    def CI(self, valor):
        self._CI = valor

    @property
    def C(self):
        return self._C

    @C.setter
    def C(self, valor):
        self._C = valor

    @property
    def NCxA(self):
        return self._NCxA

    @NCxA.setter
    def NCxA(self, valor):
        self._NCxA = valor

    @property
    def N(self):
        return self._N

    @N.setter
    def N(self, valor):
        self._N = valor
    
    @property
    def PG(self):
        return self._PG

    @PG.setter
    def PG(self, valor):
        self._PG = valor
    
    @property
    def NPG(self):
        return self._NPG

    @NPG.setter
    def NPG(self, valor):
        self._NPG = valor

    @property
    def R(self):
        return self._R

    @R.setter
    def R(self, valor):
        self._R = valor

    @property
    def R2(self):
        return self._R2

    @R2.setter
    def R2(self, valor):
        self._R2 = valor
    
    @property
    def NC(self):
        return self._NC

    @NC.setter
    def NC(self, valor):
        self._NC = valor

    @property
    def A(self):
        return self._A

    @A.setter
    def A(self, valor):
        self._A = valor
    
    @property
    def SI(self):
        return self._SI

    @SI.setter
    def SI(self, valor):
        self._SI = valor

    @property
    def SF(self):
        return self._SF

    @SF.setter
    def SF(self, valor):
        self._SF = valor

    @property
    def I(self):
        return self._I

    @I.setter
    def I(self, valor):
        self._I = valor

    @property
    def RT(self):
        return self._RT

    @RT.setter
    def RT(self, valor):
        self._RT = valor
    
    @property
    def AT(self):
        return self._AT

    @AT.setter
    def AT(self, valor):
        self._AT = valor
    
    @property
    def IT(self):
        return self._IT

    @IT.setter
    def IT(self, valor):
        self._IT = valor
    
    @property
    def CN(self):
        return self._CN

    @CN.setter
    def CN(self, valor):
        self._CN = valor
    
    @property
    def CR(self):
        return self._CR

    @CR.setter
    def CR(self, valor):
        self._CR = valor

    @property
    def TSD(self):
        return self._TSD

    @TSD.setter
    def TSD(self, valor):
        self._TSD = valor

    @property
    def TSDA(self):
        return self._TSDA

    @TSDA.setter
    def TSDA(self, valor):
        self._TSDA = valor
    
    @property
    def TSDP(self):
        return self._TSDP

    @TSDP.setter
    def TSDP(self, valor):
        self._TSDP = valor

    @property
    def SD(self):
        return self._SD

    @SD.setter
    def SD(self, valor):
        self._SD = valor

    @property
    def TSR(self):
        return self._TSR

    @TSR.setter
    def TSR(self, valor):
        self._TSR = valor

    @property
    def TSRA(self):
        return self._TSRA

    @TSRA.setter
    def TSRA(self, valor):
        self._TSRA = valor

    @property
    def TSRP(self):
        return self._TSRP

    @TSRP.setter
    def TSRP(self, valor):
        self._TSRP = valor

    @property
    def SR(self):
        return self._SR

    @SR.setter
    def SR(self, valor):
        self._SR = valor

    @property
    def GA(self):
        return self._GA

    @GA.setter
    def GA(self, valor):
        self._GA = valor

    @property
    def P(self):
        return self._P

    @P.setter
    def P(self, valor):
        self._P = valor

    @property
    def VPSF(self):
        return self._VPSF

    @VPSF.setter
    def VPSF(self, valor):
        self._VPSF = valor

    @property
    def CP(self):
        return self._CP

    @CP.setter
    def CP(self, valor):
        self._CP = valor

    @property
    def vueltas(self):
        return self._vueltas

    @vueltas.setter
    def vueltas(self, valor):
        self._vueltas = valor

    @property
    def AUX(self):
        return self._AUX

    @AUX.setter
    def AUX(self, valor):
        self._AUX = valor

    @property
    def AUX2(self):
        return self._AUX2

    @AUX2.setter
    def AUX2(self, valor):
        self._AUX2 = valor

    @property
    def AUX3(self):
        return self._AUX3

    @AUX3.setter
    def AUX3(self, valor):
        self._AUX3 = valor

class Ejecutar:
    def __init__(self, plan_de_pagos):
        self._plan = plan_de_pagos

    def PDP(pdp): #ESTE METODO EJECUTA EL PLAN DE PAGOS
        print("N\tTEA\t\tTEP\t\tSaldo Inicial\t\tIntereses\t\tCuota\t\tAmortizacion\t\tSD\t\tSR\t\tSaldo Final")

        while pdp._plan.NC <= pdp._plan.N: #Mientras que el periodo actual sea menor o igual al numero total de periodos de la deuda
            if pdp._plan.NC == 1: #Si el periodo es el primero
                pdp._plan.SI = pdp._plan.AUX3 #El saldo inicial del periodo sera igual al prestamo mas los costos notariales y registrales
            else:
                pdp._plan.SI = pdp._plan.SF #El saldo inicial del periodo actual sera igual al saldo inicial del periodo anterior
            
            pdp._plan.I = pdp._plan.TEP * pdp._plan.SI #Hallar el interes del periodo
            
            if pdp._plan.NC <= pdp._plan.NPG and pdp._plan.PG == "T": #Si el periodo actual es menor o igual que el numero total de periodos del periodo de gracia y es periodo de gracia total
                #calculo del valor monetario del seguro de desgravamen mensual
                pdp._plan.SD = pdp._plan.C * pdp._plan.TSDP

                #calculo del valor monetario del seguro contra todo riesgo mensual
                pdp._plan.SR = pdp._plan.PV * pdp._plan.TSRP
                
                pdp._plan.R = 0 #CUOTA
                pdp._plan.A = 0 #AMORTIZACION
                pdp._plan.SF = pdp._plan.SI + pdp._plan.I
                
                pdp._plan.C = pdp._plan.SF #El valor del prestamo ahora acumula intereses
                
            elif pdp._plan.NC <= pdp._plan.NPG and pdp._plan.PG == "P": #Si el periodo actual es menor o igual que el numero total de periodos del periodo de gracia y es periodo de gracia parcial
                #calculo del valor monetario del seguro de desgravamen mensual
                pdp._plan.SD = pdp._plan.C * pdp._plan.TSDP

                #calculo del valor monetario del seguro contra todo riesgo mensual
                pdp._plan.SR = pdp._plan.PV * pdp._plan.TSRP

                pdp._plan.R = pdp._plan.I #CUOTA
                pdp._plan.A = 0 #AMORTIZACION
                pdp._plan.SF = pdp._plan.SI
                
            else: #Si no hay periodo de gracia
                #calculo del valor monetario del seguro de desgravamen mensual
                pdp._plan.SD = pdp._plan.C * pdp._plan.TSDP

                #calculo del valor monetario del seguro contra todo riesgo mensual
                pdp._plan.SR = pdp._plan.PV * pdp._plan.TSRP

                if pdp._plan.vueltas == 0:
                    pdp._plan.R = pdp._plan.C * (pdp._plan.TEP * (1 + pdp._plan.TEP)**(pdp._plan.N - pdp._plan.NPG)) / ((1 + pdp._plan.TEP)**(pdp._plan.N - pdp._plan.NPG) - 1)
                    pdp._plan.AUX2 = pdp._plan.C
                else:
                    pdp._plan.R = pdp._plan.AUX
                
                pdp._plan.A = pdp._plan.R - pdp._plan.I - pdp._plan.SD - pdp._plan.SR - pdp._plan.GA - pdp._plan.CP - pdp._plan.P #------------------------AQUI CAMBIA------------------------
                pdp._plan.SF = pdp._plan.SI - pdp._plan.A
                
            pdp._plan.RT += pdp._plan.R #Hallar cantidad total de las cuotas

            pdp._plan.AT += pdp._plan.A #Hallar la cantidad total de las amortizaciones

            print(str(pdp._plan.NC) + "\t" + str(round(pdp._plan.TEA*100, 7)) + "%\t" + str(round(pdp._plan.TEP*100, 7))
                  + "%\t" + str(round(pdp._plan.SI, 2)) + "\t" + str(round(pdp._plan.I, 2)) + "\t" + str(round(pdp._plan.R, 2))
                  + "\t" + str(round(pdp._plan.A, 2)) + "\t" + str(round(pdp._plan.SD, 2)) + "\t" + str(round(pdp._plan.SR, 2))
                  + "\t" + str(round(pdp._plan.GA, 2)) + "\t" + str(round(pdp._plan.CP, 2)) + "\t" + str(round(pdp._plan.P, 2))
                  + "\t" + str(round(pdp._plan.SF, 2)))            

            pdp._plan.NC += 1

        while round(pdp._plan.SF, 2) != 0.00:
            pdp._plan.VPSF = pdp._plan.SF / (1 + pdp._plan.TEA)**pdp._plan.NA
            pdp._plan.R2 = pdp._plan.VPSF * (pdp._plan.TEP * (1 + pdp._plan.TEP)**(pdp._plan.N - pdp._plan.NPG)) / ((1 + pdp._plan.TEP)**(pdp._plan.N - pdp._plan.NPG) - 1)
            pdp._plan.R += pdp._plan.R2
            pdp._plan.AUX = pdp._plan.R
            pdp._plan.C = pdp._plan.AUX2

            pdp._plan.NC = 1
            pdp._plan.vueltas += 1
            pdp.PDP()


        pdp._plan.IT = pdp._plan.RT - pdp._plan.AT #Hallar la cantidad total de los intereses

    def correr(self):
        self._plan.NDxA = 360
        self._plan.Frec = 30
        self._plan.NCxA = 12

        #------------------A PARTIR DE AQUI SE LEEN Y VALIDAN LOS DATOS INICIALES------------------
        
        #Ingresar y validar el tipo y el valor de la tasa
        t = str(input("Ingrese el tipo de tasa de su preferencia (Si es Efectiva ingrese E y si es Nominal ingrese N): "))
        while t.upper() != "E" and t.upper() != "N":
            t = input("El tipo de tasa solo puede ser Efectiva (E) o Nominal (N). Ingrese el tipo de tasa correctamente: ")
        
        self._plan.T = t

        if self._plan.T.upper() == "E":
            while True:
                vte = input("Ingrese el valor de la tasa efectiva dividida entre 100: ") #Valor de la tasa efectiva
                try:
                    vte = float(vte)
                    if vte < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\nError: El valor de la tasa efectiva debe ser un numero mayor o igual a cero con o sin decimales.\n")

            #Tipo de tasa efectiva
            te = input("Ingrese el tipo de Tasa Efectiva:\
                       \nTasa Efectiva Anual (TEA)\
                       \nTasa Efectiva Semestral (TES)\
                       \nTasa Efectiva Cuatrimestral (TEC)\
                       \nTasa Efectiva Trimestral (TET)\
                       \nTasa Efectiva Bimestral (TEB)\
                       \nTasa Efectiva Mensual (TEM)\
                       \nTasa Efectiva Quincenal (TEQ)\
                       \nTasa Efectiva Diaria (TED)\
                       \nTipo de Tasa Efectiva: ")

            while te.upper() != "TEA" and te.upper() != "TES" and te.upper() != "TEC" and te.upper() != "TET" and te.upper() != "TEB" and te.upper() != "TEM" and te.upper() != "TEQ" and te.upper() != "TED":
                te = input("Ingrese el tipo de Tasa Efectiva:\
                       \nTasa Efectiva Anual (TEA)\
                       \nTasa Efectiva Semestral (TES)\
                       \nTasa Efectiva Cuatrimestral (TEC)\
                       \nTasa Efectiva Trimestral (TET)\
                       \nTasa Efectiva Bimestral (TEB)\
                       \nTasa Efectiva Mensual (TEM)\
                       \nTasa Efectiva Quincenal (TEQ)\
                       \nTasa Efectiva Diaria (TED)\
                       \nTipo de Tasa Efectiva: ")
                
            if te.upper() == "TES":
                self._plan.TEA = ((1 + vte) ** 2) - 1
            elif te.upper() == "TEC":
                self._plan.TEA = ((1 + vte) ** 3) - 1
            elif te.upper() == "TET":
                self._plan.TEA = ((1 + vte) ** 4) - 1
            elif te.upper() == "TEB":
                self._plan.TEA = ((1 + vte) ** 6) - 1
            elif te.upper() == "TEM":
                self._plan.TEA = ((1 + vte) ** 12) - 1
            elif te.upper() == "TEQ":
                self._plan.TEA = ((1 + vte) ** 24) - 1
            elif te.upper() == "TED":
                self._plan.TEA = ((1 + vte) ** 360) - 1
            else:
                self._plan.TEA = vte

        else: #EN CASO SEA UNA TASA NOMINAL
            while True:
                vtn = input("Ingrese el valor de la tasa nominal dividida entre 100: ") #Valor de la tasa nominal
                try:
                    vtn = float(vtn)
                    if vtn < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\nError: El valor de la tasa nominal debe ser un numero mayor o igual a cero con o sin decimales.\n")

            #Tipo de tasa nominal
            tn = input("Ingrese el tipo de Tasa Nominal:\
                       \nTasa Nominal Anual (TNA)\
                       \nTasa Nominal Semestral (TNS)\
                       \nTasa Nominal Cuatrimestral (TNC)\
                       \nTasa Nominal Trimestral (TNT)\
                       \nTasa Nominal Bimestral (TNB)\
                       \nTasa Nominal Mensual (TNM)\
                       \nTasa Nominal Quincenal (TNQ)\
                       \nTasa Nominal Diaria (TND)\
                       \nTipo de Tasa Nominal: ")
            
            while tn.upper() != "TNA" and tn.upper() != "TNS" and tn.upper() != "TNC" and tn.upper() != "TNT" and tn.upper() != "TNB" and tn.upper() != "TNM" and tn.upper() != "TNQ" and tn.upper() != "TND":
                tn = input("\nIngrese correctamente el tipo de Tasa Nominal:\
                       \nTasa Nominal Anual (TNA)\
                       \nTasa Nominal Semestral (TNS)\
                       \nTasa Nominal Cuatrimestral (TNC)\
                       \nTasa Nominal Trimestral (TNT)\
                       \nTasa Nominal Bimestral (TNB)\
                       \nTasa Nominal Mensual (TNM)\
                       \nTasa Nominal Quincenal (TNQ)\
                       \nTasa Nominal Diaria (TND)\
                       \nTipo de Tasa Nominal: ")
            
            while True:
                cap = input("Ingrese la frecuencia de la capitalizacion en dias: ") #Frecuencia de capitalizacion en dias
                try:
                    cap = int(cap)
                    if cap < 0:
                        raise ValueError
                    break
                except ValueError:
                    print("\nError: La frecuencia de capitalizacion de la tasa nominal debe ser un numero entero mayor que 0.\n")
            
            tna = 0.0
            m = int(360 / cap) #Numero de periodos de capitalizacion

            if tn.upper() == "TNS":
                tna = vtn * 2 #Tasa nominal anual
            elif tn.upper() == "TNC":
                tna = vtn * 3 #Tasa nominal anual
            elif tn.upper() == "TNT":
                tna = vtn * 4 #Tasa nominal anual
            elif tn.upper() == "TNB":
                tna = vtn * 6 #Tasa nominal anual
            elif tn.upper() == "TNM":
                tna = vtn * 12 #Tasa nominal anual
            elif tn.upper() == "TNQ":
                tna = vtn * 24 #Tasa nominal anual
            elif tn.upper() == "TND":
                tna = vtn * 360 #Tasa nominal anual
            else:
                tna = vtn * 1 #Tasa nominal anual

            self._plan.TEA = ((1 + tna / m) ** m) - 1

        #Ingresar y validar Precio de venta PV
        while True:
            pv = input("Ingrese el precio de venta del bien: ")
            try:
                pv = float(pv)
                if pv < 1:
                    raise ValueError
                self._plan.PV = pv
                break
            except ValueError:
                print("\nError: El precio de venta debe ser un numero con decimales mayor que 0.\n")

        #Ingresar y validar Porcentaje de cuota inicial pCI
        while True:
            pci = input("Ingrese el porcentaje de la cuota inicial dividido entre 100: ")
            try:
                pci = float(pci)
                if pci < 0:
                    raise ValueError
                self._plan.pCI = pci
                break
            except ValueError:
                print("\nError: El porcentaje de la cuota inicial debe ser un numero con o sin decimales mayor o igual que 0.\n")

        #Ingresar y validar Numero de anios NA
        while True:
            na = input("Ingrese el numero de anios durante los que pagara: ")
            try:
                na = int(na)
                if na < 1:
                    raise ValueError
                self._plan.NA = na
                break
            except ValueError:
                print("\nError: El numero de anios debe ser un numero entero mayor que 0.\n")
        
        #Ingresar y validar el tipo de periodo de gracia
        pg = input("Ingrese el tipo de periodo de gracia (Total 'T'/Parcial 'P'/No considera periodo de gracia 'N'): ")
        
        while pg.upper() != "T" and pg.upper() != "P" and pg.upper() != "N":
            pg = input("\nIngrese correctamente el tipo de periodo de gracia (Total 'T'/Parcial 'P'/No considera periodo de gracia 'N'): ")

        self._plan.PG = pg.upper()

        #Ingresar y validar la cantidad de meses que dura el periodo de gracia

        self._plan.NPG = 0

        if self._plan.PG != "N":
            while True:
                npg = input("Ingrese en numeros enteros la cantidad de periodos del periodo de gracia: ")
                try:
                    npg = int(npg)
                    if npg < 1:
                        raise ValueError
                    self._plan.NPG = npg
                    break
                except ValueError:
                    print("\nError: La cantidad de periodos del periodo de gracia debe ser un numero entero mayor que 0.\n")

        #Ingresar y validar tasa del seguro de desgravamen

        while True:
            tsd = input("Ingrese la tasa del seguro de desgravamen dividido entre 100: ")
            try:
                tsd = float(tsd)
                if tsd < 0:
                    raise ValueError
                self._plan.TSD = tsd
                break
            except ValueError:
                print("\nError: La tasa del seguro de desgravamen debe ser un numero mayor o igual a cero.\n")

        #Ingresar y validar tasa del seguro contra todo riesgo

        while True:
            tsr = input("Ingrese la tasa del seguro contra todo riesgo dividido entre 100: ")
            try:
                tsr = float(tsr)
                if tsr < 0:
                    raise ValueError
                self._plan.TSR = tsr
                break
            except ValueError:
                print("\nError: La tasa del seguro contra todo riesgo debe ser un numero mayor o igual a cero.\n")

        #Ingresar y validar gastos administrativos

        while True:
            ga = input("Ingrese los gastos administrativos: ")
            try:
                ga = float(ga)
                if ga < 0:
                    raise ValueError
                self._plan.GA = ga
                break
            except ValueError:
                print("\nError: Los gastos administrativos deben ser un numero mayor o igual a cero.\n")

        #Ingresar y validar portes

        while True:
            p = input("Ingrese los portes: ")
            try:
                p = float(p)
                if p < 0:
                    raise ValueError
                self._plan.P = p
                break
            except ValueError:
                print("\nError: Los portes deben ser un numero mayor o igual a cero.\n")

        #Ingresar y validar comisiones periodicas

        while True:
            cp = input("Ingrese la comision periodica: ")
            try:
                cp = float(cp)
                if cp < 0:
                    raise ValueError
                self._plan.CP = cp
                break
            except ValueError:
                print("\nError: La comision periodica debe ser un numero mayor o igual a cero.\n")

        #Ingresar y validar costos notariales

        while True:
            cn = input("Ingrese los costos notariales: ")
            try:
                cn = float(cn)
                if cn < 0:
                    raise ValueError
                self._plan.CN = cn
                break
            except ValueError:
                print("\nError: Los costos notariales deben ser un número mayor o igual a cero.\n")

        #Ingresar y validar costos registrales

        while True:
            cr = input("Ingrese los costos registrales: ")
            try:
                cr = float(cr)
                if cr < 0:
                    raise ValueError
                self._plan.CR = cr
                break
            except ValueError:
                print("\nError: Los costos registrales deben ser un número mayor o igual a cero.\n")

        #------------------A PARTIR DE AQUI SE PROCESAN LOS DATOS INTERMEDIOS------------------
        
        #Calcular cuota inicial (en numero, ya no en porcentaje) CI
        self._plan.CI = self._plan.pCI * self._plan.PV

        #Calcular prestamo C
        self._plan.C = self._plan.PV - self._plan.CI + self._plan.CN + self._plan.CR #Los costos notariales y registales se adjudican al monto del prestamo
        self._plan.AUX3 = self._plan.C

        #Calcular numero total de cuotas
        self._plan.N = self._plan.NCxA * self._plan.NA #CAMBIO AQUI

        #Inicializacion del periodo actual
        self._plan.NC = 1
        
        #Inicializacion del saldo final
        self._plan.SF = 0

        #Inicializacion de la cuota total
        self._plan.RT = 0

        #Inicializacion de la amortizacion total
        self._plan.AT = 0

        #Inicializacion del numero de veces que se ha repetido el plan de pagos
        self._plan.vueltas = 0

        #Inicializacion de la tasa del periodo (la tasa sera mensual)
        self._plan.TEP = (1 + self._plan.TEA) ** (1 / 12) - 1

        #Calculo de la tasa de seguro de desgravamen anual
        self._plan.TSDA = self._plan.TSD * 12

        #Calculo de la Tasa de Seguro de Desgravamen Ajustada al Plazo
        self._plan.TSDP = self._plan.TSDA / 360 * 30

        #Calculo de la tasa de seguro contra todo reisgo anual
        self._plan.TSRA = self._plan.TSR * 12

        #Calculo de la Tasa de Seguro Contra Todo Riesgo Ajustada al Plazo
        self._plan.TSRP = self._plan.TSRA / 360 * 30

        #------------------A PARTIR DE AQUI SE CALCULA EL PLAN DE PAGOS------------------

        self.PDP()

        print(self._plan.VPSF)
        print(self._plan.R2)

        #-----------------------------CONTINUAR DESDE LA SESION 11_2 1 H 39 MIN-----------------------------

    def imprimirInformacion(self):
        print("\nNumero de dias por anio:", self._plan.NDxA)
        print("Precio de venta del bien:", self._plan.PV)
        print("Porcentaje de la cuota inicial: " + str(round(self._plan.pCI * 100, 7)) + "%")
        print("Frecuencia de pago: " + str(self._plan.Frec) + " dias")
        print("Numero de anios:", self._plan.NA)
        print("Cuota inicial:", round(self._plan.CI,2))
        print("Prestamo:", round(self._plan.C,2))
        print("Numero de cuotas por anio:", self._plan.NCxA)
        print("Numero total de cuotas:", self._plan.N)
        print("Tasa Efectiva Anual: " + str(round(self._plan.TEA * 100, 7)) + "%")
        print("Tipo de periodo de gracia: ", self._plan.PG)
        print("Cantidad de periodos del periodo de gracia: ", self._plan.NPG)
        print("Amortizacion total: " +  str(round(self._plan.AT, 2)))
        print("Gastos administrativos: ", self._plan.GA)
        print("Portes: ", self._plan.P)
        print("Costos notariales: ", self._plan.CN)
        print("Costos registrales: ", self._plan.CR)
        print("TSD: " + str(round(self._plan.TSD * 100, 7)) + "%")
        print("Seguro de desgravamen: " + str(round(self._plan.SD, 2)))
        print("Seguro contra todo riesgo: " + str(round(self._plan.SR, 2)))

def main():
    plan = PlanDePagos()
    ejecutar = Ejecutar(plan)
    ejecutar.correr()
    ejecutar.imprimirInformacion()

if __name__ == "__main__":
    main()
