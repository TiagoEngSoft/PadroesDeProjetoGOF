package cafe;

public abstract class DecoradorBebida implements Bebida {
    protected Bebida bebida;

    public DecoradorBebida(Bebida bebida) {
        this.bebida = bebida;
    }

    public abstract String getDescricao();
    public abstract double getPreco();
}
