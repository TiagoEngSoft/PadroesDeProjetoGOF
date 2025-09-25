import visitor.*;

public class Main {
    public static void main(String[] args) {
        Elemento[] elementos = {
            new Pessoa("Alice", 30),
            new Empresa("OpenAI", 500)
        };

        Visitor visitor = new ImpressaoVisitor();

        for (Elemento e : elementos) {
            e.aceitar(visitor);
        }
    }
}
