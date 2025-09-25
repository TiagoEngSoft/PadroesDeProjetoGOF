import editor.Editor;
import editor.History;

public class Main {
    public static void main(String[] args) {
        Editor editor = new Editor();
        History history = new History();

        // Escreve algo
        editor.escrever("Olá, ");
        history.salvarEstado(editor.salvar());

        editor.escrever("mundo!");
        history.salvarEstado(editor.salvar());

        editor.escrever(" Isso será desfeito...");

        // Desfaz 2 vezes
        if (history.temHistorico()) {
            editor.restaurar(history.desfazer());
        }

        if (history.temHistorico()) {
            editor.restaurar(history.desfazer());
        }
    }
}
