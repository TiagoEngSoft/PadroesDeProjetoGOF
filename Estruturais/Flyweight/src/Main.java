public class Main {
    public static void main(String[] args) {
        String[] cores = { "vermelho", "azul", "verde" };

        for (int i = 0; i < 10; i++) {
            String cor = cores[i % cores.length];
            int x = (int) (Math.random() * 100);
            int y = (int) (Math.random() * 100);

            EmojiBalao balao = EmojiFactory.getBalao(cor);
            balao.desenhar(x, y, cor);
        }
    }
}
