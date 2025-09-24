import os

estrutura = {
    "src/cafe": {
        "Bebida.java": """\
package cafe;

public interface Bebida {
    String getDescricao();
    double getPreco();
}
""",

        "CafeSimples.java": """\
package cafe;

public class CafeSimples implements Bebida {
    public String getDescricao() {
        return "Café simples";
    }

    public double getPreco() {
        return 3.00;
    }
}
""",

        "DecoradorBebida.java": """\
package cafe;

public abstract class DecoradorBebida implements Bebida {
    protected Bebida bebida;

    public DecoradorBebida(Bebida bebida) {
        this.bebida = bebida;
    }

    public abstract String getDescricao();
    public abstract double getPreco();
}
"""
    },

    "src/adicionais": {
        "ComLeite.java": """\
package adicionais;

import cafe.Bebida;
import cafe.DecoradorBebida;

public class ComLeite extends DecoradorBebida {
    public ComLeite(Bebida bebida) {
        super(bebida);
    }

    public String getDescricao() {
        return bebida.getDescricao() + ", com leite";
    }

    public double getPreco() {
        return bebida.getPreco() + 1.00;
    }
}
""",

        "ComChocolate.java": """\
package adicionais;

import cafe.Bebida;
import cafe.DecoradorBebida;

public class ComChocolate extends DecoradorBebida {
    public ComChocolate(Bebida bebida) {
        super(bebida);
    }

    public String getDescricao() {
        return bebida.getDescricao() + ", com chocolate";
    }

    public double getPreco() {
        return bebida.getPreco() + 1.50;
    }
}
"""
    },

    "src/app": {
        "Main.java": """\
package app;

import cafe.*;
import adicionais.*;

public class Main {
    public static void main(String[] args) {
        Bebida cafe = new CafeSimples();
        System.out.println(cafe.getDescricao() + " - R$ " + cafe.getPreco());

        Bebida cafeComLeite = new ComLeite(cafe);
        System.out.println(cafeComLeite.getDescricao() + " - R$ " + cafeComLeite.getPreco());

        Bebida cafeComTudo = new ComChocolate(new ComLeite(cafe));
        System.out.println(cafeComTudo.getDescricao() + " - R$ " + cafeComTudo.getPreco());
    }
}
"""
    }
}


def main():
    print("== Gerador de Projeto Java (Padrão Decorator) ==")
    caminho = input("Informe o path onde deseja criar o projeto (ex: C:\\Projetos\\DecoratorProject): ").strip()

    try:
        print("\n🔧 Criando estrutura de diretórios e arquivos...\n")

        for pasta_relativa, arquivos in estrutura.items():
            pasta_completa = os.path.join(caminho, pasta_relativa)
            os.makedirs(pasta_completa, exist_ok=True)

            for nome_arquivo, conteudo in arquivos.items():
                caminho_arquivo = os.path.join(pasta_completa, nome_arquivo)
                with open(caminho_arquivo, "w", encoding="utf-8") as f:
                    f.write(conteudo)

        print("✅ Projeto Decorator gerado com sucesso!")
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
