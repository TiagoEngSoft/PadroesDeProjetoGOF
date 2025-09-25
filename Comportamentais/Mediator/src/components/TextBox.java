package components;

import mediator.Mediator;

public class TextBox implements Component {
    private Mediator mediator;
    private String text = "";

    public void setText(String text) {
        this.text = text;
        mediator.notify(this, "textChanged");
    }

    public String getText() {
        return text;
    }

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public String getName() {
        return "TextBox";
    }
}
