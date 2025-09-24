import os

# Conteúdo dos arquivos Java organizados
files_content = {
    "iterator/MeuIterator.java": """
package iterator;

public interface MeuIterator<T> {
    boolean hasNext();
    T next();
}
""",

    "iterator/MinhaPlaylist.java": """
package iterator;

public interface MinhaPlaylist<T> {
    MeuIterator<T> criarIterator();
}
""",

    "model/Musica.java": """
package model;

public class Musica {
    private String titulo;

    public Musica(String titulo) {
        this.titulo = titulo;
    }

    public String getTitulo() {
        return titulo;
    }
}
""",

    "model/Playlist.java": """
package model;

import iterator.MeuIterator;
import iterator.MinhaPlaylist;

public class Playlist implements MinhaPlaylist<Musica> {
    private Musica[] musicas;
    private int cont = 0;

    public Playlist(int tamanho) {
        musicas = new Musica[tamanho];
    }

    public void adicionarMusica(Musica musica) {
        if (cont < musicas.length) {
            musicas[cont++] = musica;
        }
    }

    public MeuIterator<Musica> criarIterator() {
        return new PlaylistIterator();
    }

    private class PlaylistIterator implements MeuIterator<Musica> {
        private int posicaoAtual = 0;

        public boolean hasNext() {
            return posicaoAtual < cont && musicas[posicaoAtual] != null;
        }

        public Musica next() {
            return musicas[posicaoAtual++];
        }
    }
}
""",

    "Main.java": """
import model.Musica;
import model.Playlist;
import iterator.MeuIterator;

public class Main {
    public static void main(String[] args) {
        Playlist playlist = new Playlist(5);
        playlist.adicionarMusica(new Musica("Bohemian Rhapsody"));
        playlist.adicionarMusica(new Musica("Imagine"));
        playlist.adicionarMusica(new Musica("Hotel California"));

        MeuIterator<Musica> iterator = playlist.criarIterator();

        System.out.println("🎵 Músicas na playlist:");
        while (iterator.hasNext()) {
            Musica musica = iterator.next();
            System.out.println("- " + musica.getTitulo());
        }
    }
}
"""
}


def main():
    print("Gerador de projeto Java - Padrão Iterator com estrutura em pacotes\n")
    base_path = input("Digite o caminho completo onde deseja gerar o projeto: ").strip()

    src_path = os.path.join(base_path, "IteratorPlaylist", "src")
    os.makedirs(src_path, exist_ok=True)

    # Criar as subpastas
    folders = ["iterator", "model"]
    for folder in folders:
        os.makedirs(os.path.join(src_path, folder), exist_ok=True)

    # Criar os arquivos nas pastas correspondentes
    for filepath, content in files_content.items():
        full_path = os.path.join(src_path, filepath)
        with open(full_path, "w", encoding="utf-8") as f:
            f.write(content.strip() + "\n")

    # Mostrar resumo
    print("\nProjeto criado em:\n  " + src_path)
    print("\nArquivos criados:")
    for filepath in files_content.keys():
        print(f" - {filepath}")

    input("\nPressione ENTER para fechar.")


if __name__ == "__main__":
    main()
