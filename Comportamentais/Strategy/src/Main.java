import strategy.*;

public class Main {
    public static void main(String[] args) {
        Pedido pedido = new Pedido(100.0, new SemDesconto());

        System.out.println("🧾 Preço original: R$100.00");
        System.out.println("🔸 Sem desconto: R$" + pedido.getPrecoFinal());

        pedido.setEstrategia(new DescontoFixo(0.1));
        System.out.println("🔸 Desconto de 10%: R$" + pedido.getPrecoFinal());

        pedido.setEstrategia(new DescontoFixo(0.25));
        System.out.println("🔸 Desconto de 25%: R$" + pedido.getPrecoFinal());
    }
}
