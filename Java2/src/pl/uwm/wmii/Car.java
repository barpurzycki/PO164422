package pl.uwm.wmii;

class Car {
    public Car(double pojemnoscSilnika)
    {
        this.pojemnoscSilnika = pojemnoscSilnika;
    }

    public Car()
    {
        this.pojemnoscSilnika = 4.2;
    }
    public double getPojemnoscSilnika()
    {
        return this.pojemnoscSilnika;
    }
    public void setPojemnoscSilnika(double value)
    {
        this.pojemnoscSilnika = value;
    }
    private double pojemnoscSilnika;
    private String marka;
}
