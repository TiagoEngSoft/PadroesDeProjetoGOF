package components;

import mediator.Mediator;

public class CheckBox implements Component {
    private Mediator mediator;
    private boolean checked = false;

    public void setChecked(boolean checked) {
        this.checked = checked;
        mediator.notify(this, "checkChanged");
    }

    public boolean isChecked() {
        return checked;
    }

    @Override
    public void setMediator(Mediator mediator) {
        this.mediator = mediator;
    }

    @Override
    public String getName() {
        return "CheckBox";
    }
}
