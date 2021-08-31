people = {
	"person": [
	{
		"name": {
			"first": "Tom",
			"middle": "M",
		},
		"dob": {
			"year": 2012,
			"month": 4,
			"day": 23,
			"hour": 18,
			"minute": 25,
			"second": 43,
		}
	},
	{
		"name": {
			"first": "Anna",
			"middle": "M",
		},
		"dob": {
			"year": 2015,
			"month": 4,
			"day": 23,
			"hour": 18,
			"minute": 25,
			"second": 43,
		}
	},
	{
		"name": {
			"first": "Tom",
			"middle": "M",
		},
		"dob": {
			"year": 2012,
			"month": 4,
			"day": 23,
			"hour": 18,
			"minute": 25,
			"second": 45,
		}
	},
	{
		"name": {
			"first": "Katy",
			"middle": "N",
		},
		"dob": {
			"year": 2010,
			"month": 4,
			"day": 23,
			"hour": 18,
			"minute": 25,
			"second": 45,
		}
	},
	{
		"name": {
			"first": "Bob",
			"middle": "M",
		},
		"dob": {
			"year": 2017,
			"month": 7,
			"day": 23,
			"hour": 20,
			"minute": 25,
			"second": 45,
		}
	}
]}

sample_object = [
{
	'Name': 'Farhad', 
	'Surname': 'Malik',
	'Blogs': {
		'BlogNam': 'Python1',
		'Date1': '20180901'
	}
},
{
	'Name': 'Farhad2',
	'Surname': 'Malik2',
	'Blogs': {
		'BlogName': 'Python3',
		'Date1': '20180101'
	}
}]


from datetime import datetime


def sort_by_dob(people):
	people['person'].sort(key = lambda person: datetime(
		person['dob']['year'],
		person['dob']['month'],
		person['dob']['day'],
		person['dob']['hour'],
		person['dob']['minute'],
		person['dob']['second']
		)
	)
	return people


def sort_by_first_name(peolpe):
	people['person'].sort(key = lambda person: person['name']['first'])
	return people


def sort_by_first_name_desc(peolpe):
	people['person'].sort(key = lambda person: person['name']['first'], reverse=True)
	return people


def dict_separator(persons):
	dict1, dict2 = [], []
	for p in persons:
		tmp1, tmp2 = {}, {}
		for k, v in p.items():
			if isinstance(v, dict):
				tmp2['ParentID'] = p['Name']
				tmp2.update(v)
			else:
				tmp1[k] = v
		dict1.append(tmp1)
		dict2.append(tmp2)

	return [dict1, dict2]


if __name__=='__main__':

	print(dict_separator(sample_object)[0])
	print(dict_separator(sample_object)[1])

