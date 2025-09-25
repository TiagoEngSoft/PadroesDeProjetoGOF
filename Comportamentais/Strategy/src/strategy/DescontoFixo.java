package strategy;

public class DescontoFixo implements DescontoStrategy {
    private double percentual;

    public DescontoFixo(double percentual) {
        this.percentual = percentual;
    }

    @Override
    public double calcular(double precoOriginal) {
        return precoOriginal * (1 - percentual);
    }
}
