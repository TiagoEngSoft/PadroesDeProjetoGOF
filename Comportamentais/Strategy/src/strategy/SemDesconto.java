package strategy;

public class SemDesconto implements DescontoStrategy {
    @Override
    public double calcular(double precoOriginal) {
        return precoOriginal; // Sem desconto
    }
}
