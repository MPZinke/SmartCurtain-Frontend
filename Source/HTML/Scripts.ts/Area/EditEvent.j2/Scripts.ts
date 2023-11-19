
EditAreaEvent.Inputs.DATETIME = <HTMLInputElement>document.getElementById(${{EditEventModalDatetimeInput}}$);
EditAreaEvent.Inputs.PERCENTAGE_RANGE = <HTMLInputElement>document.getElementById(${{EditEventModalPercentRangeInput}}$);
EditAreaEvent.Inputs.PERCENTAGE_INPUT = <HTMLInputElement>document.getElementById(${{EditEventModalPercentInputInput}}$);


EditAreaEvent.update_percentage_range = function update_percentage_range(input: HTMLInputElement)
{
	EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber = Math.floor(EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber);
	if(EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber > 100)
	{
		EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber = 100;
	}
	if(EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber < 0)
	{
		EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber = 0;
	}
	EditAreaEvent.Inputs.PERCENTAGE_RANGE.valueAsNumber = EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber;
}


EditAreaEvent.update_percentage_input = function update_percentage_input(range: HTMLInputElement)
{
	EditAreaEvent.Inputs.PERCENTAGE_INPUT.valueAsNumber = EditAreaEvent.Inputs.PERCENTAGE_RANGE.valueAsNumber;
}
