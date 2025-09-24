package singleton;

public class Configuracao {
    private static Configuracao instancia;

    private String ambiente;
    private String versao;

    private Configuracao() {
        // Configurações padrão
        this.ambiente = "PRODUCAO";
        this.versao = "1.0.0";
    }

    public static Configuracao getInstancia() {
        if (instancia == null) {
            instancia = new Configuracao();
        }
        return instancia;
    }

    public String getAmbiente() {
        return ambiente;
    }

    public void setAmbiente(String ambiente) {
        this.ambiente = ambiente;
    }

    public String getVersao() {
        return versao;
    }

    public void setVersao(String versao) {
        this.versao = versao;
    }

    @Override
    public String toString() {
        return "[Ambiente: " + ambiente + ", Versão: " + versao + "]";
    }
}
