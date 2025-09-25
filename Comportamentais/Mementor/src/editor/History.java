package editor;

import java.util.Stack;

// Caretaker: guarda os Mementos
public class History {
    private Stack<EditorMemento> historico = new Stack<>();

    public void salvarEstado(EditorMemento memento) {
        historico.push(memento);
    }

    public EditorMemento desfazer() {
        if (!historico.isEmpty()) {
            return historico.pop();
        }
        return null;
    }

    public boolean temHistorico() {
        return !historico.isEmpty();
    }
}
