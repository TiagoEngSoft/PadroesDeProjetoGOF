package components;

import mediator.Mediator;

public class Button implements Component {
    private Mediator mediator;
    private boolean enabled = false;

    public void setEnabled(boolean enabled) {
        this.enabled = enabled;
        System.out.println("Botão agora está " + (enabled ? "ATIVADO" : "DESATIVADO"));
    }

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public String getName() {
        return "Button";
    }
}
