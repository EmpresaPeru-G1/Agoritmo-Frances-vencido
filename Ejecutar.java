import java.util.Scanner;

public class Ejecutar {
    private PlanDePagos plan;

    public Ejecutar(PlanDePagos plan) {
        this.plan = plan;
    }

    public void PDP() {
        System.out.println("N\tTEA\t\tTEP\t\tSaldo Inicial\t\tIntereses\t\tCuota\t\tAmortizacion\t\tSD\t\tSR\t\tSaldo Final");

        while (this.plan.getNC() <= this.plan.getN()) {
            if (this.plan.getNC() == 1) {
                this.plan.setSI(this.plan.getAUX3());
            } else {
                this.plan.setSI(this.plan.getSF());
            }

            this.plan.setI(this.plan.getTEP() * this.plan.getSI());

            if (this.plan.getNC() <= this.plan.getNPG() && this.plan.getPG().equals("T")) {
                this.plan.setSD(this.plan.getC() * this.plan.getTSDP());
                this.plan.setSR(this.plan.getPV() * this.plan.getTSRP());
                this.plan.setR(0);
                this.plan.setA(0);
                this.plan.setSF(this.plan.getSI() + this.plan.getI());
                this.plan.setC(this.plan.getSF());
            } else if (this.plan.getNC() <= this.plan.getNPG() && this.plan.getPG().equals("P")) {
                this.plan.setSD(this.plan.getC() * this.plan.getTSDP());
                this.plan.setSR(this.plan.getPV() * this.plan.getTSRP());
                this.plan.setR(this.plan.getI());
                this.plan.setA(0);
                this.plan.setSF(this.plan.getSI());
            } else {
                this.plan.setSD(this.plan.getC() * this.plan.getTSDP());
                this.plan.setSR(this.plan.getPV() * this.plan.getTSRP());

                if (this.plan.getVueltas() == 0) {
                    this.plan.setR(this.plan.getC() * (this.plan.getTEP() * Math.pow(1 + this.plan.getTEP(), this.plan.getN() - this.plan.getNPG())) / (Math.pow(1 + this.plan.getTEP(), this.plan.getN() - this.plan.getNPG()) - 1));
                    this.plan.setAUX2(this.plan.getC());
                } else {
                    this.plan.setR(this.plan.getAUX());
                }

                this.plan.setA(this.plan.getR() - this.plan.getI() - this.plan.getSD() - this.plan.getSR() - this.plan.getGA() - this.plan.getCP() - this.plan.getP());
                this.plan.setSF(this.plan.getSI() - this.plan.getA());
            }

            this.plan.setRT(this.plan.getRT() + this.plan.getR());
            this.plan.setAT(this.plan.getAT() + this.plan.getA());

            System.out.println(String.format("%d\t%.7f%%\t%.7f%%\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f",
                    this.plan.getNC(), this.plan.getTEA() * 100, this.plan.getTEP() * 100, this.plan.getSI(), this.plan.getI(), this.plan.getR(), this.plan.getA(),
                    this.plan.getSD(), this.plan.getSR(), this.plan.getGA(), this.plan.getCP(), this.plan.getP(), this.plan.getSF()));

            this.plan.setNC(this.plan.getNC() + 1);
        }

        while (Math.round(this.plan.getSF() * 100.0) / 100.0 != 0.00) {
            this.plan.setVPSF(this.plan.getSF() / Math.pow(1 + this.plan.getTEA(), this.plan.getNA()));
            this.plan.setR2(this.plan.getVPSF() * (this.plan.getTEP() * Math.pow(1 + this.plan.getTEP(), this.plan.getN() - this.plan.getNPG())) / (Math.pow(1 + this.plan.getTEP(), this.plan.getN() - this.plan.getNPG()) - 1));
            this.plan.setR(this.plan.getR() + this.plan.getR2());
            this.plan.setAUX(this.plan.getR());
            this.plan.setC(this.plan.getAUX2());

            this.plan.setNC(1);
            this.plan.setVueltas(this.plan.getVueltas()+1);
            PDP();
        }

        this.plan.setIT(this.plan.getRT() - this.plan.getAT());
    }

