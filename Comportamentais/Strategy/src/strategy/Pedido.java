package strategy;

public class Pedido {
    private double precoOriginal;
    private DescontoStrategy estrategia;

    public Pedido(double precoOriginal, DescontoStrategy estrategia) {
        this.precoOriginal = precoOriginal;
        this.estrategia = estrategia;
    }

    public double getPrecoFinal() {
        return estrategia.calcular(precoOriginal);
    }

    public void setEstrategia(DescontoStrategy novaEstrategia) {
        this.estrategia = novaEstrategia;
    }
}
