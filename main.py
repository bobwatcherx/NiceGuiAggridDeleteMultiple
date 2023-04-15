from nicegui import ui

ui.label("delete multiple")

# NOW CREATE GRID TABLE
grid = ui.aggrid({
	"columnDefs":[
	{
		"headerName":"Select",
		"headerCheckboxSelection":True,
		# ENABLE CHECKBOX SELECTTION
		"checkboxSelection":True,
		"showDisabledCheckboxes":True

	},
	# CREATE COLUMN NAME AND AGE FOR SAMPLE 
	{
		"headerName":"Name","field":"name"
	},
	{
		"headerName":"Age","field":"age"
	},

	],
	# NOW ADD DATA TO TABLE
	"rowData":[
		{"name":"jun","age":12},
		{"name":"gaga","age":22},
		{"name":"ope","age":45},
	],
	"rowSelection":"multiple",
	"suppressRowClickSelection":True

	})

async def deletemultiple():
	# NOW GET YOU CLICK SELECT FROM CHECKBOX
	you_select = await grid.get_selected_rows()
	# AND NOW GET ALL DATA FROM TABLE aggrid
	get_all_data = grid.options['rowData']
	print(get_all_data)
	# NOW IF YOU SELECT > 0
	if you_select:
		# loop and remove from TABLE
		for row in  you_select:
			if row in get_all_data:
				# THEN REMOVE DATA multiple
				get_all_data.remove(row)
				ui.notify("Success Delete")

	# IF NO SELECT DATA 
	else:
		ui.notify("NO DATA SELECTED GUYS")
	# AND LAST UPDATE TABLE aggrid again
	# FOR REFRESH TABLE
	grid.update()


# NOW CREATE BUTTON FOR DELETE multiple
ui.button("delete multiple",on_click=deletemultiple).classes("bg-red")



# RUN IN DESKTOP MODE
# ENABLE native=True

ui.run(native=True)
