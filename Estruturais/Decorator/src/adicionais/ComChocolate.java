package adicionais;

import cafe.Bebida;
import cafe.DecoradorBebida;

public class ComChocolate extends DecoradorBebida {
    public ComChocolate(Bebida bebida) {
        super(bebida);
    }

    public String getDescricao() {
        return bebida.getDescricao() + ", com chocolate";
    }

    public double getPreco() {
        return bebida.getPreco() + 1.50;
    }
}
