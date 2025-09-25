package editor;

// Memento: Armazena um snapshot do estado do Editor
public class EditorMemento {
    private final String textoSalvo;

    public EditorMemento(String texto) {
        this.textoSalvo = texto;
    }

    public String getTextoSalvo() {
        return textoSalvo;
    }
}
