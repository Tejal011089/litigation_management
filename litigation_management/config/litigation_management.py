from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				{
					"type": "doctype",
					"name": "Case",
					"description": _("Court Case Details"),
				},
				
			]
		},
		{
			"label": _("Masters"),
			"icon": "icon-book",
			"items": [
				{
					"type": "doctype",
					"name": "Litigator",
					"description": _("Litigators Details"),
				},
				{
					"type": "doctype",
					"name": "Petitioner",
					"description": _("Petitioner Details"),
				},
				{
					"type": "doctype",
					"name": "Court",
					"description": _("Court Details"),
				},
			]
		},
	]
