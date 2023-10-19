

AreaEvent.New.Modal.Inputs.PERCENTAGE_RANGE = <HTMLInputElement>document.getElementById("AreaEvent.New.Modal-percentage_range-input");
AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT = <HTMLInputElement>document.getElementById("AreaEvent.New.Modal-percentage_input-input");
AreaEvent.New.Modal.Inputs.DATETIME = <HTMLInputElement>document.getElementById("AreaEvent.New.Modal-datetime-input");


AreaEvent.New.Modal.toggle_datetime = function toggle_datetime(checkbox: HTMLInputElement)
/*
SUMMARY: Enable and disables the date and time fields of the modal.
PARAMS:  Takes the item that is toggling the date and time fields.
*/
{
	const disable_inputs = checkbox.checked === false;

	AreaEvent.New.Modal.Inputs.DATETIME.disabled = disable_inputs;
}


AreaEvent.New.Modal.update_percentage_range = function update_percentage_range(input: HTMLInputElement)
{
	const floor_value = Math.floor(AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber);
	AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = floor_value;

	if(AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber > 100)
	{
		AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = 100;
	}
	if(AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber < 0)
	{
		AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = 0;
	}
	AreaEvent.New.Modal.Inputs.PERCENTAGE_RANGE.valueAsNumber = AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber;
}


AreaEvent.New.Modal.update_percentage_input = function update_percentage_input(range: HTMLInputElement)
{
	AreaEvent.New.Modal.Inputs.PERCENTAGE_INPUT.valueAsNumber = AreaEvent.New.Modal.Inputs.PERCENTAGE_RANGE.valueAsNumber;
}
