package app;

import cafe.*;
import adicionais.*;

public class Main {
    public static void main(String[] args) {
        Bebida cafe = new CafeSimples();
        System.out.println(cafe.getDescricao() + " - R$ " + cafe.getPreco());

        Bebida cafeComLeite = new ComLeite(cafe);
        System.out.println(cafeComLeite.getDescricao() + " - R$ " + cafeComLeite.getPreco());

        Bebida cafeComTudo = new ComChocolate(new ComLeite(cafe));
        System.out.println(cafeComTudo.getDescricao() + " - R$ " + cafeComTudo.getPreco());
    }
}