    public void correr(){
        this.plan.setNDxA(360);
        this.plan.setFrec(30);
        this.plan.setNCxA(12);

        // A PARTIR DE AQUI SE LEEN Y VALIDAN LOS DATOS INICIALES

        // Crear objeto Scanner para leer la entrada del usuario
        Scanner scanner = new Scanner(System.in);

        // Ingresar y validar el tipo y el valor de la tasa
        System.out.print("Ingrese el tipo de tasa de su preferencia (Si es Efectiva ingrese E y si es Nominal ingrese N): ");
        String t = scanner.nextLine();
        while (!t.equalsIgnoreCase("E") && !t.equalsIgnoreCase("N")) {
            System.out.print("El tipo de tasa solo puede ser Efectiva (E) o Nominal (N). Ingrese el tipo de tasa correctamente: ");
            t = scanner.nextLine();
        }

        // Asignar el valor al atributo T de la instancia de la clase PlanDePagos
        this.plan.setT(t);

        double vte = 0.0;

        if (this.plan.getT().equalsIgnoreCase("E")) {            
            while (true) {
                System.out.print("Ingrese el valor de la tasa efectiva dividida entre 100: ");
                String vteInput = scanner.nextLine(); // Valor de la tasa efectiva
                
                try {
                    vte = Double.parseDouble(vteInput);
                    
                    if (vte < 0) {
                        throw new NumberFormatException();
                    }
                    
                    break;
                } catch (NumberFormatException e) {
                    System.out.println("\nError: El valor de la tasa efectiva debe ser un número mayor o igual a cero con o sin decimales.\n");
                }
            }

            String te;
            System.out.print("Ingrese el tipo de Tasa Efectiva:\n" +
                    "Tasa Efectiva Anual (TEA)\n" +
                    "Tasa Efectiva Semestral (TES)\n" +
                    "Tasa Efectiva Cuatrimestral (TEC)\n" +
                    "Tasa Efectiva Trimestral (TET)\n" +
                    "Tasa Efectiva Bimestral (TEB)\n" +
                    "Tasa Efectiva Mensual (TEM)\n" +
                    "Tasa Efectiva Quincenal (TEQ)\n" +
                    "Tasa Efectiva Diaria (TED)\n" +
                    "Tipo de Tasa Efectiva: ");
            te = scanner.nextLine();

            while (!te.equalsIgnoreCase("TEA") && !te.equalsIgnoreCase("TES") && !te.equalsIgnoreCase("TEC") &&
                    !te.equalsIgnoreCase("TET") && !te.equalsIgnoreCase("TEB") && !te.equalsIgnoreCase("TEM") &&
                    !te.equalsIgnoreCase("TEQ") && !te.equalsIgnoreCase("TED")) {
                System.out.print("Ingrese el tipo de Tasa Efectiva:\n" +
                        "Tasa Efectiva Anual (TEA)\n" +
                        "Tasa Efectiva Semestral (TES)\n" +
                        "Tasa Efectiva Cuatrimestral (TEC)\n" +
                        "Tasa Efectiva Trimestral (TET)\n" +
                        "Tasa Efectiva Bimestral (TEB)\n" +
                        "Tasa Efectiva Mensual (TEM)\n" +
                        "Tasa Efectiva Quincenal (TEQ)\n" +
                        "Tasa Efectiva Diaria (TED)\n" +
                        "Tipo de Tasa Efectiva: ");
                te = scanner.nextLine();
            }

            if (te.equalsIgnoreCase("TES")) {
                this.plan.setTEA(Math.pow(1 + vte, 2) - 1);
            } else if (te.equalsIgnoreCase("TEC")) {
                this.plan.setTEA(Math.pow(1 + vte, 3) - 1);
            } else if (te.equalsIgnoreCase("TET")) {
                this.plan.setTEA(Math.pow(1 + vte, 4) - 1);
            } else if (te.equalsIgnoreCase("TEB")) {
                this.plan.setTEA(Math.pow(1 + vte, 6) - 1);
            } else if (te.equalsIgnoreCase("TEM")) {
                this.plan.setTEA(Math.pow(1 + vte, 12) - 1);
            } else if (te.equalsIgnoreCase("TEQ")) {
                this.plan.setTEA(Math.pow(1 + vte, 24) - 1);
            } else if (te.equalsIgnoreCase("TED")) {
                this.plan.setTEA(Math.pow(1 + vte, 360) - 1);
            } else {
                this.plan.setTEA(vte);
            }

        } else{
            double vtn = 0.0;

            while (true) {
                System.out.print("Ingrese el valor de la tasa nominal dividida entre 100: ");
                vtn = scanner.nextDouble(); // Valor de la tasa nominal

                try {
                    if (vtn < 0) {
                        throw new IllegalArgumentException();
                    }
                    break;
                } catch (IllegalArgumentException e) {
                    System.out.println("\nError: El valor de la tasa nominal debe ser un número mayor o igual a cero con o sin decimales.\n");
                }
            }

            String tn;

            while (true) {
                System.out.print("Ingrese el tipo de Tasa Nominal:\n"
                        + "Tasa Nominal Anual (TNA)\n"
                        + "Tasa Nominal Semestral (TNS)\n"
                        + "Tasa Nominal Cuatrimestral (TNC)\n"
                        + "Tasa Nominal Trimestral (TNT)\n"
                        + "Tasa Nominal Bimestral (TNB)\n"
                        + "Tasa Nominal Mensual (TNM)\n"
                        + "Tasa Nominal Quincenal (TNQ)\n"
                        + "Tasa Nominal Diaria (TND)\n"
                        + "Tipo de Tasa Nominal: ");
                tn = scanner.next();

                if (tn.equalsIgnoreCase("TNA") || tn.equalsIgnoreCase("TNS") || tn.equalsIgnoreCase("TNC")
                        || tn.equalsIgnoreCase("TNT") || tn.equalsIgnoreCase("TNB") || tn.equalsIgnoreCase("TNM")
                        || tn.equalsIgnoreCase("TNQ") || tn.equalsIgnoreCase("TND")) {
                    break;
                } else {
                    System.out.println("\nIngrese correctamente el tipo de Tasa Nominal:\n"
                            + "Tasa Nominal Anual (TNA)\n"
                            + "Tasa Nominal Semestral (TNS)\n"
                            + "Tasa Nominal Cuatrimestral (TNC)\n"
                            + "Tasa Nominal Trimestral (TNT)\n"
                            + "Tasa Nominal Bimestral (TNB)\n"
                            + "Tasa Nominal Mensual (TNM)\n"
                            + "Tasa Nominal Quincenal (TNQ)\n"
                            + "Tasa Nominal Diaria (TND)\n"
                            + "Tipo de Tasa Nominal: ");
                }
            }

            int cap = 0;

            while (true) {
                System.out.print("Ingrese la frecuencia de la capitalización en días: ");
                cap = scanner.nextInt(); // Frecuencia de capitalización en días

                try {
                    if (cap < 0) {
                        throw new IllegalArgumentException();
                    }
                    break;
                } catch (IllegalArgumentException e) {
                    System.out.println("\nError: La frecuencia de capitalización de la tasa nominal debe ser un número entero mayor que 0.\n");
                }
            }

            double tna = 0.0;
            int m = 360 / cap; // Número de periodos de capitalización

            if (tn.toUpperCase().equals("TNS")) {
                tna = vtn * 2; // Tasa nominal anual
            } else if (tn.toUpperCase().equals("TNC")) {
                tna = vtn * 3; // Tasa nominal anual
            } else if (tn.toUpperCase().equals("TNT")) {
                tna = vtn * 4; // Tasa nominal anual
            } else if (tn.toUpperCase().equals("TNB")) {
                tna = vtn * 6; // Tasa nominal anual
            } else if (tn.toUpperCase().equals("TNM")) {
                tna = vtn * 12; // Tasa nominal anual
            } else if (tn.toUpperCase().equals("TNQ")) {
                tna = vtn * 24; // Tasa nominal anual
            } else if (tn.toUpperCase().equals("TND")) {
                tna = vtn * 360; // Tasa nominal anual
            } else {
                tna = vtn * 1; // Tasa nominal anual
            }

            this.plan.setTEA(Math.pow(1 + tna / m, m) - 1);
        }

        // Ingresar y validar Precio de venta PV
        while (true) {
            System.out.print("Ingrese el precio de venta del bien: ");
            String pvInput = scanner.nextLine();
            try {
                double pv = Double.parseDouble(pvInput);
                if (pv < 1) {
                    throw new IllegalArgumentException();
                }
                this.plan.setPV(pv);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: El precio de venta debe ser un número con decimales mayor que 0.\n");
            }
        }

        // Ingresar y validar Porcentaje de cuota inicial pCI
        while (true) {
            System.out.print("Ingrese el porcentaje de la cuota inicial dividido entre 100: ");
            String pciInput = scanner.nextLine();
            try {
                double pci = Double.parseDouble(pciInput);
                if (pci < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setPCI(pci);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: El porcentaje de la cuota inicial debe ser un número con o sin decimales mayor o igual que 0.\n");
            }
        }

        // Ingresar y validar Numero de anios NA
        while (true) {
            System.out.print("Ingrese el numero de anios durante los que pagara: ");
            String naInput = scanner.nextLine();
            try {
                int na = Integer.parseInt(naInput);
                if (na < 1) {
                    throw new IllegalArgumentException();
                }
                this.plan.setNA(na);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: El número de años debe ser un número entero mayor que 0.\n");
            }
        }

        // Ingresar y validar el tipo de periodo de gracia
        System.out.print("Ingrese el tipo de periodo de gracia (Total 'T'/Parcial 'P'/No considera periodo de gracia 'N'): ");
        String pgInput = scanner.nextLine();

        while (!pgInput.equalsIgnoreCase("T") && !pgInput.equalsIgnoreCase("P") && !pgInput.equalsIgnoreCase("N")) {
            System.out.print("Ingrese correctamente el tipo de periodo de gracia (Total 'T'/Parcial 'P'/No considera periodo de gracia 'N'): ");
            pgInput = scanner.nextLine();
        }

        this.plan.setPG(pgInput.toUpperCase());

        // Ingresar y validar la cantidad de meses que dura el periodo de gracia
        this.plan.setNPG(0);

        if (!this.plan.getPG().equals("N")) {
            while (true) {
                System.out.print("Ingrese en numeros enteros la cantidad de periodos del periodo de gracia: ");
                String npgInput = scanner.nextLine();
                try {
                    int npg = Integer.parseInt(npgInput);
                    if (npg < 1) {
                        throw new IllegalArgumentException();
                    }
                    this.plan.setNPG(npg);
                    break;
                } catch (IllegalArgumentException e) {
                    System.out.println("\nError: La cantidad de periodos del periodo de gracia debe ser un número entero mayor que 0.\n");
                }
            }
        }
        
        //Ingresar y validar tasa del seguro de desgravamen
        while (true) {
            System.out.print("Ingrese la tasa del seguro de desgravamen dividido entre 100: ");
            String tsdInput = scanner.nextLine();
            try {
                double tsd = Double.parseDouble(tsdInput);
                if (tsd < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setTSD(tsd);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: La tasa del seguro de desgravamen debe ser un número mayor o igual a cero.\n");
            }
        }

        //Ingresar y validar tasa del seguro contra todo riesgo
        while (true) {
            System.out.print("Ingrese la tasa del seguro contra todo riesgo dividido entre 100: ");
            String tsrInput = scanner.nextLine();
            try {
                double tsr = Double.parseDouble(tsrInput);
                if (tsr < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setTSR(tsr);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: La tasa del seguro contra todo riesgo debe ser un número mayor o igual a cero.\n");
            }
        }

        //Ingresar y validar gastos administrativos
        while (true) {
            System.out.print("Ingrese los gastos administrativos: ");
            String gaInput = scanner.nextLine();
            try {
                double ga = Double.parseDouble(gaInput);
                if (ga < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setGA(ga);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: Los gastos administrativos deben ser un número mayor o igual a cero.\n");
            }
        }

        //Ingresar y validar portes
        while (true) {
            System.out.print("Ingrese los portes: ");
            String pInput = scanner.nextLine();
            try {
                double p = Double.parseDouble(pInput);
                if (p < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setP(p);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: Los portes deben ser un número mayor o igual a cero.\n");
            }
        }

        //Ingresar y validar comisiones periodicas
        while (true) {
            System.out.print("Ingrese la comision periodica: ");
            String cpInput = scanner.nextLine();
            try {
                double cp = Double.parseDouble(cpInput);
                if (cp < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setCP(cp);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: La comisión periódica debe ser un número mayor o igual a cero.\n");
            }
        }

        //Ingresar y validar costos notariales
        while (true) {
            System.out.print("Ingrese los costos notariales: ");
            String cnInput = scanner.nextLine();
            try {
                double cn = Double.parseDouble(cnInput);
                if (cn < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setCN(cn);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: Los costos notariales deben ser un número mayor o igual a cero.\n");
            }
        }

        //Ingresar y validar costos registrales
        while (true) {
            System.out.print("Ingrese los costos registrales: ");
            String crInput = scanner.nextLine();
            try {
                double cr = Double.parseDouble(crInput);
                if (cr < 0) {
                    throw new IllegalArgumentException();
                }
                this.plan.setCR(cr);
                break;
            } catch (IllegalArgumentException e) {
                System.out.println("\nError: Los costos registrales deben ser un número mayor o igual a cero.\n");
            }
        }
        scanner.close();

        //------------------A PARTIR DE AQUI SE PROCESAN LOS DATOS INTERMEDIOS------------------

        // Calcular cuota inicial (en número, ya no en porcentaje) CI
        this.plan.setCI(this.plan.getPCI() * this.plan.getPV());

        // Calcular préstamo C
        this.plan.setC(this.plan.getPV() - this.plan.getCI() + this.plan.getCN() + this.plan.getCR()); // Los costos notariales y registrales se adjudican al monto del préstamo
        this.plan.setAUX3(this.plan.getC());

        // Calcular número total de cuotas
        this.plan.setN(this.plan.getNCxA() * this.plan.getNA());

        // Inicialización del periodo actual
        this.plan.setNC(1);

        // Inicialización del saldo final
        this.plan.setSF(0);

        // Inicialización de la cuota total
        this.plan.setRT(0);

        // Inicialización de la amortización total
        this.plan.setAT(0);

        // Inicialización del número de veces que se ha repetido el plan de pagos
        this.plan.setVueltas(0);

        // Inicialización de la tasa del periodo (la tasa será mensual)
        this.plan.setTEP(Math.pow((1.0 + 1.5181701168189803), (1.0 / 12.0)) - 1.0);

        // Cálculo de la tasa de seguro de desgravamen anual
        this.plan.setTSDA(this.plan.getTSD() * 12);

        // Cálculo de la Tasa de Seguro de Desgravamen Ajustada al Plazo
        this.plan.setTSDP(this.plan.getTSDA() / 360 * 30);

        // Cálculo de la tasa de seguro contra todo riesgo anual
        this.plan.setTSRA(this.plan.getTSR() * 12);

        // Cálculo de la Tasa de Seguro Contra Todo Riesgo Ajustada al Plazo
        this.plan.setTSRP(this.plan.getTSRA() / 360 * 30);

        //------------------A PARTIR DE AQUI SE CALCULA EL PLAN DE PAGOS------------------

        this.PDP();

        System.out.println(this.plan.getVPSF());
        System.out.println(this.plan.getR2());

    }

    public void imprimirInformacion() {
        System.out.println("\nNumero de dias por anio: " + this.plan.getNDxA());
        System.out.println("Precio de venta del bien: " + this.plan.getPV());
        System.out.println("Porcentaje de la cuota inicial: " + String.format("%.7f", this.plan.getPCI() * 100) + "%");
        System.out.println("Frecuencia de pago: " + this.plan.getFrec() + " dias");
        System.out.println("Numero de anios: " + this.plan.getNA());
        System.out.println("Cuota inicial: " + String.format("%.2f", this.plan.getCI()));
        System.out.println("Prestamo: " + String.format("%.2f", this.plan.getC()));
        System.out.println("Numero de cuotas por anio: " + this.plan.getNCxA());
        System.out.println("Numero total de cuotas: " + this.plan.getN());
        System.out.println("Tasa Efectiva Anual: " + String.format("%.7f", this.plan.getTEA() * 100) + "%");
        System.out.println("Tipo de periodo de gracia: " + this.plan.getPG());
        System.out.println("Cantidad de periodos del periodo de gracia: " + this.plan.getNPG());
        System.out.println("Amortizacion total: " + String.format("%.2f", this.plan.getAT()));
        System.out.println("Gastos administrativos: " + this.plan.getGA());
        System.out.println("Portes: " + this.plan.getP());
        System.out.println("Costos notariales: " + this.plan.getCN());
        System.out.println("Costos registrales: " + this.plan.getCR());
        System.out.println("TSD: " + String.format("%.7f", this.plan.getTSD() * 100) + "%");
        System.out.println("Seguro de desgravamen: " + String.format("%.2f", this.plan.getSD()));
        System.out.println("Seguro contra todo riesgo: " + String.format("%.2f", this.plan.getSR()));
    }

}
