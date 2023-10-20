

interface NewAreaEventModalType
{
	Inputs:
	{
		PERCENTAGE_RANGE?: HTMLInputElement;
		PERCENTAGE_INPUT?: HTMLInputElement;
		DATETIME?: HTMLInputElement;
	},
	update_percentage_range?: (element: HTMLInputElement) => void;
	update_percentage_input?: (element: HTMLInputElement) => void;
}
