package app;

import composite.Componente;
import composite.Arquivo;
import composite.Pasta;

public class Main {
    public static void main(String[] args) {
        // Cria arquivos
        Componente arquivo1 = new Arquivo("arquivo1.txt");
        Componente arquivo2 = new Arquivo("arquivo2.txt");
        Componente arquivo3 = new Arquivo("foto.png");

        // Cria pastas
        Pasta pastaDocumentos = new Pasta("Documentos");
        Pasta pastaImagens = new Pasta("Imagens");
        Pasta pastaRaiz = new Pasta("Raiz");

        // Monta a estrutura
        pastaDocumentos.adicionar(arquivo1);
        pastaDocumentos.adicionar(arquivo2);

        pastaImagens.adicionar(arquivo3);

        pastaRaiz.adicionar(pastaDocumentos);
        pastaRaiz.adicionar(pastaImagens);

        // Mostra a estrutura
        pastaRaiz.mostrar(0);
    }
}
