import os

# Conteúdo dos arquivos Java

editor_java = '''\
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
'''

editor_memento_java = '''\
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
'''

history_java = '''\
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
'''

main_java = '''\
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
'''

# Mapeamento de arquivos
arquivos = {
    'editor/Editor.java': editor_java,
    'editor/EditorMemento.java': editor_memento_java,
    'editor/History.java': history_java,
    'Main.java': main_java,
}


def criar_projeto(path_base):
    print(f"\n🔧 Criando projeto Memento em: {path_base}\n")

    for caminho_relativo, conteudo in arquivos.items():
        caminho_completo = os.path.join(path_base, caminho_relativo)
        pasta = os.path.dirname(caminho_completo)

        os.makedirs(pasta, exist_ok=True)
        with open(caminho_completo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

        print(f"✅ Criado: {caminho_relativo}")

    print("\n📦 Projeto Memento Java criado com sucesso!")
    print(f"\n📁 Local: {os.path.abspath(path_base)}")
    print("\nPressione ENTER para sair...")
    input()


# Execução
if __name__ == "__main__":
    print("🛠️  Criador de Projeto Java - Padrão Memento\n")
    path = input("📂 Digite o caminho onde o projeto deve ser salvo: ").strip()

    if not path:
        print("❌ Caminho inválido. Encerrando.")
    else:
        criar_projeto(path)
