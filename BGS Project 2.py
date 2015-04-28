concepts = ['Important Concepts',
['1. HTML', '"Hypertext Markup Lnaguage", or "HTML", is how computers communicate to each other how a webpage should look. Each HTML document contains multiple "elements", denoted by "tags". Some tags (inline tags) affect how the text appears, while others (block tags) form boxes around the content. In this way, HTML is just a series of nested boxes. Each sub-box is indented in the code in order to better display the ridgid, methodical, logical thinking employed by the computers.'],
['2. CSS', 'The more code that is needed in the HTML document, the more likely it is that a mistake will be made. For this reason, if multiple elements need to look the same, they are given tags assigning them to a specific "class". A separate "Cascading Style Sheet", or "CSS", is then created which specifies how ALL members of a given class are to be presented.'],
['3. Python', 'While HTML interacts directly with the computer, Python acts as a go-between for the programmer and the computer. It allows for variables to be lists, which can then be directly modified without having to directly reassign the variable. Lists may also be checked for the presence and/or location of a specific element, or checked for length. Although these last few things can also be done with strings in HTML, they are a bit simpler to execute in Python.'],
['4. Loops', 'Python is especially useful because it allows for the implementation of "loops", which can allow for code to be run multiple times or only in certain circumstances. "If" loops only execute thier code if a certain condition exists. "Else" clauses may be added after an "if" loop for if it does not, otherwise it will simply not execute. "While" loops will CONTINUOUSLY execute so long as some condition exists. For this reason, they are usually paired with a new "counting variable", which gets modified after every iteration, and the condition is dependet on its value. "For" loops look at each and every element within a list and executes the code for each one.']]
def get_html(list):
	title = ''
	for i in list:
		if len(i) != 2:
			title = i
	html_0 ='''<head>
  				<title>BGS Project</title>
  				<link rel="stylesheet" href="BGS-style.css">
			</head>
			<body>
				<h1>''' + title + '''</hi>'''
	html_1 = '''<div class="lesson">
					<div class="concept-tile">''' + list[1][0] + '''</div>
					<div class="concept-description">''' + list[1][1]
	html_2 = '''</div>
				</div>
				<div class="lesson">
					<div class="concept-tile">''' + list[2][0] + '''</div>
					<div class="concept-description">''' + list[2][1]
	html_3 =  '''</div>
				</div>
				<div class="lesson">
					<div class="concept-tile">''' + list[3][0] + '''</div>
					<div class="concept-description">''' + list[3][1]
	html_4 =  '''</div>
				</div>
				<div class="lesson">
					<div class="concept-tile">''' + list[4][0] + '''</div>
					<div class="concept-description">''' + list[4][1]
	html_end = '''</div>
				</div'''
	full_html = html_0 + html_1 + html_2 + html_3 + html_4 + html_end

	return full_html

print get_html(concepts)