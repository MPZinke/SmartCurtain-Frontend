

NewAreaEventModal.Inputs.PERCENTAGE_RANGE = <HTMLInputElement>document.getElementById(${{NewAreaModalPercentageRangeInput}}$);
NewAreaEventModal.Inputs.PERCENTAGE_INPUT = <HTMLInputElement>document.getElementById(${{NewAreaModalPercentageInputInput}}$);
NewAreaEventModal.Inputs.DATETIME = <HTMLInputElement>document.getElementById(${{NewAreaModalDatetimeInput}}$);


NewAreaEventModal.toggle_datetime = function toggle_datetime(checkbox: HTMLInputElement)
/*
SUMMARY: Enable and disables the date and time fields of the modal.
PARAMS:  Takes the item that is toggling the date and time fields.
*/
{
	const disable_inputs = checkbox.checked === false;

	NewAreaEventModal.Inputs.DATETIME.disabled = disable_inputs;
}


NewAreaEventModal.update_percentage_range = function update_percentage_range(input: HTMLInputElement)
{
	const floor_value = Math.floor(NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber);
	NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber = floor_value;

	if(NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber > 100)
	{
		NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber = 100;
	}
	if(NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber < 0)
	{
		NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber = 0;
	}
	NewAreaEventModal.Inputs.PERCENTAGE_RANGE.valueAsNumber = NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber;
}


NewAreaEventModal.update_percentage_input = function update_percentage_input(range: HTMLInputElement)
{
	NewAreaEventModal.Inputs.PERCENTAGE_INPUT.valueAsNumber = NewAreaEventModal.Inputs.PERCENTAGE_RANGE.valueAsNumber;
}
