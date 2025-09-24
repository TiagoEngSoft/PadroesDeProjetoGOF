import os

# Dicionário com os arquivos Java
arquivos_command = {
    "comandos/Comando.java": '''\
package comandos;

public interface Comando {
    void executar();
}
''',

    "comandos/LigarLuz.java": '''\
package comandos;

import dispositivos.Luz;

public class LigarLuz implements Comando {
    private Luz luz;

    public LigarLuz(Luz luz) {
        this.luz = luz;
    }

    public void executar() {
        luz.ligar();
    }
}
''',

    "comandos/DesligarLuz.java": '''\
package comandos;

import dispositivos.Luz;

public class DesligarLuz implements Comando {
    private Luz luz;

    public DesligarLuz(Luz luz) {
        this.luz = luz;
    }

    public void executar() {
        luz.desligar();
    }
}
''',

    "comandos/LigarTV.java": '''\
package comandos;

import dispositivos.TV;

public class LigarTV implements Comando {
    private TV tv;

    public LigarTV(TV tv) {
        this.tv = tv;
    }

    public void executar() {
        tv.ligar();
    }
}
''',

    "comandos/DesligarTV.java": '''\
package comandos;

import dispositivos.TV;

public class DesligarTV implements Comando {
    private TV tv;

    public DesligarTV(TV tv) {
        this.tv = tv;
    }

    public void executar() {
        tv.desligar();
    }
}
''',

    "dispositivos/Luz.java": '''\
package dispositivos;

public class Luz {
    public void ligar() {
        System.out.println("💡 Luz ligada");
    }

    public void desligar() {
        System.out.println("💡 Luz desligada");
    }
}
''',

    "dispositivos/TV.java": '''\
package dispositivos;

public class TV {
    public void ligar() {
        System.out.println("📺 TV ligada");
    }

    public void desligar() {
        System.out.println("📺 TV desligada");
    }
}
''',

    "ControleRemoto.java": '''\
import comandos.Comando;

public class ControleRemoto {
    private Comando comando;

    public void setComando(Comando comando) {
        this.comando = comando;
    }

    public void pressionarBotao() {
        comando.executar();
    }
}
''',

    "Main.java": '''\
import comandos.*;
import dispositivos.*;

public class Main {
    public static void main(String[] args) {
        ControleRemoto controle = new ControleRemoto();

        Luz luz = new Luz();
        TV tv = new TV();

        Comando ligarLuz = new LigarLuz(luz);
        Comando desligarLuz = new DesligarLuz(luz);
        Comando ligarTV = new LigarTV(tv);
        Comando desligarTV = new DesligarTV(tv);

        System.out.println("▶️ Ligando a luz:");
        controle.setComando(ligarLuz);
        controle.pressionarBotao();

        System.out.println("\\n⏹️ Desligando a luz:");
        controle.setComando(desligarLuz);
        controle.pressionarBotao();

        System.out.println("\\n▶️ Ligando a TV:");
        controle.setComando(ligarTV);
        controle.pressionarBotao();

        System.out.println("\\n⏹️ Desligando a TV:");
        controle.setComando(desligarTV);
        controle.pressionarBotao();
    }
}
'''
}

def criar_projeto_command(path_base):
    nome_projeto = "CommandControleRemoto"
    caminho_projeto = os.path.join(path_base, nome_projeto)
    caminho_src = os.path.join(caminho_projeto, "src")
    caminho_comandos = os.path.join(caminho_src, "comandos")
    caminho_dispositivos = os.path.join(caminho_src, "dispositivos")

    os.makedirs(caminho_comandos, exist_ok=True)
    os.makedirs(caminho_dispositivos, exist_ok=True)

    for nome_arquivo, conteudo in arquivos_command.items():
        caminho_relativo = os.path.join(caminho_src, nome_arquivo.replace("/", os.sep))
        os.makedirs(os.path.dirname(caminho_relativo), exist_ok=True)
        with open(caminho_relativo, 'w', encoding='utf-8') as f:
            f.write(conteudo)

    print(f"\n✅ Projeto gerado em: {caminho_projeto}")
    print("📂 Estrutura criada:")
    print(f"{nome_projeto}/")
    print("└── src/")
    print("    ├── Main.java")
    print("    ├── ControleRemoto.java")
    print("    ├── comandos/")
    for arq in arquivos_command:
        if arq.startswith("comandos/"):
            print(f"    │   └── {arq.split('/')[-1]}")
    print("    └── dispositivos/")
    for arq in arquivos_command:
        if arq.startswith("dispositivos/"):
            print(f"        └── {arq.split('/')[-1]}")

if __name__ == "__main__":
    print("=== Gerador de Projeto Java - Padrão Command (Controle Remoto) ===")
    caminho = input("📁 Digite o caminho onde deseja criar o projeto: ").strip('"')

    if not os.path.exists(caminho):
        print("❌ Caminho não existe.")
    else:
        criar_projeto_command(caminho)

    input("\nPressione ENTER para sair...")
