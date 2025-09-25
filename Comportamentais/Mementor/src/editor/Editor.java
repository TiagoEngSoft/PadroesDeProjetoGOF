package editor;

public class Editor {
    private String texto = "";

    public void escrever(String novoTexto) {
        texto += novoTexto;
        System.out.println("Texto atual: " + texto);
    }

    public EditorMemento salvar() {
        System.out.println("🔖 Salvando estado...");
        return new EditorMemento(texto);
    }

    public void restaurar(EditorMemento memento) {
        texto = memento.getTextoSalvo();
        System.out.println("↩️ Texto restaurado: " + texto);
    }

    public String getTexto() {
        return texto;
    }
}
