

function html_to_element(html: string): DocumentFragment
{
	return <DocumentFragment>document.createRange().createContextualFragment(html);
}
