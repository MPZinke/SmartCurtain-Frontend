AreaEvent.New.Modal.Inputs.PERCENTAGE_RANGE = document.getElementById("AreaEvent.New.Modal-percentage_range-input");
AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT = document.getElementById("AreaEvent.New.Modal-percentage_input-input");
AreaEvent.New.Modal.Inputs.DATETIME = document.getElementById("AreaEvent.New.Modal-datetime-input");
AreaEvent.New.Modal.toggle_datetime = function toggle_datetime(checkbox) {
    var disable_inputs = checkbox.checked === false;
    AreaEvent.New.Modal.Inputs.DATETIME.disabled = disable_inputs;
};
AreaEvent.New.Modal.update_percentage_range = function update_percentage_range(input) {
    var floor_value = Math.floor(AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber);
    AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = floor_value;
    if (AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber > 100) {
        AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = 100;
    }
    if (AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber < 0) {
        AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = 0;
    }
    AreaEvent.New.Modal.Inputs.PERCENTAGE_RANGE.valueAsNumber = AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber;
};
AreaEvent.New.Modal.update_percentage_input = function update_percentage_input(range) {
    AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = AreaEvent.New.Modal.Inputs.PERCENTAGE_RANGE.valueAsNumber;
};
