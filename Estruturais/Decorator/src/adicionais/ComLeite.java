package adicionais;

import cafe.Bebida;
import cafe.DecoradorBebida;

public class ComLeite extends DecoradorBebida {
    public ComLeite(Bebida bebida) {
        super(bebida);
    }

    public String getDescricao() {
        return bebida.getDescricao() + ", com leite";
    }

    public double getPreco() {
        return bebida.getPreco() + 1.00;
    }
}
