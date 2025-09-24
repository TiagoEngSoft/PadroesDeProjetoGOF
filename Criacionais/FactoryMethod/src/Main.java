package app;

import criador.CriadorCartao;
import criador.CriadorCartaoAniversario;
import criador.CriadorCartaoNatal;

public class Main {
    public static void main(String[] args) {
        CriadorCartao criador1 = new CriadorCartaoAniversario();
        CriadorCartao criador2 = new CriadorCartaoNatal();

        criador1.enviarCartao(); // Saída: Feliz Aniversário!
        criador2.enviarCartao(); // Saída: Feliz Natal!
    }
}
