package composite;

import java.util.ArrayList;
import java.util.List;

public class Pasta implements Componente {
    private String nome;
    private List<Componente> filhos = new ArrayList<>();

    public Pasta(String nome) {
        this.nome = nome;
    }

    public void adicionar(Componente c) {
        filhos.add(c);
    }

    public void remover(Componente c) {
        filhos.remove(c);
    }

    @Override
    public void mostrar(int nivel) {
        System.out.println("  ".repeat(nivel) + "+ " + nome);
        for (Componente filho : filhos) {
            filho.mostrar(nivel + 1);
        }
    }
}
