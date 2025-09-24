package app;

import singleton.Configuracao;

public class Main {
    public static void main(String[] args) {
        Configuracao conf1 = Configuracao.getInstancia();
        System.out.println("Configuração Inicial: " + conf1);

        // Alterar configuração
        conf1.setAmbiente("DESENVOLVIMENTO");
        conf1.setVersao("1.1.0");

        Configuracao conf2 = Configuracao.getInstancia();
        System.out.println("Configuração Acessada Novamente: " + conf2);

        if (conf1 == conf2) {
            System.out.println("✅ Mesma instância compartilhada (Singleton)");
        } else {
            System.out.println("❌ Instâncias diferentes (Erro)");
        }
    }
}
