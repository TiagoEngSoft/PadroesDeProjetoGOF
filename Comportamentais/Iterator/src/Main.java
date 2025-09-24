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
