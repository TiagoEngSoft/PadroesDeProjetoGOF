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
