import datetime
import sqlite3
import ui

X,Y = ui.get_screen_size()
XBUFFER, YBUFFER = 10, 10

def dateAction(sender):
	datePicker.date = sender.date
	view.remove_subview(label)
	view.remove_subview(datePicker)
	view.add_subview(timeTable)


class Booking (object):
	def __init__(self, *args, **kwargs):
		self.date = None
		self.time = None
	
	def create_table(self, *args, **kwargs):
		connect = sqlite3.connect('MyDB.db')
		cursor = connect.cursor()
		cursor.execute("CREATE TABLE IF NOT EXISTS Data (Date TEXT, Time TEXT)")
		connect.commit()
		connect.close()
	
	def insert(self, Date, Time):
		self.date = Date
		self.time = Time
		connect = sqlite3.connect('MyDB.db')
		cursor = connect.cursor()
		cursor.execute("INSERT INTO Data VALUES (?,?)", (self.date, self.time))
		connect.commit()
		connect.close()
	
	def show_data(self, *args, **kwargs):
		connect = sqlite3.connect('MyDB.db')
		cursor = connect.cursor()
		cursor.execute('SELECT * FROM Data')
		allrows = cursor.fetchall()
		connect.close()
		return allrows
		
	def check_booking(self, Date, Time):
		self.date = Date
		self.time = Time
		self.available = False
		connect = sqlite3.connect('MyDB.db')
		cursor = connect.cursor()
		cursor.execute("SELECT * FROM Data WHERE Date LIKE ? AND Time LIKE ?", (self.date, self.time,))
		self.allrows = cursor.fetchall()
		
		try: self.unavailable = self.allrows[0]
		except: self.available = True
		
		
class MyTableViewDataSource (object):
	def __init__(self):
		self.times = []
		
		for i in range(7,20):
			if i < 10:
				self.times.append('0'+str(i)+':00')
				self.times.append('0'+str(i)+':30')
			else:
				self.times.append(str(i)+':00')
				self.times.append(str(i)+':30')
		
	def tableview_number_of_sections(self, tableview):
		return 1

	def tableview_number_of_rows(self, tableview, section):
		return 26

	def tableview_cell_for_row(self, tableview, section, row):
		self.datePickerDate = datePicker.date.strftime('%d/%m/%Y')
		self.Date = self.datePickerDate
		self.Time = self.times[row]
		self.cell = ui.TableViewCell()
		self.cell.background_color = None
		self.cell.text_label.text = self.times[row]
		self.cell.text_label.alignment = ui.ALIGN_CENTER
		
		booking.check_booking(self.Date, self.Time)
		
		if booking.available == False:
			self.cell.background_color = 'blue'
			tableview.reload
			
		return self.cell
		

	def tableview_title_for_header(self, tableview, section):
		return 'Available Times'

	def tableview_can_delete(self, tableview, section, row):
		return False



class MyTableViewDelegate (object):
	def tableview_did_select(self, tableview, section, row):
		self.listSelect = timeTable.selected_row[1]
		self.Time = timeTableDataSource.times[self.listSelect]
		
		booking.insert(timeTableDataSource.Date, self.Time)
		
		view.remove_subview(timeTable)
		view.add_subview(label)
		view.add_subview(datePicker)
		
		pass
	

booking = Booking()
booking.create_table()

view = ui.View(frame=(0,0,X,Y), background_color='white')

label = ui.Label(text='Select Date', frame=(XBUFFER,2*YBUFFER,X-(2*XBUFFER),(8*YBUFFER)), font=('Arial',30), text_color='black', alignment=ui.ALIGN_CENTER)

datePicker = ui.DatePicker(mode = ui.DATE_PICKER_MODE_DATE)
datePicker.frame = (XBUFFER,2*YBUFFER,X-(2*XBUFFER),Y-(2*YBUFFER))
datePicker.action = dateAction

timeTable = ui.TableView()
timeTableDataSource = MyTableViewDataSource()
timeTableDelegate = MyTableViewDelegate()
timeTable.row_height = 60
timeTable.frame = (0,0,X,Y-60)
timeTable.multitouch_enabled = True
timeTable.data_source = timeTableDataSource
timeTable.delegate = timeTableDelegate

view.add_subview(label)
view.add_subview(datePicker)

view.present()
