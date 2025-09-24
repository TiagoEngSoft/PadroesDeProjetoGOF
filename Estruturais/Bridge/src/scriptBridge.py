import os

# Estrutura do projeto
estrutura = {
    "src/dispositivos": {
        "Dispositivo.java": """\
package dispositivos;

public interface Dispositivo {
    void ligar();
    void desligar();
    boolean isLigado();
}
""",
        "TV.java": """\
package dispositivos;

public class TV implements Dispositivo {
    private boolean ligado = false;

    public void ligar() {
        ligado = true;
        System.out.println("TV ligada.");
    }

    public void desligar() {
        ligado = false;
        System.out.println("TV desligada.");
    }

    public boolean isLigado() {
        return ligado;
    }
}
""",
        "Radio.java": """\
package dispositivos;

public class Radio implements Dispositivo {
    private boolean ligado = false;

    public void ligar() {
        ligado = true;
        System.out.println("Rádio ligado.");
    }

    public void desligar() {
        ligado = false;
        System.out.println("Rádio desligado.");
    }

    public boolean isLigado() {
        return ligado;
    }
}
"""
    },
    "src/controles": {
        "ControleRemoto.java": """\
package controles;

import dispositivos.Dispositivo;

public abstract class ControleRemoto {
    protected Dispositivo dispositivo;

    public ControleRemoto(Dispositivo dispositivo) {
        this.dispositivo = dispositivo;
    }

    public abstract void ligar();
    public abstract void desligar();
}
""",
        "ControleSimples.java": """\
package controles;

import dispositivos.Dispositivo;

public class ControleSimples extends ControleRemoto {
    public ControleSimples(Dispositivo dispositivo) {
        super(dispositivo);
    }

    public void ligar() {
        dispositivo.ligar();
    }

    public void desligar() {
        dispositivo.desligar();
    }
}
""",
        "ControleAvancado.java": """\
package controles;

import dispositivos.Dispositivo;

public class ControleAvancado extends ControleRemoto {
    public ControleAvancado(Dispositivo dispositivo) {
        super(dispositivo);
    }

    public void ligar() {
        dispositivo.ligar();
        System.out.println("Controle avançado: dispositivo ligado com recursos extras.");
    }

    public void desligar() {
        dispositivo.desligar();
        System.out.println("Controle avançado: dispositivo desligado com recursos extras.");
    }

    public void alternar() {
        if (dispositivo.isLigado()) {
            desligar();
        } else {
            ligar();
        }
    }
}
"""
    },
    "src/app": {
        "Main.java": """\
package app;

import dispositivos.*;
import controles.*;

public class Main {
    public static void main(String[] args) {
        Dispositivo tv = new TV();
        Dispositivo radio = new Radio();

        ControleRemoto controleTV = new ControleSimples(tv);
        ControleRemoto controleRadio = new ControleAvancado(radio);

        System.out.println("--- Controle Simples com TV ---");
        controleTV.ligar();
        controleTV.desligar();

        System.out.println("\\n--- Controle Avançado com Rádio ---");
        controleRadio.ligar();
        controleRadio.desligar();

        System.out.println("\\n--- Usando alternar no controle avançado ---");
        ControleAvancado controleAvancadoRadio = new ControleAvancado(radio);
        controleAvancadoRadio.alternar();
        controleAvancadoRadio.alternar();
    }
}
"""
    }
}

def main():
    print("== Gerador de Projeto Java (Bridge Pattern) ==")
    caminho = input("Informe o path onde deseja criar o projeto (ex: C:\\Projetos\\BridgeProject): ").strip()

    try:
        print("\n🔧 Criando estrutura de diretórios e arquivos...\n")

        for pasta_relativa, arquivos in estrutura.items():
            pasta_completa = os.path.join(caminho, pasta_relativa)
            os.makedirs(pasta_completa, exist_ok=True)

            for nome_arquivo, conteudo in arquivos.items():
                caminho_arquivo = os.path.join(pasta_completa, nome_arquivo)
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    f.write(conteudo)

        print("✅ Projeto Bridge gerado com sucesso!")
        print(f"\n📁 Local do projeto: {caminho}\\src")
        print("📄 Arquivos criados:")
        for pasta, arquivos in estrutura.items():
            for nome in arquivos:
                print(f" - {pasta}/{nome}")

    except Exception as e:
        print(f"\n❌ Erro ao gerar o projeto: {e}")

    input("\nPressione Enter para encerrar...")

if __name__ == "__main__":
    main()
